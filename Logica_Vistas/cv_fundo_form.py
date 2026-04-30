"""Vista de Datos del Fundo. Editable solo para administradores."""
from __future__ import annotations

from PySide6.QtWidgets import QMessageBox, QWidget

from Vistas.usuarios.ui_fundo_form import Ui_FundoForm
from Vistas.recursos.estilos import QSS_FORM, COLOR_SECUNDARIO, COLOR_ERROR
from Logica.cl_fundo import ClFundo
from Conexion.cn_sesion import Sesion


class CvFundoForm(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FundoForm()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_FORM)

        self._cl = ClFundo()
        self._sesion = Sesion()

        self._cargar()
        self._configurar_permisos()
        self.ui.btnGuardar.clicked.connect(self._guardar)

    def _configurar_permisos(self) -> None:
        s = self._sesion
        puede = s.puede("ADMIN_FUNDO", "editar") or s.usuario.es_admin
        for w in (self.ui.txtNombre, self.ui.txtRuc,
                  self.ui.txtDireccion, self.ui.txtTelefono):
            w.setReadOnly(not puede)
        self.ui.btnGuardar.setEnabled(puede)

    def _cargar(self) -> None:
        f = self._cl.obtener(self._sesion.usuario.id_fundo)
        if f is None:
            return
        self.ui.txtCodigo.setText(f.codigo)
        self.ui.txtNombre.setText(f.nombre)
        self.ui.txtRuc.setText(f.ruc)
        self.ui.txtDireccion.setText(f.direccion)
        self.ui.txtTelefono.setText(f.telefono)

    def _guardar(self) -> None:
        self.ui.lblMsg.setText("")
        try:
            self._cl.actualizar(
                self._sesion.usuario.id_fundo,
                self.ui.txtNombre.text(),
                self.ui.txtRuc.text(),
                self.ui.txtDireccion.text(),
                self.ui.txtTelefono.text(),
            )
        except ValueError as e:
            self.ui.lblMsg.setText(str(e))
            self.ui.lblMsg.setStyleSheet(f"color:{COLOR_ERROR};font-weight:bold;")
            return
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        # Refrescar nombre en la sesión
        self._sesion.nombre_fundo = self.ui.txtNombre.text().strip()
        self.ui.lblMsg.setText("Cambios guardados.")
        self.ui.lblMsg.setStyleSheet(f"color:{COLOR_SECUNDARIO};font-weight:bold;")
