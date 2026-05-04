"""
Servicio de reconocimiento facial.
Wrapper alrededor de InsightFace + utilidades de comparación.

El modelo se carga UNA sola vez (singleton, lazy).
La primera llamada descarga el modelo (~30MB) en ~/.insightface/
"""
from __future__ import annotations

import logging
from typing import Optional

import numpy as np

log = logging.getLogger(__name__)


# ----- Umbrales -----
# Cosine similarity entre 2 embeddings normalizados:
#   > 0.55 → posible match
#   > 0.65 → match seguro
UMBRAL_MATCH = 0.55
UMBRAL_BUENO = 0.65

CALIDAD_MINIMA_REGISTRO = 0.65   # det_score mínimo para aceptar el registro


class SvcRostro:
    """Servicio singleton de reconocimiento facial."""

    _instancia: Optional["SvcRostro"] = None
    _app = None  # FaceAnalysis

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def _cargar_modelo(self):
        """Carga el modelo InsightFace (lazy)."""
        if self._app is not None:
            return self._app

        log.info("Cargando modelo InsightFace (puede demorar la primera vez)...")
        from insightface.app import FaceAnalysis

        self._app = FaceAnalysis(
            name="buffalo_s",                   # ~30MB, rápido
            providers=["CPUExecutionProvider"],
        )
        self._app.prepare(ctx_id=0, det_size=(640, 640))
        log.info("Modelo InsightFace listo.")
        return self._app

    # ------------------------------------------------------------------
    def detectar(self, img_bgr: np.ndarray):
        """Detecta rostros y devuelve lista de Face (con bbox + embedding)."""
        app = self._cargar_modelo()
        return app.get(img_bgr)

    def detectar_uno(self, img_bgr: np.ndarray):
        """Devuelve el rostro más grande (None si no hay)."""
        rostros = self.detectar(img_bgr)
        if not rostros:
            return None
        # El más grande por área del bbox
        def area(r):
            x1, y1, x2, y2 = r.bbox
            return (x2 - x1) * (y2 - y1)
        return max(rostros, key=area)

    # ------------------------------------------------------------------
    @staticmethod
    def comparar(emb_a: np.ndarray, emb_b: np.ndarray) -> float:
        """Cosine similarity entre 2 embeddings ya normalizados."""
        return float(np.dot(emb_a, emb_b))

    @staticmethod
    def serializar(emb: np.ndarray) -> bytes:
        """np.array → bytes para guardar en BD (BYTEA)."""
        return np.asarray(emb, dtype=np.float32).tobytes()

    @staticmethod
    def deserializar(data: bytes) -> np.ndarray:
        """BYTEA → np.array."""
        return np.frombuffer(data, dtype=np.float32)

    # ------------------------------------------------------------------
    @staticmethod
    def thumb_jpeg(img_bgr: np.ndarray, bbox, tam: int = 100) -> bytes:
        """Recorta y redimensiona el rostro a JPEG bytes."""
        import cv2
        x1, y1, x2, y2 = [int(v) for v in bbox]
        # Margen
        h, w = img_bgr.shape[:2]
        m = int(0.15 * max(x2 - x1, y2 - y1))
        x1 = max(0, x1 - m); y1 = max(0, y1 - m)
        x2 = min(w, x2 + m); y2 = min(h, y2 + m)
        recorte = img_bgr[y1:y2, x1:x2]
        if recorte.size == 0:
            return b""
        recorte = cv2.resize(recorte, (tam, tam),
                             interpolation=cv2.INTER_AREA)
        ok, buf = cv2.imencode(".jpg", recorte,
                               [cv2.IMWRITE_JPEG_QUALITY, 85])
        return buf.tobytes() if ok else b""
