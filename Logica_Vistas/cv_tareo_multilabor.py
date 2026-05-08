"""Diálogo: tareo de un empleado en múltiples labores/lotes."""
from __future__ import annotations

from datetime import date
from typing import Optional

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QAbstractItemView, QDialog, QTableWidgetItem,
)

from Vistas.personal.ui_tareo_multilabor import Ui_TareoMultiLabor
from Vistas.recursos.estilos import QSS_FORM, RUTA_ICONO
from Logica.cl_tareo import ClTareo
from Logica.cl_empleado import ClEmpleado
from Logica.cl_cargo import ClCargo
from Logica.cl_lote import ClLote
from Logica.cl_actividad import ClActividad
from Logica.cl_labor import ClLabor
from Conexion.cn_sesion import Sesion


CABECERAS = ["Lote", "Actividad", "Labor", "Mañ.", "Tar.", "Ext.",
             "Total", "Bono S/.", "Comentario"]


class CvTareoMultiLabor(QDialog):

    def __init__(self, id_fundo: int,
                 fecha_default: Optional[date] = None,
                 parent=None):
        super().__init__(parent)
        self.ui = Ui_TareoMultiLabor()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_FORM)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))

        self._id_fundo = id_fundo
        self._cl = ClTareo()
        self._cl_lab = ClLabor()
        self._bonos_por_labor: dict[int, float] = {}

        # Filas pendientes (cada una es un dict de datos para crear)
        self._filas_pendientes: list[dict] = []

        self.ui.dtFecha.setDate(QDate(fecha_default) if fecha_default
                                else QDate.currentDate())

        self._configurar_tabla()
        self._cargar_combos()
        self._cargar_empleados()
        self._cargar_labores(None)
        self.ui.spHM.setValue(0)
        self.ui.spHT.setValue(0)

        self.ui.cboActividad.currentIndexChanged.connect(self._on_actividad)
        self.ui.btnAgregar.clicked.connect(self._agregar_fila)
        self.ui.btnQuitar.clicked.connect(self._quitar_fila)
        self.ui.btnGuardar.clicked.connect(self._guardar)
        self.ui.btnCancelar.clicked.connect(self.reject)

    # ------------------------------------------------------------------
    def _configurar_tabla(self) -> None:
        t = self.ui.tblFilas
        t.setColumnCount(len(CABECERAS))
        t.setHorizontalHeaderLabels(CABECERAS)
        t.setAlternatingRowColors(True)
        t.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        t.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        t.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        t.verticalHeader().setVisible(False)
        for col, w in enumerate([90, 110, 200, 60, 60, 60, 70, 90, 240]):
            t.setColumnWidth(col, w)

    def _cargar_combos(self) -> None:
        self.ui.cboLote.clear()
        self.ui.cboLote.addItem("(ninguno)", None)
        for lt in ClLote().listar(self._id_fundo):
            self.ui.cboLote.addItem(f"{lt.codigo} — {lt.nombre}", lt.id_lote)

        self.ui.cboCargo.clear()
        self.ui.cboCargo.addItem("(no especificar)", None)
        for c in ClCargo().listar(self._id_fundo):
            self.ui.cboCargo.addItem(c.nombre, c.id_cargo)

        self.ui.cboActividad.clear()
        self.ui.cboActividad.addItem("(todas)", None)
        for a in ClActividad().listar(self._id_fundo):
            self.ui.cboActividad.addItem(a.nombre, a.id_actividad)

    def _cargar_empleados(self) -> None:
        self.ui.cboEmpleado.clear()
        self.ui.cboEmpleado.addItem("(seleccionar)", None)
        for e in ClEmpleado().listar(self._id_fundo, estado="Activo"):
            etiqueta = f"{e.codigo} — {e.apellidos.strip()} {e.nombres}"
            self.ui.cboEmpleado.addItem(etiqueta, e.id_empleado)

    def _cargar_labores(self, id_act: Optional[int]) -> None:
        self.ui.cboLabor.blockSignals(True)
        self.ui.cboLabor.clear()
        self.ui.cboLabor.addItem("(ninguna)", None)
        labores = self._cl_lab.listar(self._id_fundo, id_act)
        self._bonos_por_labor = {}
        for l in labores:
            etiqueta = l.nombre
            if l.bono_por_hora > 0:
                etiqueta += f"  (S/.{l.bono_por_hora:.2f}/h)"
            self.ui.cboLabor.addItem(etiqueta, l.id_labor)
            self._bonos_por_labor[l.id_labor] = l.bono_por_hora
        self.ui.cboLabor.blockSignals(False)

    def _on_actividad(self, _i: int) -> None:
        self._cargar_labores(self.ui.cboActividad.currentData())

    # ------------------------------------------------------------------
    def _agregar_fila(self) -> None:
        self.ui.lblError.setText("")
        hm = self.ui.spHM.value()
        ht = self.ui.spHT.value()
        he = self.ui.spHE.value()
        if hm + ht + he <= 0:
            self.ui.lblError.setText("Ingresa al menos alguna hora.")
            return

        id_lote = self.ui.cboLote.currentData()
        id_act  = self.ui.cboActividad.currentData()
        id_lab  = self.ui.cboLabor.currentData()

        fila = {
            "id_lote": id_lote,
            "lote_label": self.ui.cboLote.currentText() if id_lote else "",
            "id_actividad": id_act,
            "actividad_label": self.ui.cboActividad.currentText() if id_act else "",
            "id_labor": id_lab,
            "labor_label": self.ui.cboLabor.currentText() if id_lab else "",
            "horas_manana": hm,
            "horas_tarde": ht,
            "horas_extras": he,
            "comentario": self.ui.txtComent.toPlainText().strip(),
            "bono_h": self._bonos_por_labor.get(id_lab, 0) if id_lab else 0,
        }
        self._filas_pendientes.append(fila)
        self._refrescar_tabla()

        # Limpiar campos para siguiente fila
        self.ui.spHM.setValue(0)
        self.ui.spHT.setValue(0)
        self.ui.spHE.setValue(0)
        self.ui.txtComent.clear()

    def _quitar_fila(self) -> None:
        fila = self.ui.tblFilas.currentRow()
        if 0 <= fila < len(self._filas_pendientes):
            self._filas_pendientes.pop(fila)
            self._refrescar_tabla()

    def _refrescar_tabla(self) -> None:
        from PySide6.QtGui import QColor
        t = self.ui.tblFilas
        t.setRowCount(0)
        total_h = 0.0
        total_bono = 0.0
        for f in self._filas_pendientes:
            fila = t.rowCount()
            t.insertRow(fila)
            tot = f["horas_manana"] + f["horas_tarde"] + f["horas_extras"]
            bono = tot * f["bono_h"]
            total_h += tot
            total_bono += bono
            # Limpiar etiqueta del combo (quitar el "(bono S/...)")
            labor_txt = f["labor_label"].split("  (")[0]
            valores = [
                f["lote_label"], f["actividad_label"], labor_txt,
                f"{f['horas_manana']:.2f}",
                f"{f['horas_tarde']:.2f}",
                f"{f['horas_extras']:.2f}",
                f"{tot:.2f}",
                f"{bono:.2f}" if bono > 0 else "",
                f["comentario"],
            ]
            for col, txt in enumerate(valores):
                it = QTableWidgetItem(txt)
                if col in (3, 4, 5, 6, 7):
                    it.setTextAlignment(Qt.AlignmentFlag.AlignRight
                                         | Qt.AlignmentFlag.AlignVCenter)
                if col == 7 and bono > 0:
                    it.setForeground(QColor("#3DBA3F"))
                t.setItem(fila, col, it)

        self.ui.lblTotales.setText(
            f"Total: <b>{len(self._filas_pendientes)}</b> filas  ·  "
            f"<b>{total_h:.2f} h</b>  ·  <b>S/. {total_bono:,.2f}</b>"
        )

    # ------------------------------------------------------------------
    def _guardar(self) -> None:
        self.ui.lblError.setText("")
        id_emp = self.ui.cboEmpleado.currentData()
        if id_emp is None:
            self.ui.lblError.setText("Selecciona un empleado.")
            return
        if not self._filas_pendientes:
            self.ui.lblError.setText("Agrega al menos una fila a la lista.")
            return

        from Conexion.cn_sesion import Sesion
        base = {
            "id_fundo": self._id_fundo,
            "id_empleado": id_emp,
            "fecha": self.ui.dtFecha.date().toPython(),
            "id_cargo": self.ui.cboCargo.currentData(),
            "creado_por": Sesion().usuario.id_usuario,
        }
        filas = []
        for f in self._filas_pendientes:
            d = dict(base)
            d.update({
                "id_lote": f["id_lote"],
                "id_labor": f["id_labor"],
                "id_actividad": f["id_actividad"],
                "horas_manana": f["horas_manana"],
                "horas_tarde": f["horas_tarde"],
                "horas_extras": f["horas_extras"],
                "comentario": f["comentario"],
            })
            filas.append(d)

        try:
            n = self._cl.crear_masivo(filas)
        except ValueError as e:
            self.ui.lblError.setText(str(e))
            return
        except Exception as e:
            self.ui.lblError.setText(f"Error: {e}")
            return
        self._n_creados = n
        self.accept()
