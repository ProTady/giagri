"""Diálogo crear/editar empleado."""
from __future__ import annotations

from datetime import date
from typing import Optional

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from Vistas.personal.ui_empleado_form import Ui_EmpleadoForm
from Vistas.recursos.estilos import QSS_FORM, RUTA_ICONO
from Logica.cl_empleado import ClEmpleado
from Logica.cl_cargo import ClCargo
from Logica.cl_area_trabajo import ClAreaTrabajo


class CvEmpleadoForm(QDialog):
    def __init__(self, id_fundo: int, id_empleado: Optional[int] = None,
                 parent=None):
        super().__init__(parent)
        self.ui = Ui_EmpleadoForm()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_FORM)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))

        self._id_fundo = id_fundo
        self._id_empleado = id_empleado
        self._cl = ClEmpleado()

        self._cargar_combos()
        self._configurar_modo()

        self.ui.chkCese.toggled.connect(self.ui.dtCese.setEnabled)
        self.ui.btnGuardar.clicked.connect(self._guardar)
        self.ui.btnCancelar.clicked.connect(self.reject)

    # ------------------------------------------------------------------
    def _cargar_combos(self) -> None:
        self.ui.cboCargo.clear()
        self.ui.cboCargo.addItem("(ninguno)", None)
        for c in ClCargo().listar(self._id_fundo):
            self.ui.cboCargo.addItem(c.nombre, c.id_cargo)

        self.ui.cboArea.clear()
        self.ui.cboArea.addItem("(ninguna)", None)
        for a in ClAreaTrabajo().listar(self._id_fundo):
            self.ui.cboArea.addItem(a.nombre, a.id_area)

    def _configurar_modo(self) -> None:
        hoy = QDate.currentDate()
        self.ui.dtNac.setDate(hoy.addYears(-30))
        self.ui.dtIngreso.setDate(hoy)
        self.ui.dtCese.setDate(hoy)

        if self._id_empleado is None:
            self.ui.lblTitulo.setText("Nuevo Empleado")
            self.setWindowTitle("Nuevo Empleado")
            # Sugerir el siguiente código
            try:
                sugerido = self._cl.siguiente_codigo(self._id_fundo)
                self.ui.txtCodigo.setText(sugerido)
                self.ui.txtCodigo.setPlaceholderText(sugerido)
            except Exception:
                pass
            return

        self.ui.lblTitulo.setText("Editar Empleado")
        self.setWindowTitle("Editar Empleado")
        d = self._cl.obtener(self._id_empleado)
        if d is None:
            return

        self.ui.txtCodigo.setText(d["codigo"])
        self.ui.txtDni.setText(d["dni"])
        self.ui.txtApPaterno.setText(d["apellido_paterno"])
        self.ui.txtApMaterno.setText(d["apellido_materno"])
        self.ui.txtNombres.setText(d["nombres"])
        if d["fecha_nacimiento"]:
            self.ui.dtNac.setDate(QDate(d["fecha_nacimiento"]))
        self._set_combo(self.ui.cboSexo,
                        {"M": 1, "F": 2}.get(d["sexo"] or "", 0))
        self._seleccionar_texto(self.ui.cboEstadoCivil, d["estado_civil"])
        self.ui.txtDireccion.setText(d["direccion"])
        self.ui.txtTelefono.setText(d["telefono"])
        self.ui.txtCorreo.setText(d["correo"])

        self._seleccionar_data(self.ui.cboCargo, d["id_cargo"])
        self._seleccionar_data(self.ui.cboArea, d["id_area"])
        if d["fecha_ingreso"]:
            self.ui.dtIngreso.setDate(QDate(d["fecha_ingreso"]))
        if d["fecha_cese"]:
            self.ui.chkCese.setChecked(True)
            self.ui.dtCese.setDate(QDate(d["fecha_cese"]))
        self._seleccionar_texto(self.ui.cboEstado, d["estado"])
        if d["sueldo_base"]:
            self.ui.spSueldo.setValue(float(d["sueldo_base"]))
        self.ui.txtBanco.setText(d["banco"])
        self.ui.txtCuenta.setText(d["cuenta_banco"])
        self.ui.txtObs.setPlainText(d["observaciones"])
        self._seleccionar_texto(self.ui.cboRegimen, d.get("regimen") or "Agrario")

    @staticmethod
    def _set_combo(cbo, idx: int) -> None:
        if 0 <= idx < cbo.count():
            cbo.setCurrentIndex(idx)

    @staticmethod
    def _seleccionar_texto(cbo, txt: str) -> None:
        if not txt:
            cbo.setCurrentIndex(0)
            return
        idx = cbo.findText(txt)
        if idx >= 0:
            cbo.setCurrentIndex(idx)

    @staticmethod
    def _seleccionar_data(cbo, valor) -> None:
        if valor is None:
            cbo.setCurrentIndex(0)
            return
        for i in range(cbo.count()):
            if cbo.itemData(i) == valor:
                cbo.setCurrentIndex(i)
                return

    # ------------------------------------------------------------------
    def _recolectar(self) -> dict:
        sexo_idx = self.ui.cboSexo.currentIndex()
        sexo = {1: "M", 2: "F"}.get(sexo_idx)
        return {
            "id_fundo": self._id_fundo,
            "codigo": self.ui.txtCodigo.text().strip(),
            "dni": self.ui.txtDni.text().strip(),
            "apellido_paterno": self.ui.txtApPaterno.text().strip(),
            "apellido_materno": self.ui.txtApMaterno.text().strip(),
            "nombres": self.ui.txtNombres.text().strip(),
            "fecha_nacimiento": self.ui.dtNac.date().toPython(),
            "sexo": sexo,
            "estado_civil": self.ui.cboEstadoCivil.currentText().strip() or None,
            "direccion": self.ui.txtDireccion.text().strip(),
            "telefono": self.ui.txtTelefono.text().strip(),
            "correo": self.ui.txtCorreo.text().strip(),
            "fecha_ingreso": self.ui.dtIngreso.date().toPython(),
            "fecha_cese": (self.ui.dtCese.date().toPython()
                           if self.ui.chkCese.isChecked() else None),
            "estado": self.ui.cboEstado.currentText(),
            "id_cargo": self.ui.cboCargo.currentData(),
            "id_area": self.ui.cboArea.currentData(),
            "sueldo_base": self.ui.spSueldo.value() or None,
            "cuenta_banco": self.ui.txtCuenta.text().strip(),
            "banco": self.ui.txtBanco.text().strip(),
            "observaciones": self.ui.txtObs.toPlainText().strip(),
            "regimen": self.ui.cboRegimen.currentText(),
        }

    def _guardar(self) -> None:
        self.ui.lblError.setText("")
        datos = self._recolectar()
        try:
            if self._id_empleado is None:
                self._cl.crear(datos)
            else:
                self._cl.actualizar(self._id_empleado, datos)
        except ValueError as e:
            self.ui.lblError.setText(str(e))
            return
        except Exception as e:
            self.ui.lblError.setText(f"Error: {e}")
            return
        self.accept()
