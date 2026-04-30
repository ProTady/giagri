"""
Diálogo crear/editar usuario.
"""
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QListWidgetItem

from Vistas.usuarios.ui_usuario_form import Ui_UsuarioForm
from Vistas.recursos.estilos import QSS_FORM, RUTA_ICONO
from Logica.cl_usuario import ClUsuario
from Logica.cl_rol import ClRol


class CvUsuarioForm(QDialog):
    """Si id_usuario es None, modo crear. Si trae valor, modo editar."""

    def __init__(self, id_fundo: int, id_usuario: Optional[int] = None,
                 parent=None):
        super().__init__(parent)
        self.ui = Ui_UsuarioForm()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_FORM)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))

        self._id_fundo = id_fundo
        self._id_usuario = id_usuario
        self._cl_usuario = ClUsuario()
        self._cl_rol = ClRol()
        self._roles_disponibles: list = []

        self._cargar_roles()
        self._configurar_modo()

        self.ui.btnGuardar.clicked.connect(self._guardar)
        self.ui.btnCancelar.clicked.connect(self.reject)

    # ------------------------------------------------------------------
    def _cargar_roles(self) -> None:
        self._roles_disponibles = self._cl_rol.listar(self._id_fundo)
        self.ui.lstRoles.clear()
        for r in self._roles_disponibles:
            item = QListWidgetItem(r.nombre)
            item.setData(Qt.ItemDataRole.UserRole, r.id_rol)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.lstRoles.addItem(item)
        if not self._roles_disponibles:
            placeholder = QListWidgetItem(
                "(Aún no hay roles. Créalos en 'Roles y Permisos'.)"
            )
            placeholder.setFlags(Qt.ItemFlag.NoItemFlags)
            self.ui.lstRoles.addItem(placeholder)

    def _configurar_modo(self) -> None:
        if self._id_usuario is None:
            self.ui.lblTitulo.setText("Nuevo Usuario")
            self.setWindowTitle("Nuevo Usuario")
            return

        # Modo edición: cargar datos
        self.ui.lblTitulo.setText("Editar Usuario")
        self.setWindowTitle("Editar Usuario")
        u = self._cl_usuario.obtener(self._id_usuario)
        if u is None:
            return
        self.ui.txtUsername.setText(u["username"])
        self.ui.txtUsername.setReadOnly(True)
        self.ui.txtNombre.setText(u["nombre_completo"])
        self.ui.txtCorreo.setText(u["correo"] or "")
        self.ui.chkAdmin.setChecked(u["es_admin"])
        self.ui.chkActivo.setChecked(u["activo"])
        # Ocultar contraseñas en edición (se cambian con botón aparte)
        self.ui.txtClave.setVisible(False)
        self.ui.txtClave2.setVisible(False)
        self.ui.l4.setVisible(False)
        self.ui.l5.setVisible(False)

        # Marcar roles asignados
        ids_roles = self._cl_usuario.roles_de_usuario(self._id_usuario)
        for i in range(self.ui.lstRoles.count()):
            item = self.ui.lstRoles.item(i)
            if item.data(Qt.ItemDataRole.UserRole) in ids_roles:
                item.setCheckState(Qt.CheckState.Checked)

    # ------------------------------------------------------------------
    def _ids_roles_seleccionados(self) -> list[int]:
        ids = []
        for i in range(self.ui.lstRoles.count()):
            item = self.ui.lstRoles.item(i)
            if item.checkState() == Qt.CheckState.Checked:
                ids.append(item.data(Qt.ItemDataRole.UserRole))
        return ids

    def _guardar(self) -> None:
        self.ui.lblError.setText("")
        username = self.ui.txtUsername.text().strip()
        nombre = self.ui.txtNombre.text().strip()
        correo = self.ui.txtCorreo.text().strip()
        es_admin = self.ui.chkAdmin.isChecked()
        activo = self.ui.chkActivo.isChecked()
        ids_roles = self._ids_roles_seleccionados()

        if not username or not nombre:
            self.ui.lblError.setText("Usuario y nombre son obligatorios.")
            return

        try:
            if self._id_usuario is None:
                clave = self.ui.txtClave.text()
                clave2 = self.ui.txtClave2.text()
                if clave != clave2:
                    self.ui.lblError.setText("Las contraseñas no coinciden.")
                    return
                self._cl_usuario.crear(
                    id_fundo=self._id_fundo,
                    username=username, clave=clave,
                    nombre_completo=nombre, correo=correo,
                    es_admin=es_admin, activo=activo,
                    ids_roles=ids_roles,
                )
            else:
                self._cl_usuario.actualizar(
                    id_usuario=self._id_usuario,
                    nombre_completo=nombre, correo=correo,
                    es_admin=es_admin, activo=activo,
                    ids_roles=ids_roles,
                )
        except ValueError as e:
            self.ui.lblError.setText(str(e))
            return
        except Exception as e:
            self.ui.lblError.setText(f"Error: {e}")
            return

        self.accept()
