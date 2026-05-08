"""Diálogo: tareo masivo — varios empleados, misma labor/lote/horas."""
from __future__ import annotations

from datetime import date
from typing import Optional

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QListWidgetItem

from Vistas.personal.ui_tareo_masivo import Ui_TareoMasivo
from Vistas.recursos.estilos import QSS_FORM, RUTA_ICONO
from Logica.cl_tareo import ClTareo
from Logica.cl_empleado import ClEmpleado
from Logica.cl_cargo import ClCargo
from Logica.cl_lote import ClLote
from Logica.cl_actividad import ClActividad
from Logica.cl_labor import ClLabor
from Conexion.cn_sesion import Sesion


class CvTareoMasivo(QDialog):

    def __init__(self, id_fundo: int,
                 fecha_default: Optional[date] = None,
                 parent=None):
        super().__init__(parent)
        self.ui = Ui_TareoMasivo()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_FORM)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))

        self._id_fundo = id_fundo
        self._cl = ClTareo()
        self._cl_lab = ClLabor()
        self._bonos_por_labor: dict[int, float] = {}
        self._empleados_filtro = []  # lista completa para filtrar

        self.ui.dtFecha.setDate(QDate(fecha_default) if fecha_default
                                else QDate.currentDate())

        self._cargar_combos()
        self._cargar_empleados()

        self.ui.cboActividad.currentIndexChanged.connect(self._on_actividad_cambiada)
        self.ui.cboLabor.currentIndexChanged.connect(self._actualizar_resumen)
        for sp in (self.ui.spHM, self.ui.spHT, self.ui.spHE):
            sp.valueChanged.connect(self._actualizar_resumen)
        self.ui.txtBuscar.textChanged.connect(self._aplicar_filtro)
        self.ui.btnTodos.clicked.connect(lambda: self._marcar_todos(True))
        self.ui.btnNinguno.clicked.connect(lambda: self._marcar_todos(False))
        self.ui.btnInvertir.clicked.connect(self._invertir_seleccion)
        self.ui.lstEmpleados.itemChanged.connect(lambda _: self._actualizar_resumen())
        self.ui.btnGuardar.clicked.connect(self._guardar)
        self.ui.btnCancelar.clicked.connect(self.reject)

        self._actualizar_resumen()

    # ------------------------------------------------------------------
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

        self._cargar_labores(None)

    def _cargar_labores(self, id_actividad: Optional[int]) -> None:
        self.ui.cboLabor.blockSignals(True)
        self.ui.cboLabor.clear()
        self.ui.cboLabor.addItem("(ninguna)", None)
        labores = self._cl_lab.listar(self._id_fundo, id_actividad)
        self._bonos_por_labor = {}
        for l in labores:
            etiqueta = l.nombre
            if l.bono_por_hora > 0:
                etiqueta += f"  (S/.{l.bono_por_hora:.2f}/h)"
            self.ui.cboLabor.addItem(etiqueta, l.id_labor)
            self._bonos_por_labor[l.id_labor] = l.bono_por_hora
        self.ui.cboLabor.blockSignals(False)
        self._actualizar_resumen()

    def _on_actividad_cambiada(self, _i: int) -> None:
        self._cargar_labores(self.ui.cboActividad.currentData())

    # ------------------------------------------------------------------
    def _cargar_empleados(self) -> None:
        self.ui.lstEmpleados.clear()
        self._empleados_filtro = ClEmpleado().listar(
            self._id_fundo, estado="Activo"
        )
        for e in self._empleados_filtro:
            etiqueta = f"{e.codigo}  {e.apellidos.strip()} {e.nombres}"
            if e.cargo:
                etiqueta += f"  ({e.cargo})"
            item = QListWidgetItem(etiqueta)
            item.setData(Qt.ItemDataRole.UserRole, e.id_empleado)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            item.setCheckState(Qt.CheckState.Unchecked)
            self.ui.lstEmpleados.addItem(item)

    def _aplicar_filtro(self, texto: str) -> None:
        texto = texto.lower().strip()
        for i in range(self.ui.lstEmpleados.count()):
            item = self.ui.lstEmpleados.item(i)
            visible = (not texto) or (texto in item.text().lower())
            item.setHidden(not visible)

    def _marcar_todos(self, marcado: bool) -> None:
        estado = Qt.CheckState.Checked if marcado else Qt.CheckState.Unchecked
        self.ui.lstEmpleados.blockSignals(True)
        for i in range(self.ui.lstEmpleados.count()):
            item = self.ui.lstEmpleados.item(i)
            if not item.isHidden():
                item.setCheckState(estado)
        self.ui.lstEmpleados.blockSignals(False)
        self._actualizar_resumen()

    def _invertir_seleccion(self) -> None:
        self.ui.lstEmpleados.blockSignals(True)
        for i in range(self.ui.lstEmpleados.count()):
            item = self.ui.lstEmpleados.item(i)
            if item.isHidden():
                continue
            if item.checkState() == Qt.CheckState.Checked:
                item.setCheckState(Qt.CheckState.Unchecked)
            else:
                item.setCheckState(Qt.CheckState.Checked)
        self.ui.lstEmpleados.blockSignals(False)
        self._actualizar_resumen()

    def _ids_seleccionados(self) -> list[int]:
        return [
            self.ui.lstEmpleados.item(i).data(Qt.ItemDataRole.UserRole)
            for i in range(self.ui.lstEmpleados.count())
            if self.ui.lstEmpleados.item(i).checkState() == Qt.CheckState.Checked
        ]

    # ------------------------------------------------------------------
    def _actualizar_resumen(self) -> None:
        n = len(self._ids_seleccionados())
        horas = (self.ui.spHM.value() + self.ui.spHT.value()
                 + self.ui.spHE.value())
        id_lab = self.ui.cboLabor.currentData()
        bono_h = self._bonos_por_labor.get(id_lab, 0) if id_lab else 0
        total_horas = n * horas
        total_bono = total_horas * bono_h
        self.ui.lblResumen.setText(
            f"Seleccionados: <b>{n}</b>  ·  "
            f"Horas/persona: <b>{horas:.2f}</b>  ·  "
            f"Total horas: <b>{total_horas:.2f}</b>  ·  "
            f"Bono total: <b>S/. {total_bono:,.2f}</b>"
        )

    # ------------------------------------------------------------------
    def _guardar(self) -> None:
        self.ui.lblError.setText("")
        ids = self._ids_seleccionados()
        if not ids:
            self.ui.lblError.setText("Selecciona al menos un empleado.")
            return
        if (self.ui.spHM.value() + self.ui.spHT.value()
                + self.ui.spHE.value()) <= 0:
            self.ui.lblError.setText("Debes ingresar al menos algunas horas.")
            return

        from Conexion.cn_sesion import Sesion
        base = {
            "id_fundo": self._id_fundo,
            "fecha": self.ui.dtFecha.date().toPython(),
            "id_cargo": self.ui.cboCargo.currentData(),
            "id_lote": self.ui.cboLote.currentData(),
            "id_labor": self.ui.cboLabor.currentData(),
            "id_actividad": self.ui.cboActividad.currentData(),
            "horas_manana": self.ui.spHM.value(),
            "horas_tarde": self.ui.spHT.value(),
            "horas_extras": self.ui.spHE.value(),
            "comentario": self.ui.txtComent.text().strip(),
            "creado_por": Sesion().usuario.id_usuario,
        }
        filas = []
        for id_emp in ids:
            f = dict(base)
            f["id_empleado"] = id_emp
            filas.append(f)

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
