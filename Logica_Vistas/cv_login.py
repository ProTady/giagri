"""
Controlador de la ventana de Login.
Conecta v_login.ui con cl_usuario y cl_permisos.
"""
from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QDialog

from Vistas.login.ui_login import Ui_DialogLogin
from Vistas.recursos.estilos import QSS_LOGIN, RUTA_ICONO, RUTA_LOGO_PNG
from Logica.cl_usuario import ClUsuario
from Logica.cl_permisos import ClPermisos
from Conexion.cn_sesion import Sesion, Usuario


class CvLogin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_DialogLogin()
        self.ui.setupUi(self)

        # Quitar botón "?" de la barra de título
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # Aplicar estilo
        self.setStyleSheet(QSS_LOGIN)

        # Icono y logo
        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))
        if RUTA_LOGO_PNG.exists():
            pix = QPixmap(str(RUTA_LOGO_PNG))
            self.ui.lblLogo.setPixmap(
                pix.scaledToHeight(140, Qt.SmoothTransformation)
            )

        self._cl_usuario = ClUsuario()
        self._cl_permisos = ClPermisos()

        self.ui.btnIngresar.clicked.connect(self._intentar_login)
        self.ui.btnCancelar.clicked.connect(self.reject)

    def _intentar_login(self) -> None:
        username = self.ui.txtUsuario.text().strip()
        clave = self.ui.txtClave.text()

        self.ui.lblError.setText("")

        if not username or not clave:
            self.ui.lblError.setText("Ingrese usuario y contraseña.")
            return

        self.ui.btnIngresar.setEnabled(False)
        try:
            usuario = self._cl_usuario.autenticar(username, clave)
        except Exception as e:
            self.ui.lblError.setText(f"Error: {e}")
            self.ui.btnIngresar.setEnabled(True)
            return
        finally:
            self.ui.btnIngresar.setEnabled(True)

        if usuario is None:
            self.ui.lblError.setText("Usuario o contraseña incorrectos.")
            self.ui.txtClave.clear()
            self.ui.txtClave.setFocus()
            return

        permisos = self._cl_permisos.permisos_por_usuario(
            usuario.id_usuario, usuario.es_admin
        )

        Sesion().iniciar(
            usuario=Usuario(
                id_usuario=usuario.id_usuario,
                username=usuario.username,
                nombre_completo=usuario.nombre_completo,
                id_fundo=usuario.id_fundo,
                es_admin=usuario.es_admin,
            ),
            nombre_fundo=usuario.nombre_fundo,
            permisos=permisos,
        )
        self.accept()
