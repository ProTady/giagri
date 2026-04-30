"""Diálogo crear/editar lote."""
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog

from Vistas.lotes.ui_lote_form import Ui_LoteForm
from Vistas.recursos.estilos import QSS_FORM, RUTA_ICONO
from Logica.cl_lote import ClLote
from Logica.cl_tipo_cultivo import ClTipoCultivo
from Logica.cl_variedad import ClVariedad
from Logica.cl_patron import ClPatron


class CvLoteForm(QDialog):
    def __init__(self, id_fundo: int, id_lote: Optional[int] = None,
                 parent=None):
        super().__init__(parent)
        self.ui = Ui_LoteForm()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_FORM)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))

        self._id_fundo = id_fundo
        self._id_lote = id_lote
        self._cl = ClLote()
        self._cl_var = ClVariedad()
        self._cl_pat = ClPatron()

        self._cargar_cultivos()
        self.ui.cboCultivo.currentIndexChanged.connect(
            self._on_cultivo_cambiado
        )
        self.ui.chkFs.toggled.connect(self.ui.dtSiembra.setEnabled)
        self.ui.chkFp.toggled.connect(self.ui.dtProd.setEnabled)
        self.ui.spHa.valueChanged.connect(self._recalcular_total)
        self.ui.spDens.valueChanged.connect(self._recalcular_total)

        self.ui.btnGuardar.clicked.connect(self._guardar)
        self.ui.btnCancelar.clicked.connect(self.reject)

        self._configurar_modo()

    # ------------------------------------------------------------------
    def _cargar_cultivos(self) -> None:
        self.ui.cboCultivo.clear()
        self.ui.cboCultivo.addItem("(ninguno)", None)
        for t in ClTipoCultivo().listar(self._id_fundo):
            self.ui.cboCultivo.addItem(t.nombre, t.id_tipo_cultivo)
        self._cargar_variedades_y_patrones(None)

    def _cargar_variedades_y_patrones(self, id_tipo: Optional[int]) -> None:
        self.ui.cboVariedad.clear()
        self.ui.cboPatron.clear()
        self.ui.cboVariedad.addItem("(ninguna)", None)
        self.ui.cboPatron.addItem("(ninguno)", None)
        if id_tipo is None:
            return
        for v in self._cl_var.listar(self._id_fundo, id_tipo):
            self.ui.cboVariedad.addItem(v.nombre, v.id_variedad)
        for p in self._cl_pat.listar(self._id_fundo, id_tipo):
            self.ui.cboPatron.addItem(p.nombre, p.id_patron)

    def _on_cultivo_cambiado(self, _idx: int) -> None:
        self._cargar_variedades_y_patrones(self.ui.cboCultivo.currentData())

    def _recalcular_total(self) -> None:
        ha = self.ui.spHa.value()
        dens = self.ui.spDens.value()
        if ha and dens:
            self.ui.spTotal.setValue(int(ha * dens))

    # ------------------------------------------------------------------
    def _configurar_modo(self) -> None:
        hoy = QDate.currentDate()
        self.ui.dtSiembra.setDate(hoy)
        self.ui.dtProd.setDate(hoy)

        if self._id_lote is None:
            self.ui.lblTitulo.setText("Nuevo Lote")
            self.setWindowTitle("Nuevo Lote")
            return

        self.ui.lblTitulo.setText("Editar Lote")
        self.setWindowTitle("Editar Lote")
        d = self._cl.obtener(self._id_lote)
        if d is None:
            return

        self.ui.txtCodigo.setText(d["codigo"])
        self.ui.txtNombre.setText(d["nombre"])

        self._sel_data(self.ui.cboCultivo, d["id_tipo_cultivo"])
        self._cargar_variedades_y_patrones(d["id_tipo_cultivo"])
        self._sel_data(self.ui.cboVariedad, d["id_variedad"])
        self._sel_data(self.ui.cboPatron, d["id_patron"])
        self._sel_text(self.ui.cboEstado, d["estado"])

        if d["hectareas"] is not None:
            self.ui.spHa.setValue(float(d["hectareas"]))
        if d["fecha_siembra"]:
            self.ui.chkFs.setChecked(True)
            self.ui.dtSiembra.setDate(QDate(d["fecha_siembra"]))
        if d["fecha_inicio_produccion"]:
            self.ui.chkFp.setChecked(True)
            self.ui.dtProd.setDate(QDate(d["fecha_inicio_produccion"]))
        if d["densidad_plantas"]:
            self.ui.spDens.setValue(d["densidad_plantas"])
        if d["total_plantas"]:
            self.ui.spTotal.setValue(d["total_plantas"])
        if d["distancia_entre_plantas"]:
            self.ui.spDistP.setValue(float(d["distancia_entre_plantas"]))
        if d["distancia_entre_filas"]:
            self.ui.spDistF.setValue(float(d["distancia_entre_filas"]))
        if d["sistema_riego"]:
            self._sel_text(self.ui.cboRiego, d["sistema_riego"])
        self.ui.txtObs.setPlainText(d["observaciones"])

    @staticmethod
    def _sel_data(cbo, valor) -> None:
        if valor is None:
            cbo.setCurrentIndex(0)
            return
        for i in range(cbo.count()):
            if cbo.itemData(i) == valor:
                cbo.setCurrentIndex(i)
                return

    @staticmethod
    def _sel_text(cbo, txt: str) -> None:
        if not txt:
            return
        idx = cbo.findText(txt)
        if idx >= 0:
            cbo.setCurrentIndex(idx)

    # ------------------------------------------------------------------
    def _recolectar(self) -> dict:
        riego = self.ui.cboRiego.currentText()
        if riego.startswith("("):
            riego = None
        return {
            "id_fundo": self._id_fundo,
            "codigo": self.ui.txtCodigo.text().strip(),
            "nombre": self.ui.txtNombre.text().strip(),
            "id_tipo_cultivo": self.ui.cboCultivo.currentData(),
            "id_variedad": self.ui.cboVariedad.currentData(),
            "id_patron": self.ui.cboPatron.currentData(),
            "hectareas": self.ui.spHa.value(),
            "fecha_siembra": (self.ui.dtSiembra.date().toPython()
                              if self.ui.chkFs.isChecked() else None),
            "fecha_inicio_produccion": (self.ui.dtProd.date().toPython()
                                        if self.ui.chkFp.isChecked() else None),
            "densidad_plantas": self.ui.spDens.value() or None,
            "total_plantas": self.ui.spTotal.value() or None,
            "distancia_entre_plantas": self.ui.spDistP.value() or None,
            "distancia_entre_filas": self.ui.spDistF.value() or None,
            "sistema_riego": riego,
            "estado": self.ui.cboEstado.currentText(),
            "observaciones": self.ui.txtObs.toPlainText().strip(),
        }

    def _guardar(self) -> None:
        self.ui.lblError.setText("")
        datos = self._recolectar()
        try:
            if self._id_lote is None:
                self._cl.crear(datos)
            else:
                self._cl.actualizar(self._id_lote, datos)
        except ValueError as e:
            self.ui.lblError.setText(str(e))
            return
        except Exception as e:
            self.ui.lblError.setText(f"Error: {e}")
            return
        self.accept()
