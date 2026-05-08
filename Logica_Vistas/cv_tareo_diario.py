"""Vista de Tareo Diario — tabla por fecha estilo Excel."""
from __future__ import annotations

import logging
from datetime import date
from typing import Optional

from PySide6.QtCore import Qt, QTimer, QDate
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QAbstractItemView, QMessageBox, QTableWidgetItem, QWidget,
)

from Vistas.personal.ui_tareo_diario import Ui_TareoDiario
from Vistas.recursos.estilos import (
    QSS_LISTA, COLOR_PRIMARIO, COLOR_SECUNDARIO, COLOR_TEXTO_TENUE,
)
from Logica.cl_tareo import ClTareo, TareoFila
from Conexion.cn_sesion import Sesion

log = logging.getLogger(__name__)

CABECERAS = ["Cód.", "Empleado", "Cargo", "Lote", "Actividad", "Labor",
             "Mañ.", "Tar.", "Ext.", "Total", "Bono S/.", "Comentario"]


class CvTareoDiario(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_TareoDiario()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_LISTA)

        self._cl = ClTareo()
        self._sesion = Sesion()

        self.ui.dtFecha.setDate(QDate.currentDate())
        self.ui.dtFecha.setCalendarPopup(True)
        self.ui.dtFecha.setDisplayFormat("dd/MM/yyyy")

        self._configurar_tabla()
        self._configurar_permisos()

        self.ui.dtFecha.dateChanged.connect(lambda _: self._cargar())
        self.ui.btnHoy.clicked.connect(
            lambda: self.ui.dtFecha.setDate(QDate.currentDate())
        )
        self.ui.btnAyer.clicked.connect(
            lambda: self.ui.dtFecha.setDate(QDate.currentDate().addDays(-1))
        )
        self.ui.btnNuevo.clicked.connect(self._nuevo)
        self.ui.btnDuplicar.clicked.connect(self._duplicar)
        self.ui.btnEditar.clicked.connect(self._editar)
        self.ui.btnEliminar.clicked.connect(self._eliminar)
        self.ui.tblTareo.itemDoubleClicked.connect(lambda _: self._editar())

        QTimer.singleShot(0, self._cargar)

    # ------------------------------------------------------------------
    def _configurar_tabla(self) -> None:
        t = self.ui.tblTareo
        t.setColumnCount(len(CABECERAS))
        t.setHorizontalHeaderLabels(CABECERAS)
        t.setAlternatingRowColors(True)
        t.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        t.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        t.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        t.verticalHeader().setVisible(False)
        anchos = [70, 200, 110, 90, 110, 160, 60, 60, 60, 70, 90, 220]
        for col, w in enumerate(anchos):
            t.setColumnWidth(col, w)

    def _configurar_permisos(self) -> None:
        s = self._sesion
        self.ui.btnNuevo.setVisible(s.puede("PERSONAL_TAREO", "crear")
                                     or s.usuario.es_admin)
        self.ui.btnDuplicar.setVisible(s.puede("PERSONAL_TAREO", "crear")
                                        or s.usuario.es_admin)
        self.ui.btnEditar.setVisible(s.puede("PERSONAL_TAREO", "editar")
                                      or s.usuario.es_admin)
        self.ui.btnEliminar.setVisible(s.puede("PERSONAL_TAREO", "eliminar")
                                        or s.usuario.es_admin)

    # ------------------------------------------------------------------
    def _fecha_actual(self) -> date:
        return self.ui.dtFecha.date().toPython()

    def _cargar(self) -> None:
        try:
            filas = self._cl.listar_por_fecha(
                self._sesion.usuario.id_fundo, self._fecha_actual()
            )
        except Exception as e:
            log.exception("Error listando tareo")
            QMessageBox.critical(self, "Error",
                                 f"No se pudo cargar el tareo:\n{e}")
            return

        t = self.ui.tblTareo
        t.setRowCount(0)
        total_h = 0.0
        total_bono = 0.0
        empleados_unicos = set()
        for f in filas:
            self._agregar_fila(f)
            total_h += f.horas_total
            total_bono += f.bono_total
            empleados_unicos.add(f.id_empleado)

        self.ui.lblTotales.setText(
            f"Total horas: <b>{total_h:.2f}</b>  ·  "
            f"Personas: <b>{len(empleados_unicos)}</b>  ·  "
            f"Bono: <b>S/. {total_bono:,.2f}</b>"
        )

    def _agregar_fila(self, t: TareoFila) -> None:
        tbl = self.ui.tblTareo
        fila = tbl.rowCount()
        tbl.insertRow(fila)
        valores = [
            t.empleado_codigo, t.empleado_nombre, t.cargo_nombre,
            t.lote_codigo, t.actividad_nombre, t.labor_nombre,
            f"{t.horas_manana:.2f}",
            f"{t.horas_tarde:.2f}",
            f"{t.horas_extras:.2f}",
            f"{t.horas_total:.2f}",
            f"{t.bono_total:.2f}" if t.bono_total > 0 else "",
            t.comentario,
        ]
        for col, txt in enumerate(valores):
            it = QTableWidgetItem(txt)
            it.setData(Qt.ItemDataRole.UserRole, t.id_tareo)
            if col in (6, 7, 8, 9, 10):
                it.setTextAlignment(Qt.AlignmentFlag.AlignRight
                                    | Qt.AlignmentFlag.AlignVCenter)
            if col == 8 and t.horas_extras > 0:
                it.setForeground(QColor("#E67E22"))
            if col == 9:
                f = it.font(); f.setBold(True); it.setFont(f)
            if col == 10 and t.bono_total > 0:
                it.setForeground(QColor(COLOR_SECUNDARIO))
                f = it.font(); f.setBold(True); it.setFont(f)
            tbl.setItem(fila, col, it)

    def _id_seleccionado(self) -> Optional[int]:
        fila = self.ui.tblTareo.currentRow()
        if fila < 0:
            return None
        item = self.ui.tblTareo.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def _datos_fila_seleccionada(self) -> Optional[dict]:
        """Re-obtiene los datos completos del tareo seleccionado."""
        id_t = self._id_seleccionado()
        if id_t is None:
            return None
        # Buscar en lista actual (más rápido que reconsultar)
        # Pero necesitamos campos id_*, listar_por_fecha trae todos.
        for f in self._cl.listar_por_fecha(self._sesion.usuario.id_fundo,
                                            self._fecha_actual()):
            if f.id_tareo == id_t:
                return {
                    "id_tareo": f.id_tareo,
                    "fecha": self._fecha_actual(),
                    "id_empleado": f.id_empleado,
                    "id_cargo": f.id_cargo,
                    "id_lote": f.id_lote,
                    "id_labor": f.id_labor,
                    "id_actividad": f.id_actividad,
                    "horas_manana": f.horas_manana,
                    "horas_tarde": f.horas_tarde,
                    "horas_extras": f.horas_extras,
                    "comentario": f.comentario,
                }
        return None

    # ------------------------------------------------------------------
    def _nuevo(self) -> None:
        from Logica_Vistas.cv_tareo_form import CvTareoForm
        dlg = CvTareoForm(self._sesion.usuario.id_fundo,
                          fecha_default=self._fecha_actual(), parent=self)
        if dlg.exec() == dlg.DialogCode.Accepted:
            self._cargar()

    def _duplicar(self) -> None:
        d = self._datos_fila_seleccionada()
        if d is None:
            QMessageBox.information(self, "Duplicar",
                                    "Selecciona una fila primero.")
            return
        from Logica_Vistas.cv_tareo_form import CvTareoForm
        dlg = CvTareoForm(self._sesion.usuario.id_fundo,
                          id_tareo=None, precarga=d, parent=self)
        if dlg.exec() == dlg.DialogCode.Accepted:
            self._cargar()

    def _editar(self) -> None:
        d = self._datos_fila_seleccionada()
        if d is None:
            QMessageBox.information(self, "Editar",
                                    "Selecciona una fila primero.")
            return
        from Logica_Vistas.cv_tareo_form import CvTareoForm
        dlg = CvTareoForm(self._sesion.usuario.id_fundo,
                          id_tareo=d["id_tareo"], precarga=d, parent=self)
        if dlg.exec() == dlg.DialogCode.Accepted:
            self._cargar()

    def _eliminar(self) -> None:
        id_t = self._id_seleccionado()
        if id_t is None:
            QMessageBox.information(self, "Eliminar",
                                    "Selecciona una fila primero.")
            return
        r = QMessageBox.question(
            self, "Eliminar fila", "¿Eliminar esta fila del tareo?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r != QMessageBox.StandardButton.Yes:
            return
        try:
            self._cl.eliminar(id_t)
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))
            return
        self._cargar()
