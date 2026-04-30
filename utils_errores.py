"""
Manejo global de errores y logging.
Captura cualquier excepción no manejada y la muestra en consola + diálogo.
"""
from __future__ import annotations

import faulthandler
import logging
import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Type

from PySide6.QtCore import qInstallMessageHandler, QtMsgType
from PySide6.QtWidgets import QApplication, QMessageBox


_RAIZ = Path(__file__).resolve().parent
_CARPETA_LOGS = _RAIZ / "logs"
_CARPETA_LOGS.mkdir(exist_ok=True)


def _activar_faulthandler() -> None:
    """Captura segfaults y otros crashes de C/Qt con stack trace."""
    archivo_crash = _CARPETA_LOGS / f"crash_{datetime.now():%Y%m%d}.log"
    f = open(archivo_crash, "a", encoding="utf-8")
    f.write(f"\n=== {datetime.now()} ===\n")
    f.flush()
    faulthandler.enable(file=f, all_threads=True)


class _FlushFileHandler(logging.FileHandler):
    """FileHandler que hace flush en cada emit (para no perder logs en crash)."""
    def emit(self, record):
        super().emit(record)
        self.flush()


def configurar_logging() -> None:
    """Configura logging a archivo + consola."""
    archivo = _CARPETA_LOGS / f"giagri_{datetime.now():%Y%m%d}.log"

    formato = "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=formato,
        handlers=[
            _FlushFileHandler(archivo, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    logging.info("=" * 60)
    logging.info("Inicio de sesión GIAGRI")


def manejador_excepciones(tipo: Type[BaseException], valor: BaseException,
                          tb) -> None:
    """Captura cualquier excepción no manejada."""
    if issubclass(tipo, KeyboardInterrupt):
        sys.__excepthook__(tipo, valor, tb)
        return

    texto = "".join(traceback.format_exception(tipo, valor, tb))

    # Siempre imprimir en consola
    print("\n" + "=" * 70, file=sys.stderr)
    print("ERROR NO MANEJADO:", file=sys.stderr)
    print("=" * 70, file=sys.stderr)
    print(texto, file=sys.stderr)
    print("=" * 70 + "\n", file=sys.stderr)

    logging.error("Excepción no manejada:\n%s", texto)

    # Mostrar diálogo si la app Qt está corriendo
    if QApplication.instance() is not None:
        try:
            box = QMessageBox()
            box.setIcon(QMessageBox.Icon.Critical)
            box.setWindowTitle("Error inesperado")
            box.setText(f"<b>{tipo.__name__}:</b> {valor}")
            box.setDetailedText(texto)
            box.setStandardButtons(QMessageBox.StandardButton.Ok)
            box.exec()
        except Exception:
            pass


def _qt_message_handler(modo: QtMsgType, _ctx, mensaje: str) -> None:
    """Redirige mensajes internos de Qt al log."""
    nivel = {
        QtMsgType.QtDebugMsg:    logging.DEBUG,
        QtMsgType.QtInfoMsg:     logging.INFO,
        QtMsgType.QtWarningMsg:  logging.WARNING,
        QtMsgType.QtCriticalMsg: logging.ERROR,
        QtMsgType.QtFatalMsg:    logging.CRITICAL,
    }.get(modo, logging.INFO)
    logging.log(nivel, "[Qt] %s", mensaje)


def instalar_manejadores() -> None:
    """Instala todos los hooks. Llamar UNA vez al inicio."""
    _activar_faulthandler()
    configurar_logging()
    sys.excepthook = manejador_excepciones
    qInstallMessageHandler(_qt_message_handler)
