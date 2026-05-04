"""
Thread de captura de cámara con OpenCV.
Emite QImage por cada frame para que la UI lo dibuje.
"""
from __future__ import annotations

import logging

import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage

log = logging.getLogger(__name__)


class ThreadCamara(QThread):
    """Thread independiente que lee frames de la cámara.

    Emite:
        frame_listo(np.ndarray BGR, QImage RGB)
        error(str)
    """
    frame_listo = Signal(np.ndarray, QImage)
    error = Signal(str)

    def __init__(self, indice_camara: int = 0, parent=None):
        super().__init__(parent)
        self._indice = indice_camara
        self._corriendo = False

    def run(self) -> None:
        cap = cv2.VideoCapture(self._indice, cv2.CAP_DSHOW)
        if not cap.isOpened():
            self.error.emit(
                f"No se pudo abrir la cámara #{self._indice}.\n"
                "Verifica que esté conectada y no la esté usando otra app."
            )
            return

        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

        self._corriendo = True
        try:
            while self._corriendo:
                ok, frame_bgr = cap.read()
                if not ok:
                    self.msleep(20)
                    continue
                # BGR (OpenCV) → RGB (Qt)
                rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
                h, w, _ = rgb.shape
                img = QImage(rgb.data, w, h, w * 3, QImage.Format.Format_RGB888)
                # Copy() porque rgb se libera al iterar
                self.frame_listo.emit(frame_bgr.copy(), img.copy())
                self.msleep(15)
        finally:
            cap.release()
            log.info("Cámara liberada")

    def detener(self) -> None:
        self._corriendo = False
        self.wait(2000)
