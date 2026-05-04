"""
Servicio de reconocimiento facial usando OpenCV YuNet + SFace.

Modelos (descarga automática a la carpeta `modelos/` la primera vez):
  - YuNet  (~340 KB) — detector de rostros con landmarks
  - SFace  (~37 MB)  — embeddings 128-dim para reconocimiento

Ventaja vs InsightFace: no requiere compilar nada, solo opencv-python.
"""
from __future__ import annotations

import logging
import urllib.request
from pathlib import Path
from typing import Optional

import cv2
import numpy as np

log = logging.getLogger(__name__)


# ----- Umbrales -----
# SFace usa cosine similarity (recomendado por OpenCV Zoo: 0.363)
# Subimos un poco para mejorar precisión:
UMBRAL_MATCH = 0.40   # posible match
UMBRAL_BUENO = 0.55   # match seguro

CALIDAD_MINIMA_REGISTRO = 0.65   # det_score mínimo para registrar


# ----- Modelos -----
_RAIZ = Path(__file__).resolve().parent.parent
CARPETA_MODELOS = _RAIZ / "modelos"

MODELOS = {
    "yunet": {
        "archivo": "face_detection_yunet_2023mar.onnx",
        "url": ("https://github.com/opencv/opencv_zoo/raw/main/models/"
                "face_detection_yunet/face_detection_yunet_2023mar.onnx"),
    },
    "sface": {
        "archivo": "face_recognition_sface_2021dec.onnx",
        "url": ("https://github.com/opencv/opencv_zoo/raw/main/models/"
                "face_recognition_sface/face_recognition_sface_2021dec.onnx"),
    },
}


def _descargar_modelo(clave: str) -> Path:
    """Descarga el modelo si no existe; devuelve la ruta local."""
    info = MODELOS[clave]
    CARPETA_MODELOS.mkdir(exist_ok=True)
    destino = CARPETA_MODELOS / info["archivo"]
    if destino.exists() and destino.stat().st_size > 1024:
        return destino
    log.info("Descargando modelo %s desde %s ...", clave, info["url"])
    print(f"[INFO] Descargando modelo {clave} (puede demorar la primera vez)...")
    urllib.request.urlretrieve(info["url"], destino)
    log.info("Modelo %s guardado en %s", clave, destino)
    return destino


class Rostro:
    """Resultado de detección: bbox + landmarks + embedding."""
    __slots__ = ("bbox", "det_score", "landmarks_5", "normed_embedding",
                 "_face_aligned")

    def __init__(self, bbox, det_score, landmarks_5,
                 normed_embedding, face_aligned):
        self.bbox = bbox                      # (x1, y1, x2, y2)
        self.det_score = det_score
        self.landmarks_5 = landmarks_5        # 5 puntos (10 floats)
        self.normed_embedding = normed_embedding  # 128 floats normalizados
        self._face_aligned = face_aligned     # imagen alineada (debug)

    def estimar_direccion(self) -> tuple[str, float, float]:
        """Estima la dirección desde landmarks. Devuelve (etiqueta, yaw, pitch).

        Convención (perspectiva del usuario; cámara SIN espejo):
            - 'derecha'   → usuario gira la cabeza a SU derecha
            - 'izquierda' → usuario gira la cabeza a SU izquierda
            - 'arriba'    → usuario mira hacia arriba
            - 'abajo'     → usuario mira hacia abajo
            - 'frente'    → al centro
        """
        lm = self.landmarks_5
        re_x, re_y = lm[0], lm[1]      # ojo derecho en la imagen
        le_x, le_y = lm[2], lm[3]      # ojo izquierdo en la imagen
        n_x,  n_y  = lm[4], lm[5]      # nariz
        mr_x, mr_y = lm[6], lm[7]      # comisura derecha
        ml_x, ml_y = lm[8], lm[9]      # comisura izquierda

        # Centro horizontal entre ojos y boca
        face_cx = (re_x + le_x + mr_x + ml_x) / 4
        face_cy_top = (re_y + le_y) / 2
        face_cy_bot = (mr_y + ml_y) / 2

        eye_dist = max(abs(le_x - re_x), 1.0)
        face_h = max(face_cy_bot - face_cy_top, 1.0)

        # Yaw normalizado: nariz desplazada horizontalmente
        yaw = (n_x - face_cx) / eye_dist

        # Pitch normalizado: posición vertical de la nariz entre ojos y boca
        # 0 = a la altura de los ojos; 1 = a la altura de la boca
        # Frente típico ~0.45-0.55. <0.35 = mirando arriba, >0.65 = abajo
        pitch_raw = (n_y - face_cy_top) / face_h

        # En cámara NO espejada:
        #   nariz a la IZQ del centro de la imagen (yaw < 0)
        #   = usuario gira a SU DERECHA
        UMBRAL_YAW = 0.18
        UMBRAL_PITCH_UP = 0.30
        UMBRAL_PITCH_DN = 0.65

        if yaw < -UMBRAL_YAW:
            etiqueta = "derecha"
        elif yaw > UMBRAL_YAW:
            etiqueta = "izquierda"
        elif pitch_raw < UMBRAL_PITCH_UP:
            etiqueta = "arriba"
        elif pitch_raw > UMBRAL_PITCH_DN:
            etiqueta = "abajo"
        else:
            etiqueta = "frente"
        return etiqueta, float(yaw), float(pitch_raw)


class SvcRostro:
    """Singleton — detector + recognizer cargados una vez."""

    _instancia: Optional["SvcRostro"] = None
    _detector = None
    _recognizer = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def _cargar(self):
        if self._detector is not None and self._recognizer is not None:
            return
        log.info("Cargando modelos de rostro...")
        ruta_yunet = _descargar_modelo("yunet")
        ruta_sface = _descargar_modelo("sface")

        self._detector = cv2.FaceDetectorYN.create(
            str(ruta_yunet), "", (320, 320),
            score_threshold=0.6, nms_threshold=0.3, top_k=5000,
        )
        self._recognizer = cv2.FaceRecognizerSF.create(
            str(ruta_sface), "",
        )
        log.info("Modelos de rostro listos.")

    # ------------------------------------------------------------------
    def _detectar_raw(self, img_bgr: np.ndarray):
        """Devuelve el array crudo de YuNet o None."""
        self._cargar()
        h, w = img_bgr.shape[:2]
        self._detector.setInputSize((w, h))
        _, faces = self._detector.detect(img_bgr)
        return faces

    def detectar(self, img_bgr: np.ndarray) -> list[Rostro]:
        """Detecta todos los rostros y calcula embeddings."""
        faces = self._detectar_raw(img_bgr)
        if faces is None or len(faces) == 0:
            return []
        rostros = []
        for f in faces:
            # f: [x, y, w, h, lx_re, ly_re, lx_le, ly_le, lx_n, ly_n,
            #     lx_mr, ly_mr, lx_ml, ly_ml, score]
            x, y, w, h = f[0], f[1], f[2], f[3]
            score = float(f[14])
            bbox = (float(x), float(y), float(x + w), float(y + h))
            landmarks = f[4:14].copy()

            # Alinear y obtener embedding
            try:
                aligned = self._recognizer.alignCrop(img_bgr, f)
                emb = self._recognizer.feature(aligned)  # (1, 128)
                emb = emb.flatten().astype(np.float32)
                # Normalizar (norm L2)
                norm = np.linalg.norm(emb)
                if norm > 0:
                    emb = emb / norm
            except Exception as e:
                log.warning("No se pudo alinear/embedding: %s", e)
                continue

            rostros.append(Rostro(bbox, score, landmarks, emb, aligned))
        return rostros

    def detectar_uno(self, img_bgr: np.ndarray) -> Optional[Rostro]:
        rostros = self.detectar(img_bgr)
        if not rostros:
            return None
        # El más grande
        def area(r):
            x1, y1, x2, y2 = r.bbox
            return (x2 - x1) * (y2 - y1)
        return max(rostros, key=area)

    # ------------------------------------------------------------------
    @staticmethod
    def comparar(emb_a: np.ndarray, emb_b: np.ndarray) -> float:
        """Cosine similarity (ya normalizados → producto punto)."""
        return float(np.dot(emb_a, emb_b))

    @staticmethod
    def serializar(emb: np.ndarray) -> bytes:
        return np.asarray(emb, dtype=np.float32).tobytes()

    @staticmethod
    def deserializar(data: bytes) -> np.ndarray:
        return np.frombuffer(data, dtype=np.float32)

    # ------------------------------------------------------------------
    @staticmethod
    def thumb_jpeg(img_bgr: np.ndarray, bbox, tam: int = 100) -> bytes:
        x1, y1, x2, y2 = [int(v) for v in bbox]
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
