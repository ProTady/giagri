"""
Controlador de la ventana principal.
Construye el menú dinámicamente según los permisos del usuario.
"""
from __future__ import annotations

from typing import Optional

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import (
    QLabel, QMainWindow, QMessageBox, QTreeWidgetItem, QVBoxLayout, QWidget,
)

from Vistas.main.ui_principal import Ui_VentanaPrincipal
from Vistas.recursos.estilos import (
    QSS_PRINCIPAL, RUTA_ICONO, RUTA_LOGO_PNG, COLOR_PRIMARIO, COLOR_TEXTO_TENUE,
)
from Logica.cl_permisos import ClPermisos, Modulo
from Conexion.cn_sesion import Sesion
from version import __version__


ROL_CODIGO = Qt.ItemDataRole.UserRole + 1


class CvPrincipal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_VentanaPrincipal()
        self.ui.setupUi(self)
        self.setStyleSheet(QSS_PRINCIPAL)

        if RUTA_ICONO.exists():
            self.setWindowIcon(QIcon(str(RUTA_ICONO)))
        if RUTA_LOGO_PNG.exists():
            pix = QPixmap(str(RUTA_LOGO_PNG))
            self.ui.lblLogoMini.setPixmap(
                pix.scaledToHeight(40, Qt.SmoothTransformation)
            )
            self.ui.lblLogoMini.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._sesion = Sesion()
        self._cl_permisos = ClPermisos()

        # Cache de páginas ya creadas: { codigo_modulo: indice_stack }
        self._paginas: dict[str, int] = {}

        self._poblar_header()
        self._poblar_menu()

        self.ui.btnSalir.clicked.connect(self._cerrar_sesion)
        self.ui.treeMenu.itemClicked.connect(self._on_menu_click)

        self.ui.statusbar.showMessage(
            f"GIAGRI v{__version__}   ·   Conectado a {self._sesion.nombre_fundo}"
        )

    # ------------------------------------------------------------------
    def _poblar_header(self) -> None:
        u = self._sesion.usuario
        self.ui.lblFundo.setText(f"  {self._sesion.nombre_fundo}  ")
        rol = "Administrador" if u.es_admin else "Usuario"
        self.ui.lblUsuario.setText(f"{u.nombre_completo}  ·  {rol}")

    def _poblar_menu(self) -> None:
        arbol = self._cl_permisos.arbol_modulos_visibles(
            self._sesion.modulos_permitidos
        )
        self.ui.treeMenu.clear()
        for raiz in arbol:
            item = self._crear_item(raiz)
            self.ui.treeMenu.addTopLevelItem(item)
        self.ui.treeMenu.expandAll()

    def _crear_item(self, modulo: Modulo) -> QTreeWidgetItem:
        item = QTreeWidgetItem([modulo.nombre])
        item.setData(0, ROL_CODIGO, modulo.codigo)
        for hijo in modulo.hijos:
            item.addChild(self._crear_item(hijo))
        return item

    # ------------------------------------------------------------------
    def _on_menu_click(self, item: QTreeWidgetItem, _col: int) -> None:
        # Si tiene hijos, sólo expande/colapsa
        if item.childCount() > 0:
            item.setExpanded(not item.isExpanded())
            return
        codigo = item.data(0, ROL_CODIGO)
        if not codigo:
            return
        self._abrir_modulo(codigo, item.text(0))

    def _abrir_modulo(self, codigo: str, nombre: str) -> None:
        if codigo in self._paginas:
            self.ui.stackContenido.setCurrentIndex(self._paginas[codigo])
            return

        try:
            pagina = self._instanciar_modulo(codigo, nombre)
        except Exception as e:
            import traceback, logging
            tb = traceback.format_exc()
            logging.error("Error abriendo módulo %s:\n%s", codigo, tb)
            print(f"\n[ERROR módulo {codigo}]\n{tb}\n")
            QMessageBox.critical(
                self, f"Error al abrir {nombre}",
                f"<b>{type(e).__name__}:</b> {e}\n\nRevisa la consola/log para detalles."
            )
            return

        idx = self.ui.stackContenido.addWidget(pagina)
        self._paginas[codigo] = idx
        self.ui.stackContenido.setCurrentIndex(idx)

    def _instanciar_modulo(self, codigo: str, nombre: str) -> QWidget:
        """Mapea código de módulo -> widget. Si no está implementado, placeholder."""
        if codigo == "ADMIN_USUARIOS":
            from Logica_Vistas.cv_usuarios_lista import CvUsuariosLista
            return CvUsuariosLista()
        if codigo == "ADMIN_ROLES":
            from Logica_Vistas.cv_roles import CvRoles
            return CvRoles()
        if codigo == "PERSONAL_LISTA":
            from Logica_Vistas.cv_empleados_lista import CvEmpleadosLista
            return CvEmpleadosLista()
        if codigo == "LOTES_LISTA":
            from Logica_Vistas.cv_lotes_lista import CvLotesLista
            return CvLotesLista()
        if codigo in ("LOTES_CULTIVOS", "LOTES_VARIEDADES", "LOTES_PATRONES"):
            from Logica_Vistas.cv_catalogos_agricolas import CvCatalogosAgricolas
            w = CvCatalogosAgricolas()
            indice = {"LOTES_CULTIVOS": 0,
                      "LOTES_VARIEDADES": 1,
                      "LOTES_PATRONES": 2}.get(codigo, 0)
            w.ui.tabs.setCurrentIndex(indice)
            return w
        if codigo in ("PERSONAL_CARGOS", "PERSONAL_AREAS"):
            from Logica_Vistas.cv_catalogos_personal import CvCatalogosPersonal
            w = CvCatalogosPersonal()
            indice = {"PERSONAL_CARGOS": 0,
                      "PERSONAL_AREAS": 1}.get(codigo, 0)
            w.ui.tabs.setCurrentIndex(indice)
            return w
        if codigo == "ADMIN_FUNDO":
            from Logica_Vistas.cv_fundo_form import CvFundoForm
            return CvFundoForm()
        return self._crear_placeholder(codigo, nombre)

    def _crear_placeholder(self, codigo: str, nombre: str) -> QWidget:
        w = QWidget()
        lyt = QVBoxLayout(w)
        lyt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo = QLabel(nombre)
        titulo.setStyleSheet(
            f"font-size:24px; font-weight:bold; color:{COLOR_PRIMARIO};"
        )
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sub = QLabel(f"Módulo: {codigo}\n\n(En construcción)")
        sub.setStyleSheet(f"font-size:13px; color:{COLOR_TEXTO_TENUE};")
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lyt.addWidget(titulo)
        lyt.addWidget(sub)
        return w

    # ------------------------------------------------------------------
    def _cerrar_sesion(self) -> None:
        r = QMessageBox.question(
            self, "Cerrar sesión",
            "¿Seguro que deseas cerrar la sesión?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
        )
        if r == QMessageBox.StandardButton.Yes:
            Sesion().cerrar()
            self.close()
