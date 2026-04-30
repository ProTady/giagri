"""
Paleta de colores y rutas a recursos del aplicativo.
Basado en el logo de GIAGRI.
"""
from __future__ import annotations

from pathlib import Path

# ----- Paleta -----
COLOR_PRIMARIO     = "#0F5F5C"   # Verde teal oscuro (logo)
COLOR_PRIMARIO_HV  = "#147A77"   # Hover
COLOR_SECUNDARIO   = "#3DBA3F"   # Verde brillante (logo)
COLOR_FONDO        = "#F2F8F6"   # Fondo claro
COLOR_FONDO_INPUT  = "#FFFFFF"
COLOR_BORDE        = "#C8D6D2"
COLOR_TEXTO        = "#1F2D2C"
COLOR_TEXTO_TENUE  = "#5A6968"
COLOR_ERROR        = "#C0392B"

# ----- Recursos -----
_RAIZ = Path(__file__).resolve().parent.parent.parent
RUTA_IMAGENES = _RAIZ / "IMAGENES"
RUTA_ICONO    = RUTA_IMAGENES / "LOGOSIS.ico"
RUTA_LOGO_PNG = RUTA_IMAGENES / "LOGOAPPSINFONDO.png"


# ----- QSS reutilizables -----
QSS_LOGIN = f"""
QDialog {{ background-color: {COLOR_FONDO}; }}

QLabel#lblTitulo {{
    font-size: 24px;
    font-weight: bold;
    color: {COLOR_PRIMARIO};
    letter-spacing: 2px;
}}
QLabel#lblSub {{
    color: {COLOR_TEXTO_TENUE};
    font-size: 11px;
}}
QLabel#lblError {{
    color: {COLOR_ERROR};
    font-size: 11px;
    font-weight: bold;
}}
QLabel {{
    color: {COLOR_TEXTO};
    font-size: 12px;
}}

QLineEdit {{
    padding: 9px;
    border: 1px solid {COLOR_BORDE};
    border-radius: 6px;
    background: {COLOR_FONDO_INPUT};
    color: {COLOR_TEXTO};
    selection-background-color: {COLOR_PRIMARIO};
}}
QLineEdit:focus {{
    border: 2px solid {COLOR_PRIMARIO};
}}

QPushButton#btnIngresar {{
    background-color: {COLOR_PRIMARIO};
    color: white;
    padding: 11px;
    border-radius: 6px;
    font-weight: bold;
    border: none;
}}
QPushButton#btnIngresar:hover {{ background-color: {COLOR_PRIMARIO_HV}; }}
QPushButton#btnIngresar:pressed {{ background-color: {COLOR_SECUNDARIO}; }}
QPushButton#btnIngresar:disabled {{ background-color: #94B4B2; }}

QPushButton#btnCancelar {{
    padding: 11px;
    border: 1px solid {COLOR_BORDE};
    border-radius: 6px;
    background: {COLOR_FONDO_INPUT};
    color: {COLOR_TEXTO};
}}
QPushButton#btnCancelar:hover {{
    background: #E2EDEA;
    border-color: {COLOR_PRIMARIO};
    color: {COLOR_PRIMARIO};
}}
"""


QSS_PRINCIPAL = f"""
QMainWindow {{ background: {COLOR_FONDO}; }}

/* ===== HEADER ===== */
QFrame#frameHeader {{
    background: {COLOR_PRIMARIO};
    border-bottom: 3px solid {COLOR_SECUNDARIO};
}}
QFrame#frameHeader QLabel {{ color: white; }}
QLabel#lblLogoMini {{
    background: #FFFFFF;
    border-radius: 24px;
    padding: 4px;
}}
QLabel#lblAppNombre {{
    font-size: 18px;
    font-weight: bold;
    letter-spacing: 2px;
}}
QLabel#lblFundo {{
    font-size: 13px;
    font-weight: 600;
    padding: 4px 10px;
    background: rgba(255,255,255,0.12);
    border-radius: 4px;
}}
QLabel#lblUsuario {{
    font-size: 12px;
}}
QFrame#sepH1 {{ color: rgba(255,255,255,0.3); }}

QPushButton#btnSalir {{
    background: transparent;
    color: white;
    border: 1px solid rgba(255,255,255,0.5);
    padding: 6px 14px;
    border-radius: 4px;
    font-weight: 600;
}}
QPushButton#btnSalir:hover {{
    background: {COLOR_SECUNDARIO};
    border-color: {COLOR_SECUNDARIO};
    color: white;
}}

/* ===== MENÚ LATERAL ===== */
QFrame#frameMenu {{
    background: #FFFFFF;
    border-right: 1px solid {COLOR_BORDE};
}}
QLabel#lblMenuTitulo {{
    background: {COLOR_PRIMARIO};
    color: white;
    font-weight: bold;
    letter-spacing: 2px;
    font-size: 11px;
    qproperty-alignment: AlignVCenter;
}}

QTreeWidget#treeMenu {{
    border: none;
    background: #FFFFFF;
    color: {COLOR_TEXTO};
    font-size: 13px;
    outline: 0;
    padding: 4px 0;
}}
QTreeWidget#treeMenu::item {{
    padding: 8px 6px;
    border: none;
}}
QTreeWidget#treeMenu::item:hover {{
    background: #E8F2EF;
    color: {COLOR_PRIMARIO};
}}
QTreeWidget#treeMenu::item:selected {{
    background: {COLOR_PRIMARIO};
    color: white;
    border-radius: 0px;
}}
QTreeWidget#treeMenu::branch:has-children:!has-siblings:closed,
QTreeWidget#treeMenu::branch:closed:has-children:has-siblings {{
    image: none;
    border-image: none;
}}

/* ===== ÁREA DE CONTENIDO ===== */
QStackedWidget#stackContenido {{
    background: {COLOR_FONDO};
}}
QLabel#lblBienvenida {{
    font-size: 26px;
    font-weight: bold;
    color: {COLOR_PRIMARIO};
}}
QLabel#lblBienvenidaSub {{
    font-size: 14px;
    color: {COLOR_TEXTO_TENUE};
}}

/* ===== STATUS BAR ===== */
QStatusBar {{
    background: #FFFFFF;
    color: {COLOR_TEXTO_TENUE};
    border-top: 1px solid {COLOR_BORDE};
}}
"""


# ====================================================================
# QSS reutilizable para listas (tabla + filtros)
# ====================================================================
QSS_LISTA = f"""
QWidget {{ background: {COLOR_FONDO}; color: {COLOR_TEXTO}; }}

QLabel#lblTitulo {{
    font-size: 22px;
    font-weight: bold;
    color: {COLOR_PRIMARIO};
}}
QLabel#lblTotal {{
    color: {COLOR_TEXTO_TENUE};
    font-size: 12px;
    padding: 4px 10px;
    background: #FFFFFF;
    border: 1px solid {COLOR_BORDE};
    border-radius: 4px;
}}

QLineEdit, QComboBox {{
    padding: 7px;
    border: 1px solid {COLOR_BORDE};
    border-radius: 4px;
    background: #FFFFFF;
    selection-background-color: {COLOR_PRIMARIO};
    min-height: 18px;
}}
QLineEdit:focus, QComboBox:focus {{
    border: 2px solid {COLOR_PRIMARIO};
}}

QPushButton {{
    padding: 7px 14px;
    border-radius: 4px;
    background: #FFFFFF;
    border: 1px solid {COLOR_BORDE};
    color: {COLOR_TEXTO};
    font-weight: 600;
}}
QPushButton:hover {{
    background: #E8F2EF;
    border-color: {COLOR_PRIMARIO};
    color: {COLOR_PRIMARIO};
}}
QPushButton#btnNuevo {{
    background: {COLOR_PRIMARIO};
    color: white;
    border: none;
}}
QPushButton#btnNuevo:hover {{
    background: {COLOR_PRIMARIO_HV};
    color: white;
}}

QTableWidget {{
    background: #FFFFFF;
    border: 1px solid {COLOR_BORDE};
    border-radius: 6px;
    gridline-color: #EAEFEC;
    alternate-background-color: #F7FAF9;
    selection-background-color: {COLOR_PRIMARIO};
    selection-color: white;
}}
QTableWidget::item {{ padding: 6px; }}
QHeaderView::section {{
    background: {COLOR_PRIMARIO};
    color: white;
    padding: 8px 6px;
    border: none;
    font-weight: bold;
    font-size: 12px;
}}
"""


# ====================================================================
# QSS reutilizable para formularios (diálogos)
# ====================================================================
QSS_FORM = f"""
QDialog {{ background: {COLOR_FONDO}; }}
QLabel {{ color: {COLOR_TEXTO}; font-size: 12px; }}
QLabel#lblTitulo {{
    font-size: 18px;
    font-weight: bold;
    color: {COLOR_PRIMARIO};
}}
QLabel#lblError {{
    color: {COLOR_ERROR};
    font-size: 11px;
    font-weight: bold;
}}
QLabel#lblRolesTit {{
    font-weight: bold;
    color: {COLOR_PRIMARIO};
    margin-top: 6px;
}}
QFrame#lineSep {{ color: {COLOR_BORDE}; }}

QLineEdit, QComboBox {{
    padding: 8px;
    border: 1px solid {COLOR_BORDE};
    border-radius: 4px;
    background: #FFFFFF;
    selection-background-color: {COLOR_PRIMARIO};
}}
QLineEdit:focus, QComboBox:focus {{ border: 2px solid {COLOR_PRIMARIO}; }}
QLineEdit:read-only {{ background: #ECEFEE; color: {COLOR_TEXTO_TENUE}; }}

QCheckBox {{ spacing: 8px; }}
QCheckBox::indicator {{
    width: 16px; height: 16px;
    border: 1px solid {COLOR_BORDE};
    border-radius: 3px;
    background: #FFFFFF;
}}
QCheckBox::indicator:checked {{
    background: {COLOR_PRIMARIO};
    border-color: {COLOR_PRIMARIO};
}}

QListWidget {{
    border: 1px solid {COLOR_BORDE};
    border-radius: 4px;
    background: #FFFFFF;
    padding: 4px;
}}
QListWidget::item {{ padding: 5px; }}
QListWidget::item:selected {{ background: #E8F2EF; color: {COLOR_PRIMARIO}; }}

QPushButton {{
    padding: 8px 18px;
    border-radius: 4px;
    background: #FFFFFF;
    border: 1px solid {COLOR_BORDE};
    color: {COLOR_TEXTO};
    font-weight: 600;
}}
QPushButton:hover {{ background: #E8F2EF; color: {COLOR_PRIMARIO}; border-color: {COLOR_PRIMARIO}; }}
QPushButton#btnGuardar {{
    background: {COLOR_PRIMARIO};
    color: white;
    border: none;
}}
QPushButton#btnGuardar:hover {{ background: {COLOR_PRIMARIO_HV}; }}
"""
