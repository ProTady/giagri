"""Diálogo crear/editar/duplicar fila de tareo."""
from __future__ import annotations

from datetime import date
from typing import Optional

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from Vistas.personal.ui_tareo_form import Ui_TareoForm
from Vistas.recursos.estilos import QSS_FORM, RUTA_ICONO
from Logica.cl_tareo import ClTareo
from Logica.cl_empleado import ClEmpleado
from Logica.cl_cargo import ClCargo
from Logica.cl_lote import ClLote
from Logica.cl_actividad import ClActividad
from Logica.cl_labor import ClLabor


class CvTareoForm(QDialog):
    """Si id_tareo=None y precarga=None: nuevo en blanco.
       Si id_tareo!=None: editar.
       Si id_tareo=None y precarga!=None: 'Duplicar' (carga datos pero crea)."""

    def __init__(self, id_fundo: int,
                 id_tareo: Optional[int] = None,
                 precarga: Optional[dict] = None,
                 fecha_default: Optional[date] = None,
                 parent=None):
        super().__init__(parent)
        self.ui = Ui_TareoForm()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_FORM)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))

        self._id_fundo = id_fundo
        self._id_tareo = id_tareo
        self._cl = ClTareo()
        self._cl_lab = ClLabor()
        self._labores_cache: dict[int, list] = {}  # por actividad

        self._cargar_combos()

        self.ui.cboActividad.currentIndexChanged.connect(self._on_actividad_cambiada)
        self.ui.cboLabor.currentIndexChanged.connect(self._actualizar_bono)
        for sp in (self.ui.spHM, self.ui.spHT, self.ui.spHE):
            sp.valueChanged.connect(self._actualizar_total)
        self.ui.btnGuardar.clicked.connect(self._guardar)
        self.ui.btnCancelar.clicked.connect(self.reject)

        self._configurar_modo(precarga, fecha_default)

    # ------------------------------------------------------------------
    def _cargar_combos(self) -> None:
        # Empleados activos
        self.ui.cboEmpleado.clear()
        self.ui.cboEmpleado.addItem("(seleccionar)", None)
        for e in ClEmpleado().listar(self._id_fundo, estado="Activo"):
            etiqueta = f"{e.codigo} — {e.apellidos.strip()} {e.nombres}"
            self.ui.cboEmpleado.addItem(etiqueta, e.id_empleado)

        self.ui.cboCargo.clear()
        self.ui.cboCargo.addItem("(ninguno)", None)
        for c in ClCargo().listar(self._id_fundo):
            self.ui.cboCargo.addItem(c.nombre, c.id_cargo)

        self.ui.cboLote.clear()
        self.ui.cboLote.addItem("(ninguno)", None)
        try:
            from Logica.cl_lote import ClLote as _CL
            for lt in _CL().listar(self._id_fundo):
                self.ui.cboLote.addItem(f"{lt.codigo} — {lt.nombre}", lt.id_lote)
        except Exception:
            pass

        self.ui.cboActividad.clear()
        self.ui.cboActividad.addItem("(todas)", None)
        for a in ClActividad().listar(self._id_fundo):
            self.ui.cboActividad.addItem(a.nombre, a.id_actividad)

        # Labor: todas al inicio
        self._cargar_labores(None)

    def _cargar_labores(self, id_actividad: Optional[int]) -> None:
        self.ui.cboLabor.blockSignals(True)
        self.ui.cboLabor.clear()
        self.ui.cboLabor.addItem("(ninguna)", None)
        labores = self._cl_lab.listar(self._id_fundo, id_actividad)
        for l in labores:
            etiqueta = l.nombre
            if l.bono_por_hora > 0:
                etiqueta += f"  (bono S/.{l.bono_por_hora:.2f}/h)"
            self.ui.cboLabor.addItem(etiqueta, l.id_labor)
            # Guardamos bono por id_labor
        # Cache para consulta rápida del bono
        self._bonos_por_labor = {l.id_labor: l.bono_por_hora for l in labores}
        self.ui.cboLabor.blockSignals(False)
        self._actualizar_bono()

    def _on_actividad_cambiada(self, _idx: int) -> None:
        id_act = self.ui.cboActividad.currentData()
        self._cargar_labores(id_act)

    def _actualizar_total(self) -> None:
        total = (self.ui.spHM.value() + self.ui.spHT.value()
                 + self.ui.spHE.value())
        self.ui.lblTotal.setText(f"{total:.2f} h")
        self._actualizar_bono()

    def _actualizar_bono(self) -> None:
        id_lab = self.ui.cboLabor.currentData()
        bono_h = self._bonos_por_labor.get(id_lab, 0) if id_lab else 0
        total = (self.ui.spHM.value() + self.ui.spHT.value()
                 + self.ui.spHE.value())
        bono = bono_h * total
        self.ui.lblBono.setText(f"S/. {bono:.2f}  ({bono_h:.2f}/h × {total:.2f}h)")

    # ------------------------------------------------------------------
    def _configurar_modo(self, precarga: Optional[dict],
                         fecha_default: Optional[date]) -> None:
        if self._id_tareo is None and precarga is None:
            self.ui.lblTitulo.setText("Nueva fila de Tareo")
            self.setWindowTitle("Nueva fila de Tareo")
            if fecha_default:
                self.ui.dtFecha.setDate(QDate(fecha_default))
            else:
                self.ui.dtFecha.setDate(QDate.currentDate())
            self.ui.spHM.setValue(8.0)
            return

        if self._id_tareo is None and precarga is not None:
            self.ui.lblTitulo.setText("Duplicar fila de Tareo")
            self.setWindowTitle("Duplicar fila de Tareo")
        else:
            self.ui.lblTitulo.setText("Editar fila de Tareo")
            self.setWindowTitle("Editar fila de Tareo")

        d = precarga or {}
        if d.get("fecha"):
            self.ui.dtFecha.setDate(QDate(d["fecha"]))
        else:
            self.ui.dtFecha.setDate(QDate.currentDate())

        self._sel_data(self.ui.cboEmpleado, d.get("id_empleado"))
        self._sel_data(self.ui.cboCargo, d.get("id_cargo"))
        self._sel_data(self.ui.cboLote, d.get("id_lote"))
        self._sel_data(self.ui.cboActividad, d.get("id_actividad"))
        # Recargar labores por actividad
        self._cargar_labores(d.get("id_actividad"))
        self._sel_data(self.ui.cboLabor, d.get("id_labor"))

        self.ui.spHM.setValue(float(d.get("horas_manana", 0) or 0))
        self.ui.spHT.setValue(float(d.get("horas_tarde", 0) or 0))
        self.ui.spHE.setValue(float(d.get("horas_extras", 0) or 0))
        self.ui.txtComent.setPlainText(d.get("comentario", "") or "")
        self._actualizar_total()

    @staticmethod
    def _sel_data(cbo, valor) -> None:
        if valor is None:
            cbo.setCurrentIndex(0)
            return
        for i in range(cbo.count()):
            if cbo.itemData(i) == valor:
                cbo.setCurrentIndex(i)
                return

    # ------------------------------------------------------------------
    def _recolectar(self) -> dict:
        from Conexion.cn_sesion import Sesion
        return {
            "id_fundo": self._id_fundo,
            "id_empleado": self.ui.cboEmpleado.currentData(),
            "fecha": self.ui.dtFecha.date().toPython(),
            "id_cargo": self.ui.cboCargo.currentData(),
            "id_lote": self.ui.cboLote.currentData(),
            "id_labor": self.ui.cboLabor.currentData(),
            "id_actividad": self.ui.cboActividad.currentData(),
            "horas_manana": self.ui.spHM.value(),
            "horas_tarde": self.ui.spHT.value(),
            "horas_extras": self.ui.spHE.value(),
            "comentario": self.ui.txtComent.toPlainText(),
            "creado_por": Sesion().usuario.id_usuario,
        }

    def _guardar(self) -> None:
        self.ui.lblError.setText("")
        datos = self._recolectar()
        try:
            if self._id_tareo is None:
                self._cl.crear(datos)
            else:
                self._cl.actualizar(self._id_tareo, datos)
        except ValueError as e:
            self.ui.lblError.setText(str(e))
            return
        except Exception as e:
            self.ui.lblError.setText(f"Error: {e}")
            return
        self.accept()
