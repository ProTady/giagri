"""
Diálogo de registro guiado de rostros.

Flujo: la cámara indica al usuario dónde mirar (frente, izquierda, derecha,
arriba, abajo) y captura automáticamente cuando lo hace correctamente
durante 1 segundo continuo.
"""
from __future__ import annotations

import logging
import time
from typing import Optional

import cv2
import numpy as np
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QDialog, QListWidgetItem, QMessageBox

from Vistas.personal.ui_capturar_rostro import Ui_CapturarRostro
from Vistas.recursos.estilos import (
    QSS_FORM, RUTA_ICONO, COLOR_PRIMARIO, COLOR_SECUNDARIO, COLOR_ERROR,
    COLOR_TEXTO_TENUE,
)
from Logica.svc_rostro import SvcRostro, CALIDAD_MINIMA_REGISTRO
from Logica.cl_rostro_empleado import ClRostroEmpleado
from Logica.thread_camara import ThreadCamara
from Conexion.cn_sesion import Sesion

log = logging.getLogger(__name__)


# Secuencia de capturas (mínimas) y sus instrucciones
SECUENCIA = [
    ("frente",    "Mira al frente, recto a la cámara"),
    ("izquierda", "Gira la cabeza a tu IZQUIERDA"),
    ("derecha",   "Gira la cabeza a tu DERECHA"),
]
# Tiempo que debes mantener la posición correcta (segundos)
ESTABILIDAD_REQUERIDA = 1.2


class CvCapturarRostro(QDialog):

    def __init__(self, id_empleado: int, nombre_empleado: str,
                 parent=None):
        super().__init__(parent)
        self.ui = Ui_CapturarRostro()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_FORM)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))

        self._id_empleado = id_empleado
        self._cl = ClRostroEmpleado()
        self._svc = SvcRostro()
        self._sesion = Sesion()

        self.ui.lblEmpleado.setText(f"<b>{nombre_empleado}</b>")

        # Estado de la guía
        self._frame_actual: Optional[np.ndarray] = None
        self._rostro_actual = None
        self._idx_objetivo = 0
        self._estable_desde: Optional[float] = None
        self._capturando = False

        self.ui.btnCapturarManual.clicked.connect(self._capturar_manual)
        self.ui.btnReiniciar.clicked.connect(self._reiniciar_guia)
        self.ui.btnEliminarSel.clicked.connect(self._eliminar_seleccionado)
        self.ui.btnCerrar.clicked.connect(self.accept)

        self._poblar_objetivos()
        self._cargar_registrados()
        self._iniciar_camara()

    # ------------------------------------------------------------------
    def _iniciar_camara(self) -> None:
        self._thread = ThreadCamara()
        self._thread.frame_listo.connect(self._on_frame)
        self._thread.error.connect(self._on_error)
        self._thread.start()

    def _on_error(self, msg: str) -> None:
        QMessageBox.critical(
            self, "Error de cámara",
            f"{msg}\n\nVe a Configuración → Privacidad → Cámara y "
            "permite el acceso a aplicaciones de escritorio."
        )
        self.reject()

    # ------------------------------------------------------------------
    def _poblar_objetivos(self) -> None:
        self.ui.lstObjetivos.clear()
        for i, (codigo, instr) in enumerate(SECUENCIA):
            item = QListWidgetItem(f"  {i+1}. {codigo.capitalize()}")
            item.setData(Qt.ItemDataRole.UserRole, codigo)
            self.ui.lstObjetivos.addItem(item)
        self._actualizar_lista_objetivos()

    def _actualizar_lista_objetivos(self) -> None:
        for i in range(self.ui.lstObjetivos.count()):
            item = self.ui.lstObjetivos.item(i)
            codigo = item.data(Qt.ItemDataRole.UserRole)
            base = f"  {i+1}. {codigo.capitalize()}"
            if i < self._idx_objetivo:
                item.setText(f"✔ {base[2:]}")
                item.setForeground(Qt.GlobalColor.darkGreen)
            elif i == self._idx_objetivo:
                item.setText(f"➤ {base[2:]}")
                f = item.font(); f.setBold(True); item.setFont(f)
            else:
                item.setText(base)
                item.setForeground(Qt.GlobalColor.gray)

    # ------------------------------------------------------------------
    def _on_frame(self, frame_bgr: np.ndarray, _qimg) -> None:
        # Frame "espejo" para mostrar (más natural)
        preview = cv2.flip(frame_bgr, 1)
        # IMPORTANTE: detectamos sobre el frame ORIGINAL (sin espejo)
        # así el embedding queda igual que en reconocimiento en vivo.
        self._frame_actual = frame_bgr

        try:
            rostro = self._svc.detectar_uno(frame_bgr)
        except Exception as e:
            log.exception("Error detectando")
            self._dibujar_y_mostrar(preview)
            return

        self._rostro_actual = rostro

        if self._idx_objetivo >= len(SECUENCIA):
            self._set_instruccion("✔ Listo. Captura completa.", COLOR_SECUNDARIO)
            self.ui.prgEstable.setValue(100)
            self._dibujar_y_mostrar(preview)
            return

        if rostro is None:
            self._set_instruccion("Acércate a la cámara",
                                  COLOR_TEXTO_TENUE)
            self.ui.prgEstable.setValue(0)
            self._estable_desde = None
            self._dibujar_y_mostrar(preview)
            return

        if rostro.det_score < CALIDAD_MINIMA_REGISTRO:
            self._set_instruccion("Mejora la luz / acércate más", "#E67E22")
            self.ui.prgEstable.setValue(0)
            self._estable_desde = None
            self._dibujar_bbox(preview, rostro, (0, 165, 255))
            self._dibujar_y_mostrar(preview)
            return

        objetivo, instruccion = SECUENCIA[self._idx_objetivo]
        direccion, yaw, pitch = rostro.estimar_direccion()

        if direccion == objetivo:
            ahora = time.time()
            if self._estable_desde is None:
                self._estable_desde = ahora
            transcurrido = ahora - self._estable_desde
            progreso = min(100, int(100 * transcurrido / ESTABILIDAD_REQUERIDA))
            self.ui.prgEstable.setValue(progreso)
            self._set_instruccion(
                f"✓ Posición correcta ({objetivo}). Mantén... {progreso}%",
                COLOR_SECUNDARIO,
            )
            self._dibujar_bbox(preview, rostro, (0, 200, 0))
            if transcurrido >= ESTABILIDAD_REQUERIDA and not self._capturando:
                self._capturar_automatico(objetivo)
        else:
            self._estable_desde = None
            self.ui.prgEstable.setValue(0)
            self._set_instruccion(instruccion, COLOR_PRIMARIO)
            self._dibujar_bbox(preview, rostro, (0, 165, 255))

        self._dibujar_y_mostrar(preview)

    def _dibujar_bbox(self, frame, rostro, color) -> None:
        """Dibuja bbox sobre frame ESPEJADO (recordando que rostro fue
        detectado en frame original)."""
        h, w = frame.shape[:2]
        x1, y1, x2, y2 = [int(v) for v in rostro.bbox]
        # Espejar coordenadas X
        nx1 = w - x2
        nx2 = w - x1
        cv2.rectangle(frame, (nx1, y1), (nx2, y2), color, 2)

    def _dibujar_y_mostrar(self, frame_bgr: np.ndarray) -> None:
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        h, w, _ = rgb.shape
        img = QImage(rgb.data, w, h, w * 3, QImage.Format.Format_RGB888)
        self.ui.lblVideo.setPixmap(QPixmap.fromImage(img).scaled(
            self.ui.lblVideo.size(), Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))

    def _set_instruccion(self, texto: str, color: str) -> None:
        self.ui.lblInstr.setText(texto)
        self.ui.lblInstr.setStyleSheet(
            f"color:{color}; font-size:18px; font-weight:bold;"
        )

    # ------------------------------------------------------------------
    def _capturar_automatico(self, angulo: str) -> None:
        if self._frame_actual is None or self._rostro_actual is None:
            return
        self._capturando = True
        try:
            self._guardar_rostro(angulo, self._rostro_actual)
        finally:
            self._capturando = False
            self._estable_desde = None
            self._idx_objetivo += 1
            self._actualizar_lista_objetivos()

    def _capturar_manual(self) -> None:
        """Captura manual: usa el ángulo objetivo actual o 'frente' si terminó."""
        if self._rostro_actual is None:
            QMessageBox.information(self, "Capturar",
                                    "No se detecta ningún rostro.")
            return
        if self._rostro_actual.det_score < CALIDAD_MINIMA_REGISTRO:
            QMessageBox.information(self, "Calidad baja",
                                    "Mejora la iluminación o acércate.")
            return
        if self._idx_objetivo < len(SECUENCIA):
            angulo = SECUENCIA[self._idx_objetivo][0]
        else:
            angulo = "extra"
        self._capturando = True
        try:
            self._guardar_rostro(angulo, self._rostro_actual)
        finally:
            self._capturando = False
            self._estable_desde = None
            if self._idx_objetivo < len(SECUENCIA):
                self._idx_objetivo += 1
                self._actualizar_lista_objetivos()

    def _guardar_rostro(self, angulo: str, rostro) -> None:
        thumb = self._svc.thumb_jpeg(self._frame_actual, rostro.bbox)
        try:
            self._cl.registrar(
                id_empleado=self._id_empleado,
                embedding=rostro.normed_embedding,
                thumb_jpeg=thumb,
                angulo=angulo,
                calidad=float(rostro.det_score),
                registrado_por=self._sesion.usuario.id_usuario,
            )
        except Exception as e:
            log.exception("Error guardando rostro")
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_registrados()

    def _reiniciar_guia(self) -> None:
        self._idx_objetivo = 0
        self._estable_desde = None
        self.ui.prgEstable.setValue(0)
        self._actualizar_lista_objetivos()
        self._set_instruccion("Reiniciado. Mira al frente.", COLOR_PRIMARIO)

    # ------------------------------------------------------------------
    def _cargar_registrados(self) -> None:
        self.ui.lstRegistrados.clear()
        registrados = self._cl.listar_de_empleado(self._id_empleado)
        for r in registrados:
            item = QListWidgetItem(f"{r.angulo}\n{r.calidad:.2f}")
            item.setData(Qt.ItemDataRole.UserRole, r.id_rostro)
            if r.foto_thumb:
                pm = QPixmap()
                pm.loadFromData(r.foto_thumb, "JPEG")
                item.setIcon(QIcon(pm))
            item.setSizeHint(QSize(86, 96))
            self.ui.lstRegistrados.addItem(item)

    def _eliminar_seleccionado(self) -> None:
        item = self.ui.lstRegistrados.currentItem()
        if item is None:
            return
        id_r = item.data(Qt.ItemDataRole.UserRole)
        r = QMessageBox.question(
            self, "Eliminar rostro", "¿Eliminar este registro facial?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl.eliminar(id_r)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_registrados()

    # ------------------------------------------------------------------
    def closeEvent(self, ev) -> None:
        try:
            self._thread.detener()
        except Exception:
            pass
        super().closeEvent(ev)
