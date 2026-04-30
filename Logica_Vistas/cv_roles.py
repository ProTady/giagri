"""
Vista de Roles y Permisos.
Lista de roles a la izquierda; matriz de permisos a la derecha.
"""
from __future__ import annotations

import logging
from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QInputDialog, QListWidgetItem, QMessageBox, QTreeWidgetItem, QWidget,
)

from Vistas.usuarios.ui_roles import Ui_RolesPermisos
from Vistas.recursos.estilos import QSS_LISTA
from Logica.cl_rol import ClRol, Rol
from Logica.cl_permisos import ClPermisos, Modulo
from Conexion.cn_sesion import Sesion

log = logging.getLogger(__name__)

ACCIONES = ["ver", "crear", "editar", "eliminar"]
COL_VER, COL_CREAR, COL_EDITAR, COL_ELIMINAR = 1, 2, 3, 4
ID_MODULO_ROLE = Qt.ItemDataRole.UserRole + 1


class CvRoles(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        log.info("CvRoles.__init__ inicio")
        self.ui = Ui_RolesPermisos()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_LISTA)

        self._cl_rol = ClRol()
        self._cl_permisos = ClPermisos()
        self._sesion = Sesion()

        self._id_rol_actual: Optional[int] = None
        self._cargando = False

        self._configurar_tree()
        self._configurar_permisos_botones()

        self.ui.btnNuevoRol.clicked.connect(self._nuevo_rol)
        self.ui.btnRenombrar.clicked.connect(self._renombrar_rol)
        self.ui.btnEliminarRol.clicked.connect(self._eliminar_rol)
        self.ui.btnGuardarPerm.clicked.connect(self._guardar_permisos)
        self.ui.lstRoles.currentItemChanged.connect(self._on_rol_cambiado)
        self.ui.treePermisos.itemChanged.connect(self._on_check_cambiado)

        self._cargar_roles()
        log.info("CvRoles.__init__ fin")

    # ------------------------------------------------------------------
    def _configurar_tree(self) -> None:
        from PySide6.QtWidgets import QHeaderView
        t = self.ui.treePermisos
        t.setColumnWidth(0, 320)
        for c in (COL_VER, COL_CREAR, COL_EDITAR, COL_ELIMINAR):
            t.setColumnWidth(c, 80)
        h = t.header()
        h.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

    def _configurar_permisos_botones(self) -> None:
        s = self._sesion
        crear = s.puede("ADMIN_ROLES", "crear")
        editar = s.puede("ADMIN_ROLES", "editar")
        eliminar = s.puede("ADMIN_ROLES", "eliminar")
        self.ui.btnNuevoRol.setEnabled(crear)
        self.ui.btnRenombrar.setEnabled(editar)
        self.ui.btnEliminarRol.setEnabled(eliminar)
        self.ui.btnGuardarPerm.setEnabled(editar)

    # ------------------------------------------------------------------
    def _cargar_roles(self) -> None:
        self.ui.lstRoles.clear()
        roles = self._cl_rol.listar(self._sesion.usuario.id_fundo)
        for r in roles:
            item = QListWidgetItem(r.nombre)
            item.setData(Qt.ItemDataRole.UserRole, r.id_rol)
            self.ui.lstRoles.addItem(item)

        if self.ui.lstRoles.count() == 0:
            self._id_rol_actual = None
            self.ui.treePermisos.clear()
            self.ui.lblRolSeleccionado.setText(
                "(No hay roles. Crea uno con '+ Nuevo'.)"
            )
        else:
            self.ui.lstRoles.setCurrentRow(0)

    def _on_rol_cambiado(self, actual: QListWidgetItem,
                         _ant: QListWidgetItem) -> None:
        if actual is None:
            self._id_rol_actual = None
            self.ui.treePermisos.clear()
            return
        self._id_rol_actual = actual.data(Qt.ItemDataRole.UserRole)
        self.ui.lblRolSeleccionado.setText(
            f"Rol: <b>{actual.text()}</b>"
        )
        self._cargar_arbol_permisos()

    # ------------------------------------------------------------------
    def _cargar_arbol_permisos(self) -> None:
        if self._id_rol_actual is None:
            return
        self._cargando = True
        try:
            self.ui.treePermisos.clear()
            arbol = self._cl_permisos.arbol_modulos_completo()
            permisos = self._cl_permisos.permisos_de_rol(self._id_rol_actual)
            for raiz in arbol:
                self.ui.treePermisos.addTopLevelItem(
                    self._crear_item_arbol(raiz, permisos)
                )
            self.ui.treePermisos.expandAll()
        finally:
            self._cargando = False

    def _crear_item_arbol(self, modulo: Modulo,
                          permisos: dict) -> QTreeWidgetItem:
        item = QTreeWidgetItem([modulo.nombre, "", "", "", ""])
        item.setData(0, ID_MODULO_ROLE, modulo.id_modulo)
        p = permisos.get(modulo.id_modulo, {})
        for col, accion in zip(
            (COL_VER, COL_CREAR, COL_EDITAR, COL_ELIMINAR), ACCIONES
        ):
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(col, self._bool_a_check(p.get(accion, False)))
            item.setTextAlignment(col, Qt.AlignmentFlag.AlignCenter)
        for hijo in modulo.hijos:
            item.addChild(self._crear_item_arbol(hijo, permisos))
        return item

    @staticmethod
    def _bool_a_check(v: bool) -> Qt.CheckState:
        return Qt.CheckState.Checked if v else Qt.CheckState.Unchecked

    @staticmethod
    def _check_a_bool(s: Qt.CheckState) -> bool:
        return s == Qt.CheckState.Checked

    # ------------------------------------------------------------------
    def _on_check_cambiado(self, item: QTreeWidgetItem, col: int) -> None:
        """Si marcas 'Ver' en un padre, marca 'Ver' en todos los hijos."""
        if self._cargando:
            return
        if col not in (COL_VER, COL_CREAR, COL_EDITAR, COL_ELIMINAR):
            return
        if item.childCount() == 0:
            return
        self._cargando = True
        try:
            estado = item.checkState(col)
            self._propagar_a_hijos(item, col, estado)
        finally:
            self._cargando = False

    def _propagar_a_hijos(self, padre: QTreeWidgetItem, col: int,
                          estado: Qt.CheckState) -> None:
        for i in range(padre.childCount()):
            hijo = padre.child(i)
            hijo.setCheckState(col, estado)
            self._propagar_a_hijos(hijo, col, estado)

    # ------------------------------------------------------------------
    def _recolectar_permisos(self) -> dict[int, dict[str, bool]]:
        permisos: dict[int, dict[str, bool]] = {}

        def recorrer(item: QTreeWidgetItem) -> None:
            id_m = item.data(0, ID_MODULO_ROLE)
            permisos[id_m] = {
                "ver":      self._check_a_bool(item.checkState(COL_VER)),
                "crear":    self._check_a_bool(item.checkState(COL_CREAR)),
                "editar":   self._check_a_bool(item.checkState(COL_EDITAR)),
                "eliminar": self._check_a_bool(item.checkState(COL_ELIMINAR)),
            }
            for i in range(item.childCount()):
                recorrer(item.child(i))

        for i in range(self.ui.treePermisos.topLevelItemCount()):
            recorrer(self.ui.treePermisos.topLevelItem(i))
        return permisos

    # ------------------------------------------------------------------
    def _nuevo_rol(self) -> None:
        nombre, ok = QInputDialog.getText(
            self, "Nuevo Rol", "Nombre del nuevo rol:"
        )
        if not ok or not nombre.strip():
            return
        try:
            id_nuevo = self._cl_rol.crear(
                self._sesion.usuario.id_fundo, nombre.strip()
            )
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_roles()
        # Seleccionar el recién creado
        for i in range(self.ui.lstRoles.count()):
            if self.ui.lstRoles.item(i).data(Qt.ItemDataRole.UserRole) == id_nuevo:
                self.ui.lstRoles.setCurrentRow(i)
                break

    def _renombrar_rol(self) -> None:
        if self._id_rol_actual is None:
            return
        item = self.ui.lstRoles.currentItem()
        nuevo, ok = QInputDialog.getText(
            self, "Renombrar Rol", "Nuevo nombre:", text=item.text()
        )
        if not ok or not nuevo.strip():
            return
        try:
            self._cl_rol.renombrar(
                self._id_rol_actual, self._sesion.usuario.id_fundo,
                nuevo.strip()
            )
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        item.setText(nuevo.strip())
        self.ui.lblRolSeleccionado.setText(f"Rol: <b>{nuevo.strip()}</b>")

    def _eliminar_rol(self) -> None:
        if self._id_rol_actual is None:
            return
        item = self.ui.lstRoles.currentItem()
        r = QMessageBox.question(
            self, "Eliminar rol",
            f"¿Eliminar el rol '{item.text()}'?\n\nSe perderán sus permisos.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl_rol.eliminar(self._id_rol_actual)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_roles()

    def _guardar_permisos(self) -> None:
        if self._id_rol_actual is None:
            QMessageBox.information(self, "Guardar",
                                    "Selecciona un rol primero.")
            return
        permisos = self._recolectar_permisos()
        try:
            self._cl_permisos.guardar_permisos_rol(self._id_rol_actual, permisos)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        QMessageBox.information(
            self, "Guardado",
            "Permisos guardados.\n\nLos usuarios con este rol verán los cambios "
            "la próxima vez que inicien sesión."
        )
