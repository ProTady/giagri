"""Vista unificada de catálogos agrícolas: Cultivos, Variedades, Patrones."""
from __future__ import annotations

import logging
from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView, QInputDialog, QMessageBox, QTableWidgetItem, QWidget,
)

from Vistas.lotes.ui_catalogos import Ui_CatalogosAgricolas
from Vistas.recursos.estilos import QSS_LISTA
from Logica.cl_tipo_cultivo import ClTipoCultivo
from Logica.cl_variedad import ClVariedad
from Logica.cl_patron import ClPatron
from Conexion.cn_sesion import Sesion

log = logging.getLogger(__name__)


class CvCatalogosAgricolas(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CatalogosAgricolas()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_LISTA)

        self._cl_tc = ClTipoCultivo()
        self._cl_v = ClVariedad()
        self._cl_p = ClPatron()
        self._sesion = Sesion()

        self._configurar_tablas()
        self._configurar_permisos()
        self._conectar_senales()
        self._cargar_todo()

    # ------------------------------------------------------------------
    def _configurar_tablas(self) -> None:
        for tbl, cabs, anchos in [
            (self.ui.tblCultivos,
             ["Nombre", "Nombre científico", "Activo"], [200, 280, 80]),
            (self.ui.tblVariedades,
             ["Cultivo", "Variedad", "Descripción", "Activo"],
             [150, 180, 280, 80]),
            (self.ui.tblPatrones,
             ["Cultivo", "Patrón", "Descripción", "Activo"],
             [150, 180, 280, 80]),
        ]:
            tbl.setColumnCount(len(cabs))
            tbl.setHorizontalHeaderLabels(cabs)
            tbl.setAlternatingRowColors(True)
            tbl.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
            tbl.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
            tbl.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
            tbl.verticalHeader().setVisible(False)
            for col, w in enumerate(anchos):
                tbl.setColumnWidth(col, w)

    def _configurar_permisos(self) -> None:
        s = self._sesion
        crear = s.puede("LOTES_CULTIVOS", "crear")
        editar = s.puede("LOTES_CULTIVOS", "editar")
        elim = s.puede("LOTES_CULTIVOS", "eliminar")
        for btn, ok in [
            (self.ui.btnCultivoAgregar, crear),
            (self.ui.btnVarAgregar, crear),
            (self.ui.btnPatAgregar, crear),
            (self.ui.btnCultivoEditar, editar),
            (self.ui.btnVarEditar, editar),
            (self.ui.btnPatEditar, editar),
            (self.ui.btnCultivoEliminar, elim),
            (self.ui.btnVarEliminar, elim),
            (self.ui.btnPatEliminar, elim),
        ]:
            btn.setEnabled(ok)

    def _conectar_senales(self) -> None:
        # Cultivos
        self.ui.btnCultivoAgregar.clicked.connect(self._cultivo_agregar)
        self.ui.btnCultivoEditar.clicked.connect(self._cultivo_editar)
        self.ui.btnCultivoEliminar.clicked.connect(self._cultivo_eliminar)
        self.ui.tblCultivos.itemDoubleClicked.connect(
            lambda _: self._cultivo_editar()
        )
        # Variedades
        self.ui.btnVarAgregar.clicked.connect(self._var_agregar)
        self.ui.btnVarEditar.clicked.connect(self._var_editar)
        self.ui.btnVarEliminar.clicked.connect(self._var_eliminar)
        self.ui.cboVarFiltro.currentIndexChanged.connect(
            lambda _: self._var_cargar()
        )
        self.ui.tblVariedades.itemDoubleClicked.connect(
            lambda _: self._var_editar()
        )
        # Patrones
        self.ui.btnPatAgregar.clicked.connect(self._pat_agregar)
        self.ui.btnPatEditar.clicked.connect(self._pat_editar)
        self.ui.btnPatEliminar.clicked.connect(self._pat_eliminar)
        self.ui.cboPatFiltro.currentIndexChanged.connect(
            lambda _: self._pat_cargar()
        )
        self.ui.tblPatrones.itemDoubleClicked.connect(
            lambda _: self._pat_editar()
        )

    # ==================================================================
    # CARGA INICIAL
    # ==================================================================
    def _cargar_todo(self) -> None:
        self._cargar_cultivos()
        self._refrescar_combos_cultivo()
        self._var_cargar()
        self._pat_cargar()

    def _refrescar_combos_cultivo(self) -> None:
        cultivos = self._cl_tc.listar(self._sesion.usuario.id_fundo)
        for cbo, con_todos in [
            (self.ui.cboVarCultivo, False),
            (self.ui.cboPatCultivo, False),
            (self.ui.cboVarFiltro, True),
            (self.ui.cboPatFiltro, True),
        ]:
            cbo.blockSignals(True)
            cbo.clear()
            if con_todos:
                cbo.addItem("(Todos)", None)
            for t in cultivos:
                cbo.addItem(t.nombre, t.id_tipo_cultivo)
            cbo.blockSignals(False)

    # ==================================================================
    # CULTIVOS
    # ==================================================================
    def _cargar_cultivos(self) -> None:
        cultivos = self._cl_tc.listar(self._sesion.usuario.id_fundo,
                                      solo_activos=False)
        t = self.ui.tblCultivos
        t.setRowCount(0)
        for c in cultivos:
            fila = t.rowCount()
            t.insertRow(fila)
            it_nom = QTableWidgetItem(c.nombre)
            it_nom.setData(Qt.ItemDataRole.UserRole, c.id_tipo_cultivo)
            t.setItem(fila, 0, it_nom)
            t.setItem(fila, 1, QTableWidgetItem(c.nombre_cientifico))
            t.setItem(fila, 2, QTableWidgetItem("Sí" if c.activo else "No"))

    def _cultivo_id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblCultivos.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblCultivos.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _cultivo_agregar(self) -> None:
        nombre = self.ui.txtCultivoNombre.text().strip()
        sci = self.ui.txtCultivoSci.text().strip()
        if not nombre:
            QMessageBox.information(self, "Cultivo", "Ingresa un nombre.")
            return
        try:
            self._cl_tc.crear(self._sesion.usuario.id_fundo, nombre, sci)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self.ui.txtCultivoNombre.clear()
        self.ui.txtCultivoSci.clear()
        self._cargar_cultivos()
        self._refrescar_combos_cultivo()

    def _cultivo_editar(self) -> None:
        id_c = self._cultivo_id_seleccionado()
        if id_c is None:
            return
        cultivos = self._cl_tc.listar(self._sesion.usuario.id_fundo,
                                      solo_activos=False)
        actual = next((c for c in cultivos if c.id_tipo_cultivo == id_c), None)
        if not actual:
            return
        nombre, ok = QInputDialog.getText(
            self, "Editar Cultivo", "Nombre:", text=actual.nombre
        )
        if not ok:
            return
        sci, ok = QInputDialog.getText(
            self, "Editar Cultivo", "Nombre científico:",
            text=actual.nombre_cientifico
        )
        if not ok:
            return
        try:
            self._cl_tc.actualizar(id_c, self._sesion.usuario.id_fundo,
                                   nombre, sci, actual.activo)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_cultivos()
        self._refrescar_combos_cultivo()

    def _cultivo_eliminar(self) -> None:
        id_c = self._cultivo_id_seleccionado()
        if id_c is None:
            return
        r = QMessageBox.question(
            self, "Eliminar cultivo",
            "¿Eliminar este tipo de cultivo?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl_tc.eliminar(id_c)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar_cultivos()
        self._refrescar_combos_cultivo()

    # ==================================================================
    # VARIEDADES
    # ==================================================================
    def _var_cargar(self) -> None:
        id_filtro = self.ui.cboVarFiltro.currentData()
        variedades = self._cl_v.listar(
            self._sesion.usuario.id_fundo, id_filtro, solo_activos=False
        )
        # Mapear id_tipo_cultivo a nombre
        cultivos = {t.id_tipo_cultivo: t.nombre
                    for t in self._cl_tc.listar(self._sesion.usuario.id_fundo,
                                                solo_activos=False)}
        t = self.ui.tblVariedades
        t.setRowCount(0)
        for v in variedades:
            fila = t.rowCount()
            t.insertRow(fila)
            it_c = QTableWidgetItem(cultivos.get(v.id_tipo_cultivo, ""))
            it_c.setData(Qt.ItemDataRole.UserRole, v.id_variedad)
            t.setItem(fila, 0, it_c)
            t.setItem(fila, 1, QTableWidgetItem(v.nombre))
            t.setItem(fila, 2, QTableWidgetItem(v.descripcion))
            t.setItem(fila, 3, QTableWidgetItem("Sí" if v.activo else "No"))

    def _var_id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblVariedades.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblVariedades.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _var_agregar(self) -> None:
        id_tc = self.ui.cboVarCultivo.currentData()
        nombre = self.ui.txtVarNombre.text().strip()
        desc = self.ui.txtVarDesc.text().strip()
        if id_tc is None:
            QMessageBox.information(self, "Variedad",
                                    "Selecciona un tipo de cultivo.")
            return
        if not nombre:
            QMessageBox.information(self, "Variedad", "Ingresa un nombre.")
            return
        try:
            self._cl_v.crear(id_tc, nombre, desc)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self.ui.txtVarNombre.clear()
        self.ui.txtVarDesc.clear()
        self._var_cargar()

    def _var_editar(self) -> None:
        id_v = self._var_id_seleccionado()
        if id_v is None:
            return
        variedades = self._cl_v.listar(
            self._sesion.usuario.id_fundo, solo_activos=False
        )
        actual = next((v for v in variedades if v.id_variedad == id_v), None)
        if not actual:
            return
        nombre, ok = QInputDialog.getText(
            self, "Editar Variedad", "Nombre:", text=actual.nombre
        )
        if not ok:
            return
        desc, ok = QInputDialog.getText(
            self, "Editar Variedad", "Descripción:", text=actual.descripcion
        )
        if not ok:
            return
        try:
            self._cl_v.actualizar(id_v, nombre, desc, actual.activo)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._var_cargar()

    def _var_eliminar(self) -> None:
        id_v = self._var_id_seleccionado()
        if id_v is None:
            return
        r = QMessageBox.question(
            self, "Eliminar variedad", "¿Eliminar esta variedad?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl_v.eliminar(id_v)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._var_cargar()

    # ==================================================================
    # PATRONES
    # ==================================================================
    def _pat_cargar(self) -> None:
        id_filtro = self.ui.cboPatFiltro.currentData()
        patrones = self._cl_p.listar(
            self._sesion.usuario.id_fundo, id_filtro, solo_activos=False
        )
        cultivos = {t.id_tipo_cultivo: t.nombre
                    for t in self._cl_tc.listar(self._sesion.usuario.id_fundo,
                                                solo_activos=False)}
        t = self.ui.tblPatrones
        t.setRowCount(0)
        for p in patrones:
            fila = t.rowCount()
            t.insertRow(fila)
            it_c = QTableWidgetItem(cultivos.get(p.id_tipo_cultivo, ""))
            it_c.setData(Qt.ItemDataRole.UserRole, p.id_patron)
            t.setItem(fila, 0, it_c)
            t.setItem(fila, 1, QTableWidgetItem(p.nombre))
            t.setItem(fila, 2, QTableWidgetItem(p.descripcion))
            t.setItem(fila, 3, QTableWidgetItem("Sí" if p.activo else "No"))

    def _pat_id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblPatrones.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblPatrones.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _pat_agregar(self) -> None:
        id_tc = self.ui.cboPatCultivo.currentData()
        nombre = self.ui.txtPatNombre.text().strip()
        desc = self.ui.txtPatDesc.text().strip()
        if id_tc is None:
            QMessageBox.information(self, "Patrón",
                                    "Selecciona un tipo de cultivo.")
            return
        if not nombre:
            QMessageBox.information(self, "Patrón", "Ingresa un nombre.")
            return
        try:
            self._cl_p.crear(id_tc, nombre, desc)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self.ui.txtPatNombre.clear()
        self.ui.txtPatDesc.clear()
        self._pat_cargar()

    def _pat_editar(self) -> None:
        id_p = self._pat_id_seleccionado()
        if id_p is None:
            return
        patrones = self._cl_p.listar(
            self._sesion.usuario.id_fundo, solo_activos=False
        )
        actual = next((p for p in patrones if p.id_patron == id_p), None)
        if not actual:
            return
        nombre, ok = QInputDialog.getText(
            self, "Editar Patrón", "Nombre:", text=actual.nombre
        )
        if not ok:
            return
        desc, ok = QInputDialog.getText(
            self, "Editar Patrón", "Descripción:", text=actual.descripcion
        )
        if not ok:
            return
        try:
            self._cl_p.actualizar(id_p, nombre, desc, actual.activo)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._pat_cargar()

    def _pat_eliminar(self) -> None:
        id_p = self._pat_id_seleccionado()
        if id_p is None:
            return
        r = QMessageBox.question(
            self, "Eliminar patrón", "¿Eliminar este patrón?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl_p.eliminar(id_p)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._pat_cargar()
