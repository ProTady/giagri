"""
Diálogo para capturar rostros de un empleado con cámara en vivo.
"""
from __future__ import annotations

import logging
from typing import Optional

import cv2
import numpy as np
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QImage, QPixmap
from PySide6.QtWidgets import QDialog, QListWidgetItem, QMessageBox

from Vistas.personal.ui_capturar_rostro import Ui_CapturarRostro
from Vistas.recursos.estilos import (
    QSS_FORM, RUTA_ICONO, COLOR_PRIMARIO, COLOR_SECUNDARIO, COLOR_ERROR,
)
from Logica.svc_rostro import SvcRostro, CALIDAD_MINIMA_REGISTRO
from Logica.cl_rostro_empleado import ClRostroEmpleado
from Logica.thread_camara import ThreadCamara
from Conexion.cn_sesion import Sesion

log = logging.getLogger(__name__)


class CvCapturarRostro(QDialog):
    """Dialog modal con cámara para registrar rostros."""

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

        # Último frame BGR + último rostro detectado (para capturar)
        self._frame_actual: Optional[np.ndarray] = None
        self._rostro_actual = None

        self.ui.lblEmpleado.setText(f"<b>{nombre_empleado}</b>")
        self.ui.btnCapturar.clicked.connect(self._capturar)
        self.ui.btnEliminarSel.clicked.connect(self._eliminar_seleccionado)
        self.ui.btnCerrar.clicked.connect(self.accept)

        self._cargar_registrados()
        self._iniciar_camara()

    # ------------------------------------------------------------------
    def _iniciar_camara(self) -> None:
        self._thread = ThreadCamara()
        self._thread.frame_listo.connect(self._on_frame)
        self._thread.error.connect(self._on_error_camara)
        self._thread.start()

    def _on_error_camara(self, msg: str) -> None:
        QMessageBox.critical(self, "Error de cámara", msg)
        self.reject()

    def _on_frame(self, frame_bgr: np.ndarray, qimg: QImage) -> None:
        """Cada frame: detectar y dibujar bbox; mostrar en label."""
        self._frame_actual = frame_bgr

        rostro = None
        try:
            rostro = self._svc.detectar_uno(frame_bgr)
        except Exception as e:
            log.exception("Error detectando rostro")
            self._actualizar_estado(f"Error: {e}", COLOR_ERROR)
            self.ui.lblVideo.setPixmap(QPixmap.fromImage(qimg).scaled(
                self.ui.lblVideo.size(), Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation))
            return

        self._rostro_actual = rostro

        # Dibujar bbox sobre el frame BGR y rehacer QImage
        if rostro is not None:
            x1, y1, x2, y2 = [int(v) for v in rostro.bbox]
            calidad = float(rostro.det_score)
            color = (0, 200, 0) if calidad >= CALIDAD_MINIMA_REGISTRO else (0, 165, 255)
            cv2.rectangle(frame_bgr, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame_bgr, f"{calidad:.2f}", (x1, y1 - 8),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
            self.ui.lblCalidad.setText(f"Calidad: <b>{calidad:.2f}</b>")
            if calidad >= CALIDAD_MINIMA_REGISTRO:
                self._actualizar_estado("Rostro OK ✓ Listo para capturar",
                                        COLOR_SECUNDARIO)
                self.ui.btnCapturar.setEnabled(True)
            else:
                self._actualizar_estado("Acércate / mejora la luz", "#E67E22")
                self.ui.btnCapturar.setEnabled(False)
        else:
            self.ui.lblCalidad.setText("Calidad: --")
            self._actualizar_estado("No se detecta rostro", COLOR_ERROR)
            self.ui.btnCapturar.setEnabled(False)

        # BGR → RGB → QImage para mostrar (con bbox dibujado)
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        h, w, _ = rgb.shape
        img = QImage(rgb.data, w, h, w * 3, QImage.Format.Format_RGB888)
        self.ui.lblVideo.setPixmap(QPixmap.fromImage(img).scaled(
            self.ui.lblVideo.size(), Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation))

    def _actualizar_estado(self, texto: str, color: str) -> None:
        self.ui.lblEstado.setText(texto)
        self.ui.lblEstado.setStyleSheet(f"color:{color}; font-weight:bold;")

    # ------------------------------------------------------------------
    def _capturar(self) -> None:
        if self._frame_actual is None or self._rostro_actual is None:
            return
        rostro = self._rostro_actual
        if rostro.det_score < CALIDAD_MINIMA_REGISTRO:
            QMessageBox.information(self, "Calidad baja",
                                    "Mejora la iluminación o acércate.")
            return

        emb = rostro.normed_embedding
        thumb = self._svc.thumb_jpeg(self._frame_actual, rostro.bbox)
        angulo = self.ui.cboAngulo.currentText()
        try:
            self._cl.registrar(
                id_empleado=self._id_empleado,
                embedding=emb,
                thumb_jpeg=thumb,
                angulo=angulo,
                calidad=float(rostro.det_score),
                registrado_por=self._sesion.usuario.id_usuario,
            )
        except Exception as e:
            log.exception("Error registrando rostro")
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_registrados()

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
            item.setSizeHint(QSize(96, 110))
            self.ui.lstRegistrados.addItem(item)
        self.ui.lblConteo.setText(f"Capturados: <b>{len(registrados)}</b>")

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
