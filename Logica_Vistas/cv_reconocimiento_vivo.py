"""
Vista de reconocimiento facial en vivo.
Detecta rostros con la cámara y los identifica contra los embeddings registrados.
"""
from __future__ import annotations

import logging
import time
from typing import Optional

import cv2
import numpy as np
from PySide6.QtCore import Qt, QSize, QTimer
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QListWidgetItem, QMessageBox, QWidget

from Vistas.personal.ui_reconocimiento_vivo import Ui_ReconocimientoVivo
from Vistas.recursos.estilos import (
    QSS_LISTA, COLOR_PRIMARIO, COLOR_SECUNDARIO, COLOR_ERROR,
)
from Logica.svc_rostro import SvcRostro, UMBRAL_MATCH, UMBRAL_BUENO
from Logica.cl_rostro_empleado import ClRostroEmpleado, RostroParaReconocer
from Logica.thread_camara import ThreadCamara
from Conexion.cn_sesion import Sesion

log = logging.getLogger(__name__)


class CvReconocimientoVivo(QWidget):

    # Procesamos detección cada N frames (para no saturar CPU)
    PROCESAR_CADA_N_FRAMES = 3

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ReconocimientoVivo()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_LISTA)

        self._cl = ClRostroEmpleado()
        self._svc = SvcRostro()
        self._sesion = Sesion()

        # Cache de embeddings registrados
        self._registrados: list[RostroParaReconocer] = []

        self._thread: Optional[ThreadCamara] = None
        self._frame_count = 0
        self._fps_t0 = time.time()
        self._fps_frames = 0
        self._auto_iniciado = False

        # Para no spamear el panel lateral con la misma persona
        self._ultima_deteccion: dict[int, float] = {}

        self.ui.btnIniciar.clicked.connect(lambda: self._iniciar_camara(False))
        self.ui.btnDetener.clicked.connect(self._detener_camara)
        self.ui.btnRecargar.clicked.connect(self._cargar_registrados)
        self.ui.btnDetener.setEnabled(False)

        self.ui.lblVideo.setText(
            "Cargando modelos...\n\n"
            "(La primera vez descarga ~37 MB. Espera unos segundos.)"
        )

        self._cargar_registrados()

    # Auto-iniciar cuando el widget se muestra por primera vez
    def showEvent(self, ev) -> None:
        super().showEvent(ev)
        if not self._auto_iniciado:
            self._auto_iniciado = True
            QTimer.singleShot(200, lambda: self._iniciar_camara(silencioso=True))

    # ------------------------------------------------------------------
    def _cargar_registrados(self) -> None:
        self._registrados = self._cl.cargar_todos_para_reconocer(
            self._sesion.usuario.id_fundo
        )
        # Agrupar por empleado para contar
        ids = {r.id_empleado for r in self._registrados}
        self.ui.lblCount.setText(
            f"Empleados con rostro: <b>{len(ids)}</b>  "
            f"(<i>{len(self._registrados)} embeddings</i>)"
        )

    def _iniciar_camara(self, silencioso: bool = False) -> None:
        """silencioso=True: no muestra el diálogo si no hay rostros (para auto-start)."""
        if self._thread is not None and self._thread.isRunning():
            return
        if not self._registrados and not silencioso:
            r = QMessageBox.question(
                self, "Sin registros",
                "No hay rostros registrados todavía. ¿Iniciar igualmente?\n"
                "(Solo verás detecciones como 'Desconocido')",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if r != QMessageBox.StandardButton.Yes:
                return
        log.info("Iniciando cámara (registrados=%d)", len(self._registrados))
        self.ui.lblVideo.setText("Abriendo cámara...")
        self._thread = ThreadCamara()
        self._thread.frame_listo.connect(self._on_frame)
        self._thread.error.connect(self._on_error)
        self._thread.start()
        self.ui.btnIniciar.setEnabled(False)
        self.ui.btnDetener.setEnabled(True)

    def _detener_camara(self) -> None:
        if self._thread is not None:
            self._thread.detener()
            self._thread = None
        self.ui.lblVideo.setText("Cámara detenida")
        self.ui.lblVideo.setPixmap(QPixmap())
        self.ui.btnIniciar.setEnabled(True)
        self.ui.btnDetener.setEnabled(False)

    def _on_error(self, msg: str) -> None:
        log.error("Error cámara: %s", msg)
        self.ui.lblVideo.setText("✗ Cámara no disponible")
        QMessageBox.critical(
            self, "Error de cámara",
            f"{msg}\n\n"
            "Si tienes cámara: ve a Configuración de Windows → "
            "Privacidad → Cámara y permite el acceso a aplicaciones de escritorio."
        )
        self._detener_camara()

    # ------------------------------------------------------------------
    def _on_frame(self, frame_bgr: np.ndarray, qimg: QImage) -> None:
        self._frame_count += 1
        self._fps_frames += 1
        ahora = time.time()
        if ahora - self._fps_t0 >= 1.0:
            fps = self._fps_frames / (ahora - self._fps_t0)
            self.ui.lblFps.setText(f"FPS: {fps:.1f}")
            self._fps_t0 = ahora
            self._fps_frames = 0

        # Procesamos detección cada N frames
        if self._frame_count % self.PROCESAR_CADA_N_FRAMES != 0:
            self._mostrar(frame_bgr)
            return

        try:
            rostros = self._svc.detectar(frame_bgr)
        except Exception as e:
            log.exception("Error detectando")
            self._mostrar(frame_bgr)
            return

        for rostro in rostros:
            x1, y1, x2, y2 = [int(v) for v in rostro.bbox]
            emb = rostro.normed_embedding

            # Buscar mejor match
            mejor = None
            mejor_sim = -1.0
            for reg in self._registrados:
                sim = self._svc.comparar(emb, reg.embedding)
                if sim > mejor_sim:
                    mejor_sim = sim
                    mejor = reg

            if mejor and mejor_sim >= UMBRAL_MATCH:
                etiqueta = f"{mejor.nombre_completo} ({mejor_sim:.2f})"
                color = (0, 200, 0) if mejor_sim >= UMBRAL_BUENO else (0, 165, 255)
                self._registrar_deteccion(mejor, mejor_sim,
                                          frame_bgr, rostro.bbox)
            else:
                etiqueta = f"Desconocido ({mejor_sim:.2f})" if mejor else "Desconocido"
                color = (0, 0, 220)

            cv2.rectangle(frame_bgr, (x1, y1), (x2, y2), color, 2)
            # Fondo del texto
            (tw, th), _ = cv2.getTextSize(etiqueta,
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(frame_bgr, (x1, y1 - th - 8),
                          (x1 + tw + 8, y1), color, -1)
            cv2.putText(frame_bgr, etiqueta, (x1 + 4, y1 - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        self._mostrar(frame_bgr)

    def _mostrar(self, frame_bgr: np.ndarray) -> None:
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        h, w, _ = rgb.shape
        img = QImage(rgb.data, w, h, w * 3, QImage.Format.Format_RGB888)
        self.ui.lblVideo.setPixmap(QPixmap.fromImage(img).scaled(
            self.ui.lblVideo.size(), Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))

    def _registrar_deteccion(self, reg: RostroParaReconocer,
                             similitud: float, frame_bgr: np.ndarray,
                             bbox) -> None:
        """Añade la detección al panel lateral, con cooldown de 3 segundos."""
        ahora = time.time()
        if ahora - self._ultima_deteccion.get(reg.id_empleado, 0) < 3.0:
            return
        self._ultima_deteccion[reg.id_empleado] = ahora

        thumb = self._svc.thumb_jpeg(frame_bgr, bbox, tam=64)
        item = QListWidgetItem(
            f"{reg.nombre_completo}\n"
            f"Cód: {reg.codigo}  ·  Sim: {similitud:.2f}  ·  "
            f"{time.strftime('%H:%M:%S')}"
        )
        if thumb:
            pm = QPixmap()
            pm.loadFromData(thumb, "JPEG")
            item.setIcon(QIcon(pm))
        item.setSizeHint(QSize(0, 56))
        self.ui.lstDetecciones.insertItem(0, item)
        # Limitar a 30 items
        while self.ui.lstDetecciones.count() > 30:
            self.ui.lstDetecciones.takeItem(self.ui.lstDetecciones.count() - 1)

    # ------------------------------------------------------------------
    def hideEvent(self, ev) -> None:
        self._detener_camara()
        super().hideEvent(ev)

    def closeEvent(self, ev) -> None:
        self._detener_camara()
        super().closeEvent(ev)
