"""
GIAGRI - Punto de entrada de la aplicación.
"""
from __future__ import annotations

import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox

from utils_errores import instalar_manejadores
from version import __app_name__, __version__
from Conexion.cn_postgres import probar_conexion
from Conexion.cn_sesion import Sesion
from Vistas.recursos.estilos import RUTA_ICONO


def main() -> int:
    instalar_manejadores()

    app = QApplication(sys.argv)
    app.setApplicationName(__app_name__)
    app.setApplicationVersion(__version__)
    app.setOrganizationName("GIAGRI")
    if RUTA_ICONO.exists():
        app.setWindowIcon(QIcon(str(RUTA_ICONO)))

    if not probar_conexion():
        QMessageBox.critical(
            None, "Error de conexión",
            "No se pudo conectar a la base de datos.\n\n"
            "Revisa el archivo .env y que PostgreSQL esté corriendo.",
        )
        return 1

    # Bucle login -> principal -> login (permite cerrar sesión y volver a entrar)
    while True:
        from Logica_Vistas.cv_login import CvLogin
        login = CvLogin()
        if login.exec() != QDialog.DialogCode.Accepted:
            return 0

        if Sesion().usuario is None:
            return 0

        from Logica_Vistas.cv_principal import CvPrincipal
        ventana = CvPrincipal()
        ventana.show()
        app.exec()

        # Si el usuario cerró sesión, volvemos al login.
        if Sesion().activa:
            return 0  # Cierre normal de ventana sin logout


if __name__ == "__main__":
    sys.exit(main())
