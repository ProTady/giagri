"""Vista de listado de empleados."""
from __future__ import annotations

import logging
from typing import Optional

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QAbstractItemView, QMessageBox, QTableWidgetItem, QWidget,
)

from Vistas.personal.ui_empleados_lista import Ui_EmpleadosLista
from Vistas.recursos.estilos import (
    QSS_LISTA, COLOR_SECUNDARIO, COLOR_TEXTO_TENUE, COLOR_ERROR,
)
from Logica.cl_empleado import ClEmpleado, EmpleadoFila
from Conexion.cn_sesion import Sesion

log = logging.getLogger(__name__)

CABECERAS = ["Código", "DNI", "Apellidos", "Nombres",
             "Cargo", "Área", "Ingreso", "Estado"]

COLOR_ESTADO = {
    "Activo":     COLOR_SECUNDARIO,
    "Cesado":     COLOR_ERROR,
    "Vacaciones": "#E67E22",
    "Suspendido": "#8E44AD",
}


class CvEmpleadosLista(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EmpleadosLista()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_LISTA)

        self._cl = ClEmpleado()
        self._sesion = Sesion()

        self._configurar_tabla()
        self._configurar_permisos()

        self.ui.btnNuevo.clicked.connect(self._nuevo)
        self.ui.btnEditar.clicked.connect(self._editar)
        self.ui.btnEliminar.clicked.connect(self._eliminar)
        self.ui.txtBuscar.textChanged.connect(lambda _: self._cargar())
        self.ui.cboEstado.currentIndexChanged.connect(lambda _: self._cargar())
        self.ui.tblEmpleados.itemDoubleClicked.connect(lambda _: self._editar())

        QTimer.singleShot(0, self._cargar)

    def _configurar_tabla(self) -> None:
        t = self.ui.tblEmpleados
        t.setColumnCount(len(CABECERAS))
        t.setHorizontalHeaderLabels(CABECERAS)
        t.setAlternatingRowColors(True)
        t.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        t.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        t.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        t.verticalHeader().setVisible(False)
        for col, w in enumerate([90, 100, 220, 180, 140, 130, 100, 100]):
            t.setColumnWidth(col, w)

    def _configurar_permisos(self) -> None:
        s = self._sesion
        self.ui.btnNuevo.setVisible(s.puede("PERSONAL_LISTA", "crear"))
        self.ui.btnEditar.setVisible(s.puede("PERSONAL_LISTA", "editar"))
        self.ui.btnEliminar.setVisible(s.puede("PERSONAL_LISTA", "eliminar"))

    def _cargar(self) -> None:
        filtro = self.ui.txtBuscar.text().strip()
        estado_idx = self.ui.cboEstado.currentIndex()
        estado = ["todos","Activo","Cesado","Vacaciones","Suspendido"][estado_idx]

        try:
            filas = self._cl.listar(self._sesion.usuario.id_fundo, filtro, estado)
        except Exception as e:
            log.exception("Error listando empleados")
            QMessageBox.critical(self, "Error", f"No se pudieron cargar:\n{e}")
            return

        t = self.ui.tblEmpleados
        t.setRowCount(0)
        for f in filas:
            self._agregar_fila(f)
        self.ui.lblTotal.setText(f"{len(filas)} empleados")

    def _agregar_fila(self, e: EmpleadoFila) -> None:
        t = self.ui.tblEmpleados
        fila = t.rowCount()
        t.insertRow(fila)
        ingreso = e.fecha_ingreso.strftime("%Y-%m-%d") if e.fecha_ingreso else ""
        valores = [e.codigo, e.dni, e.apellidos, e.nombres,
                   e.cargo, e.area, ingreso, e.estado]
        for col, txt in enumerate(valores):
            it = QTableWidgetItem(txt)
            it.setData(Qt.ItemDataRole.UserRole, e.id_empleado)
            if col == 7:
                color = COLOR_ESTADO.get(e.estado, COLOR_TEXTO_TENUE)
                it.setForeground(QColor(color))
            t.setItem(fila, col, it)

    def _id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblEmpleados.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblEmpleados.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _nuevo(self) -> None:
        from Logica_Vistas.cv_empleado_form import CvEmpleadoForm
        dlg = CvEmpleadoForm(self._sesion.usuario.id_fundo, None, self)
        if dlg.exec() == dlg.DialogCode.Accepted:
            self._cargar()

    def _editar(self) -> None:
        id_e = self._id_seleccionado()
        if id_e is None:
            QMessageBox.information(self, "Editar", "Selecciona un empleado primero.")
            return
        from Logica_Vistas.cv_empleado_form import CvEmpleadoForm
        dlg = CvEmpleadoForm(self._sesion.usuario.id_fundo, id_e, self)
        if dlg.exec() == dlg.DialogCode.Accepted:
            self._cargar()

    def _eliminar(self) -> None:
        id_e = self._id_seleccionado()
        if id_e is None:
            QMessageBox.information(self, "Eliminar", "Selecciona un empleado primero.")
            return
        r = QMessageBox.question(
            self, "Eliminar",
            "¿Eliminar este empleado?\n\nEsta acción no se puede deshacer.",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl.eliminar(id_e)
            self._cargar()
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
