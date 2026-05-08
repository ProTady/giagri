"""Vista unificada de catálogos de Tareo: Actividades y Labores."""
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView, QInputDialog, QMessageBox, QTableWidgetItem, QWidget,
)

from Vistas.personal.ui_catalogos_tareo import Ui_CatalogosTareo
from Vistas.recursos.estilos import QSS_LISTA, COLOR_SECUNDARIO
from Logica.cl_actividad import ClActividad
from Logica.cl_labor import ClLabor
from Conexion.cn_sesion import Sesion


class CvCatalogosTareo(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CatalogosTareo()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_LISTA)

        self._cl_a = ClActividad()
        self._cl_l = ClLabor()
        self._sesion = Sesion()

        self._configurar_tablas()
        self._configurar_permisos()
        self._conectar()
        self._cargar_todo()

    # ------------------------------------------------------------------
    def _configurar_tablas(self) -> None:
        ta = self.ui.tblActividades
        ta.setColumnCount(3)
        ta.setHorizontalHeaderLabels(["Nombre", "Descripción", "Activo"])
        for tbl, anchos in [
            (ta, [220, 380, 80]),
            (self.ui.tblLabores, [150, 220, 110, 280, 80]),
        ]:
            tbl.setAlternatingRowColors(True)
            tbl.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            tbl.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
            tbl.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            tbl.verticalHeader().setVisible(False)
            for col, w in enumerate(anchos):
                tbl.setColumnWidth(col, w)
        self.ui.tblLabores.setColumnCount(5)
        self.ui.tblLabores.setHorizontalHeaderLabels(
            ["Actividad", "Labor", "Bono S/. /h", "Descripción", "Activo"]
        )

    def _configurar_permisos(self) -> None:
        s = self._sesion
        crear_a = s.puede("PERSONAL_ACTIVIDADES", "crear") or s.usuario.es_admin
        edit_a  = s.puede("PERSONAL_ACTIVIDADES", "editar") or s.usuario.es_admin
        elim_a  = s.puede("PERSONAL_ACTIVIDADES", "eliminar") or s.usuario.es_admin
        crear_l = s.puede("PERSONAL_LABORES", "crear") or s.usuario.es_admin
        edit_l  = s.puede("PERSONAL_LABORES", "editar") or s.usuario.es_admin
        elim_l  = s.puede("PERSONAL_LABORES", "eliminar") or s.usuario.es_admin

        for btn, ok in [
            (self.ui.btnActAgregar, crear_a),
            (self.ui.btnActEditar, edit_a),
            (self.ui.btnActEliminar, elim_a),
            (self.ui.btnLabAgregar, crear_l),
            (self.ui.btnLabEditar, edit_l),
            (self.ui.btnLabEliminar, elim_l),
        ]:
            btn.setEnabled(ok)

    def _conectar(self) -> None:
        self.ui.btnActAgregar.clicked.connect(self._act_agregar)
        self.ui.btnActEditar.clicked.connect(self._act_editar)
        self.ui.btnActEliminar.clicked.connect(self._act_eliminar)
        self.ui.tblActividades.itemDoubleClicked.connect(lambda _: self._act_editar())

        self.ui.btnLabAgregar.clicked.connect(self._lab_agregar)
        self.ui.btnLabEditar.clicked.connect(self._lab_editar)
        self.ui.btnLabEliminar.clicked.connect(self._lab_eliminar)
        self.ui.tblLabores.itemDoubleClicked.connect(lambda _: self._lab_editar())
        self.ui.cboLabFiltro.currentIndexChanged.connect(
            lambda _: self._cargar_labores()
        )

    # ==================================================================
    def _cargar_todo(self) -> None:
        self._cargar_actividades()
        self._refrescar_combos_actividad()
        self._cargar_labores()

    def _refrescar_combos_actividad(self) -> None:
        actividades = self._cl_a.listar(self._sesion.usuario.id_fundo)
        for cbo, con_todos in [
            (self.ui.cboLabActividad, False),
            (self.ui.cboLabFiltro, True),
        ]:
            cbo.blockSignals(True)
            cbo.clear()
            if con_todos:
                cbo.addItem("(Todas)", None)
            for a in actividades:
                cbo.addItem(a.nombre, a.id_actividad)
            cbo.blockSignals(False)

    # ==================================================================
    # ACTIVIDADES
    # ==================================================================
    def _cargar_actividades(self) -> None:
        actividades = self._cl_a.listar(self._sesion.usuario.id_fundo,
                                         solo_activos=False)
        t = self.ui.tblActividades
        t.setRowCount(0)
        for a in actividades:
            fila = t.rowCount()
            t.insertRow(fila)
            it = QTableWidgetItem(a.nombre)
            it.setData(Qt.ItemDataRole.UserRole, a.id_actividad)
            t.setItem(fila, 0, it)
            t.setItem(fila, 1, QTableWidgetItem(a.descripcion))
            t.setItem(fila, 2, QTableWidgetItem("Sí" if a.activo else "No"))

    def _act_id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblActividades.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblActividades.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _act_agregar(self) -> None:
        nombre = self.ui.txtActNombre.text().strip()
        desc = self.ui.txtActDesc.text().strip()
        if not nombre:
            QMessageBox.information(self, "Actividad", "Ingresa un nombre.")
            return
        try:
            self._cl_a.crear(self._sesion.usuario.id_fundo, nombre, desc)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self.ui.txtActNombre.clear()
        self.ui.txtActDesc.clear()
        self._cargar_actividades()
        self._refrescar_combos_actividad()

    def _act_editar(self) -> None:
        id_a = self._act_id_seleccionado()
        if id_a is None:
            return
        actividades = self._cl_a.listar(self._sesion.usuario.id_fundo,
                                         solo_activos=False)
        actual = next((a for a in actividades if a.id_actividad == id_a), None)
        if not actual:
            return
        nombre, ok = QInputDialog.getText(self, "Editar Actividad",
                                          "Nombre:", text=actual.nombre)
        if not ok:
            return
        desc, ok = QInputDialog.getText(self, "Editar Actividad",
                                         "Descripción:", text=actual.descripcion)
        if not ok:
            return
        try:
            self._cl_a.actualizar(id_a, self._sesion.usuario.id_fundo,
                                   nombre, desc, actual.activo)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_actividades()
        self._refrescar_combos_actividad()
        self._cargar_labores()

    def _act_eliminar(self) -> None:
        id_a = self._act_id_seleccionado()
        if id_a is None:
            return
        r = QMessageBox.question(
            self, "Eliminar actividad", "¿Eliminar esta actividad?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl_a.eliminar(id_a)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_actividades()
        self._refrescar_combos_actividad()

    # ==================================================================
    # LABORES
    # ==================================================================
    def _cargar_labores(self) -> None:
        from PySide6.QtGui import QColor
        id_filtro = self.ui.cboLabFiltro.currentData()
        labores = self._cl_l.listar(
            self._sesion.usuario.id_fundo, id_filtro, solo_activos=False
        )
        t = self.ui.tblLabores
        t.setRowCount(0)
        for l in labores:
            fila = t.rowCount()
            t.insertRow(fila)
            it_a = QTableWidgetItem(l.actividad_nombre)
            it_a.setData(Qt.ItemDataRole.UserRole, l.id_labor)
            t.setItem(fila, 0, it_a)
            t.setItem(fila, 1, QTableWidgetItem(l.nombre))
            it_b = QTableWidgetItem(f"{l.bono_por_hora:.2f}")
            it_b.setTextAlignment(Qt.AlignmentFlag.AlignRight
                                   | Qt.AlignmentFlag.AlignVCenter)
            if l.bono_por_hora > 0:
                it_b.setForeground(QColor(COLOR_SECUNDARIO))
                f = it_b.font(); f.setBold(True); it_b.setFont(f)
            t.setItem(fila, 2, it_b)
            t.setItem(fila, 3, QTableWidgetItem(l.descripcion))
            t.setItem(fila, 4, QTableWidgetItem("Sí" if l.activo else "No"))

    def _lab_id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblLabores.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblLabores.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _lab_agregar(self) -> None:
        id_act = self.ui.cboLabActividad.currentData()
        nombre = self.ui.txtLabNombre.text().strip()
        bono = float(self.ui.spLabBono.value())
        if not nombre:
            QMessageBox.information(self, "Labor", "Ingresa un nombre.")
            return
        try:
            self._cl_l.crear(
                self._sesion.usuario.id_fundo,
                id_act, nombre, codigo="",
                descripcion="", bono_por_hora=bono,
            )
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self.ui.txtLabNombre.clear()
        self.ui.spLabBono.setValue(0)
        self._cargar_labores()

    def _lab_editar(self) -> None:
        id_l = self._lab_id_seleccionado()
        if id_l is None:
            return
        labores = self._cl_l.listar(self._sesion.usuario.id_fundo,
                                     solo_activos=False)
        actual = next((l for l in labores if l.id_labor == id_l), None)
        if not actual:
            return
        nombre, ok = QInputDialog.getText(self, "Editar Labor",
                                          "Nombre:", text=actual.nombre)
        if not ok:
            return
        bono_str, ok = QInputDialog.getText(
            self, "Editar Labor",
            f"Bono por hora (S/.) — actual: {actual.bono_por_hora:.2f}",
            text=str(actual.bono_por_hora),
        )
        if not ok:
            return
        try:
            bono = float(bono_str.replace(",", "."))
        except ValueError:
            QMessageBox.warning(self, "Error", "Bono inválido.")
            return
        desc, ok = QInputDialog.getText(self, "Editar Labor",
                                        "Descripción:", text=actual.descripcion)
        if not ok:
            return
        try:
            self._cl_l.actualizar(id_l, self._sesion.usuario.id_fundo,
                                   actual.id_actividad, nombre,
                                   actual.codigo, desc, bono, actual.activo)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_labores()

    def _lab_eliminar(self) -> None:
        id_l = self._lab_id_seleccionado()
        if id_l is None:
            return
        r = QMessageBox.question(
            self, "Eliminar labor", "¿Eliminar esta labor?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl_l.eliminar(id_l)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_labores()
