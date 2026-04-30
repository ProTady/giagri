"""
Vista de listado de usuarios. Embebida en el QStackedWidget de la principal.
"""
from __future__ import annotations

import logging
from datetime import datetime
from typing import Optional

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QInputDialog, QMessageBox, QTableWidgetItem, QWidget,
)

from Vistas.usuarios.ui_usuarios_lista import Ui_UsuariosLista
from Vistas.recursos.estilos import (
    QSS_LISTA, COLOR_PRIMARIO, COLOR_SECUNDARIO, COLOR_ERROR,
)
from Logica.cl_usuario import ClUsuario, UsuarioFila
from Conexion.cn_sesion import Sesion

log = logging.getLogger(__name__)

CABECERAS = ["Usuario", "Nombre completo", "Correo", "Roles",
             "Admin", "Estado", "Último acceso"]


class CvUsuariosLista(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        log.info("CvUsuariosLista.__init__ inicio")
        self.ui = Ui_UsuariosLista()
        self.ui.setupUi(self)
        log.info("setupUi OK")

        self.setStyleSheet(QSS_LISTA)
        log.info("stylesheet aplicado")

        self._cl_usuario = ClUsuario()
        self._sesion = Sesion()

        self._configurar_tabla()
        log.info("tabla configurada")
        self._configurar_permisos_botones()

        self.ui.btnNuevo.clicked.connect(self._nuevo)
        self.ui.btnEditar.clicked.connect(self._editar)
        self.ui.btnResetClave.clicked.connect(self._resetear_clave)
        self.ui.btnActivar.clicked.connect(self._alternar_activo)
        self.ui.txtBuscar.textChanged.connect(lambda _: self._cargar())
        self.ui.cboEstado.currentIndexChanged.connect(lambda _: self._cargar())
        self.ui.tblUsuarios.itemDoubleClicked.connect(lambda _: self._editar())

        # Diferir la carga inicial para que el widget se monte completo
        QTimer.singleShot(0, self._cargar)
        log.info("CvUsuariosLista.__init__ fin (carga diferida)")

    # ------------------------------------------------------------------
    def _configurar_tabla(self) -> None:
        from PySide6.QtWidgets import QAbstractItemView
        t = self.ui.tblUsuarios
        t.setColumnCount(len(CABECERAS))
        t.setHorizontalHeaderLabels(CABECERAS)
        t.setAlternatingRowColors(True)
        t.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        t.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        t.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        t.verticalHeader().setVisible(False)
        t.setColumnWidth(0, 130)
        t.setColumnWidth(1, 220)
        t.setColumnWidth(2, 200)
        t.setColumnWidth(3, 180)
        t.setColumnWidth(4, 70)
        t.setColumnWidth(5, 90)
        t.setColumnWidth(6, 150)

    def _configurar_permisos_botones(self) -> None:
        s = self._sesion
        self.ui.btnNuevo.setVisible(s.puede("ADMIN_USUARIOS", "crear"))
        self.ui.btnEditar.setVisible(s.puede("ADMIN_USUARIOS", "editar"))
        self.ui.btnResetClave.setVisible(s.puede("ADMIN_USUARIOS", "editar"))
        self.ui.btnActivar.setVisible(s.puede("ADMIN_USUARIOS", "editar"))

    # ------------------------------------------------------------------
    def _cargar(self) -> None:
        log.info("_cargar inicio")
        filtro = self.ui.txtBuscar.text().strip()
        estado_idx = self.ui.cboEstado.currentIndex()
        estado = ["todos", "activos", "inactivos"][estado_idx]

        try:
            filas = self._cl_usuario.listar(
                self._sesion.usuario.id_fundo, filtro, estado
            )
        except Exception as e:
            log.exception("Error en listar()")
            QMessageBox.critical(self, "Error",
                                 f"No se pudieron cargar los usuarios:\n{e}")
            return

        log.info("listar() devolvió %d filas", len(filas))
        t = self.ui.tblUsuarios
        t.setRowCount(0)
        for f in filas:
            self._agregar_fila(f)
        self.ui.lblTotal.setText(f"{len(filas)} usuarios")
        log.info("_cargar fin")

    def _agregar_fila(self, u: UsuarioFila) -> None:
        t = self.ui.tblUsuarios
        fila = t.rowCount()
        t.insertRow(fila)

        items = [
            u.username, u.nombre_completo, u.correo, u.roles,
            "Sí" if u.es_admin else "—",
            "Activo" if u.activo else "Inactivo",
            self._fmt_fecha(u.ultimo_acceso),
        ]
        for col, txt in enumerate(items):
            it = QTableWidgetItem(txt)
            it.setData(Qt.ItemDataRole.UserRole, u.id_usuario)
            if col == 5:
                it.setForeground(
                    QColor(COLOR_SECUNDARIO) if u.activo else QColor(COLOR_ERROR)
                )
            t.setItem(fila, col, it)

    @staticmethod
    def _fmt_fecha(f: Optional[datetime]) -> str:
        return f.strftime("%Y-%m-%d %H:%M") if f else "Nunca"

    def _id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblUsuarios.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblUsuarios.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    # ------------------------------------------------------------------
    def _nuevo(self) -> None:
        from Logica_Vistas.cv_usuario_form import CvUsuarioForm
        dlg = CvUsuarioForm(self._sesion.usuario.id_fundo, None, self)
        if dlg.exec() == dlg.DialogCode.Accepted:
            self._cargar()

    def _editar(self) -> None:
        id_u = self._id_seleccionado()
        if id_u is None:
            QMessageBox.information(self, "Editar",
                                    "Selecciona un usuario primero.")
            return
        from Logica_Vistas.cv_usuario_form import CvUsuarioForm
        dlg = CvUsuarioForm(self._sesion.usuario.id_fundo, id_u, self)
        if dlg.exec() == dlg.DialogCode.Accepted:
            self._cargar()

    def _resetear_clave(self) -> None:
        id_u = self._id_seleccionado()
        if id_u is None:
            QMessageBox.information(self, "Resetear",
                                    "Selecciona un usuario primero.")
            return
        nueva, ok = QInputDialog.getText(
            self, "Resetear contraseña",
            "Nueva contraseña (mínimo 6 caracteres):",
        )
        if not ok or not nueva:
            return
        try:
            self._cl_usuario.cambiar_clave(id_u, nueva)
            QMessageBox.information(self, "OK", "Contraseña actualizada.")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def _alternar_activo(self) -> None:
        id_u = self._id_seleccionado()
        if id_u is None:
            QMessageBox.information(self, "Activar/Desactivar",
                                    "Selecciona un usuario primero.")
            return
        try:
            nuevo = self._cl_usuario.alternar_activo(
                id_u, self._sesion.usuario.id_usuario
            )
            estado = "activado" if nuevo else "desactivado"
            QMessageBox.information(self, "OK", f"Usuario {estado}.")
            self._cargar()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
