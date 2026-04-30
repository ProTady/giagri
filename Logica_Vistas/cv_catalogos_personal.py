"""Vista unificada de catálogos de Personal: Cargos y Áreas."""
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView, QInputDialog, QMessageBox, QTableWidgetItem, QWidget,
)

from Vistas.personal.ui_catalogos_personal import Ui_CatalogosPersonal
from Vistas.recursos.estilos import QSS_LISTA
from Logica.cl_cargo import ClCargo
from Logica.cl_area_trabajo import ClAreaTrabajo
from Conexion.cn_sesion import Sesion


class CvCatalogosPersonal(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CatalogosPersonal()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_LISTA)

        self._cl_c = ClCargo()
        self._cl_a = ClAreaTrabajo()
        self._sesion = Sesion()

        self._configurar_tablas()
        self._configurar_permisos()
        self._conectar()

        self._cargar_cargos()
        self._cargar_areas()

    # ------------------------------------------------------------------
    def _configurar_tablas(self) -> None:
        for tbl in (self.ui.tblCargos, self.ui.tblAreas):
            tbl.setColumnCount(3)
            tbl.setHorizontalHeaderLabels(["Nombre", "Descripción", "Activo"])
            tbl.setAlternatingRowColors(True)
            tbl.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            tbl.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
            tbl.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            tbl.verticalHeader().setVisible(False)
            tbl.setColumnWidth(0, 220)
            tbl.setColumnWidth(1, 380)
            tbl.setColumnWidth(2, 80)

    def _configurar_permisos(self) -> None:
        s = self._sesion
        crear_c = s.puede("PERSONAL_CARGOS", "crear") or s.usuario.es_admin
        edit_c  = s.puede("PERSONAL_CARGOS", "editar") or s.usuario.es_admin
        elim_c  = s.puede("PERSONAL_CARGOS", "eliminar") or s.usuario.es_admin
        crear_a = s.puede("PERSONAL_AREAS", "crear") or s.usuario.es_admin
        edit_a  = s.puede("PERSONAL_AREAS", "editar") or s.usuario.es_admin
        elim_a  = s.puede("PERSONAL_AREAS", "eliminar") or s.usuario.es_admin

        self.ui.btnCargoAgregar.setEnabled(crear_c)
        self.ui.btnCargoEditar.setEnabled(edit_c)
        self.ui.btnCargoEliminar.setEnabled(elim_c)
        self.ui.btnAreaAgregar.setEnabled(crear_a)
        self.ui.btnAreaEditar.setEnabled(edit_a)
        self.ui.btnAreaEliminar.setEnabled(elim_a)

    def _conectar(self) -> None:
        self.ui.btnCargoAgregar.clicked.connect(self._cargo_agregar)
        self.ui.btnCargoEditar.clicked.connect(self._cargo_editar)
        self.ui.btnCargoEliminar.clicked.connect(self._cargo_eliminar)
        self.ui.tblCargos.itemDoubleClicked.connect(lambda _: self._cargo_editar())

        self.ui.btnAreaAgregar.clicked.connect(self._area_agregar)
        self.ui.btnAreaEditar.clicked.connect(self._area_editar)
        self.ui.btnAreaEliminar.clicked.connect(self._area_eliminar)
        self.ui.tblAreas.itemDoubleClicked.connect(lambda _: self._area_editar())

    # ==================================================================
    # CARGOS
    # ==================================================================
    def _cargar_cargos(self) -> None:
        cargos = self._cl_c.listar(self._sesion.usuario.id_fundo,
                                    solo_activos=False)
        t = self.ui.tblCargos
        t.setRowCount(0)
        for c in cargos:
            fila = t.rowCount()
            t.insertRow(fila)
            it_n = QTableWidgetItem(c.nombre)
            it_n.setData(Qt.ItemDataRole.UserRole, c.id_cargo)
            t.setItem(fila, 0, it_n)
            t.setItem(fila, 1, QTableWidgetItem(c.descripcion))
            t.setItem(fila, 2, QTableWidgetItem("Sí" if c.activo else "No"))

    def _cargo_id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblCargos.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblCargos.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _cargo_agregar(self) -> None:
        nombre = self.ui.txtCargoNombre.text().strip()
        desc = self.ui.txtCargoDesc.text().strip()
        if not nombre:
            QMessageBox.information(self, "Cargo", "Ingresa un nombre.")
            return
        try:
            self._cl_c.crear(self._sesion.usuario.id_fundo, nombre, desc)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self.ui.txtCargoNombre.clear()
        self.ui.txtCargoDesc.clear()
        self._cargar_cargos()

    def _cargo_editar(self) -> None:
        id_c = self._cargo_id_seleccionado()
        if id_c is None:
            return
        cargos = self._cl_c.listar(self._sesion.usuario.id_fundo,
                                    solo_activos=False)
        actual = next((c for c in cargos if c.id_cargo == id_c), None)
        if not actual:
            return
        nombre, ok = QInputDialog.getText(self, "Editar Cargo",
                                          "Nombre:", text=actual.nombre)
        if not ok:
            return
        desc, ok = QInputDialog.getText(self, "Editar Cargo",
                                        "Descripción:", text=actual.descripcion)
        if not ok:
            return
        try:
            self._cl_c.actualizar(id_c, self._sesion.usuario.id_fundo,
                                  nombre, desc, actual.activo)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_cargos()

    def _cargo_eliminar(self) -> None:
        id_c = self._cargo_id_seleccionado()
        if id_c is None:
            return
        r = QMessageBox.question(
            self, "Eliminar cargo", "¿Eliminar este cargo?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl_c.eliminar(id_c)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_cargos()

    # ==================================================================
    # ÁREAS
    # ==================================================================
    def _cargar_areas(self) -> None:
        areas = self._cl_a.listar(self._sesion.usuario.id_fundo,
                                   solo_activos=False)
        t = self.ui.tblAreas
        t.setRowCount(0)
        for a in areas:
            fila = t.rowCount()
            t.insertRow(fila)
            it_n = QTableWidgetItem(a.nombre)
            it_n.setData(Qt.ItemDataRole.UserRole, a.id_area)
            t.setItem(fila, 0, it_n)
            t.setItem(fila, 1, QTableWidgetItem(a.descripcion))
            t.setItem(fila, 2, QTableWidgetItem("Sí" if a.activo else "No"))

    def _area_id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblAreas.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblAreas.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _area_agregar(self) -> None:
        nombre = self.ui.txtAreaNombre.text().strip()
        desc = self.ui.txtAreaDesc.text().strip()
        if not nombre:
            QMessageBox.information(self, "Área", "Ingresa un nombre.")
            return
        try:
            self._cl_a.crear(self._sesion.usuario.id_fundo, nombre, desc)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self.ui.txtAreaNombre.clear()
        self.ui.txtAreaDesc.clear()
        self._cargar_areas()

    def _area_editar(self) -> None:
        id_a = self._area_id_seleccionado()
        if id_a is None:
            return
        areas = self._cl_a.listar(self._sesion.usuario.id_fundo,
                                   solo_activos=False)
        actual = next((a for a in areas if a.id_area == id_a), None)
        if not actual:
            return
        nombre, ok = QInputDialog.getText(self, "Editar Área",
                                          "Nombre:", text=actual.nombre)
        if not ok:
            return
        desc, ok = QInputDialog.getText(self, "Editar Área",
                                        "Descripción:", text=actual.descripcion)
        if not ok:
            return
        try:
            self._cl_a.actualizar(id_a, self._sesion.usuario.id_fundo,
                                  nombre, desc, actual.activo)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_areas()

    def _area_eliminar(self) -> None:
        id_a = self._area_id_seleccionado()
        if id_a is None:
            return
        r = QMessageBox.question(
            self, "Eliminar área", "¿Eliminar esta área?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl_a.eliminar(id_a)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_areas()
