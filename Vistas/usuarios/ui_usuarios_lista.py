# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_usuarios_lista.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_UsuariosLista(object):
    def setupUi(self, UsuariosLista):
        if not UsuariosLista.objectName():
            UsuariosLista.setObjectName(u"UsuariosLista")
        UsuariosLista.resize(1000, 620)
        self.lytRoot = QVBoxLayout(UsuariosLista)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lytTitulo = QHBoxLayout()
        self.lytTitulo.setObjectName(u"lytTitulo")
        self.lblTitulo = QLabel(UsuariosLista)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytTitulo.addWidget(self.lblTitulo)

        self.spT = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytTitulo.addItem(self.spT)

        self.lblTotal = QLabel(UsuariosLista)
        self.lblTotal.setObjectName(u"lblTotal")

        self.lytTitulo.addWidget(self.lblTotal)


        self.lytRoot.addLayout(self.lytTitulo)

        self.lytFiltros = QHBoxLayout()
        self.lytFiltros.setSpacing(10)
        self.lytFiltros.setObjectName(u"lytFiltros")
        self.txtBuscar = QLineEdit(UsuariosLista)
        self.txtBuscar.setObjectName(u"txtBuscar")
        self.txtBuscar.setMinimumSize(QSize(320, 0))

        self.lytFiltros.addWidget(self.txtBuscar)

        self.cboEstado = QComboBox(UsuariosLista)
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.setObjectName(u"cboEstado")

        self.lytFiltros.addWidget(self.cboEstado)

        self.spF = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytFiltros.addItem(self.spF)

        self.btnNuevo = QPushButton(UsuariosLista)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFiltros.addWidget(self.btnNuevo)

        self.btnEditar = QPushButton(UsuariosLista)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFiltros.addWidget(self.btnEditar)

        self.btnResetClave = QPushButton(UsuariosLista)
        self.btnResetClave.setObjectName(u"btnResetClave")
        self.btnResetClave.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFiltros.addWidget(self.btnResetClave)

        self.btnActivar = QPushButton(UsuariosLista)
        self.btnActivar.setObjectName(u"btnActivar")
        self.btnActivar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFiltros.addWidget(self.btnActivar)


        self.lytRoot.addLayout(self.lytFiltros)

        self.tblUsuarios = QTableWidget(UsuariosLista)
        self.tblUsuarios.setObjectName(u"tblUsuarios")

        self.lytRoot.addWidget(self.tblUsuarios)


        self.retranslateUi(UsuariosLista)

        QMetaObject.connectSlotsByName(UsuariosLista)
    # setupUi

    def retranslateUi(self, UsuariosLista):
        self.lblTitulo.setText(QCoreApplication.translate("UsuariosLista", u"Gesti\u00f3n de Usuarios", None))
        self.lblTotal.setText(QCoreApplication.translate("UsuariosLista", u"0 usuarios", None))
        self.txtBuscar.setPlaceholderText(QCoreApplication.translate("UsuariosLista", u"Buscar por usuario, nombre o correo...", None))
        self.cboEstado.setItemText(0, QCoreApplication.translate("UsuariosLista", u"Todos", None))
        self.cboEstado.setItemText(1, QCoreApplication.translate("UsuariosLista", u"Activos", None))
        self.cboEstado.setItemText(2, QCoreApplication.translate("UsuariosLista", u"Inactivos", None))

        self.btnNuevo.setText(QCoreApplication.translate("UsuariosLista", u"+ Nuevo Usuario", None))
        self.btnEditar.setText(QCoreApplication.translate("UsuariosLista", u"Editar", None))
        self.btnResetClave.setText(QCoreApplication.translate("UsuariosLista", u"Resetear contrase\u00f1a", None))
        self.btnActivar.setText(QCoreApplication.translate("UsuariosLista", u"Activar/Desactivar", None))
        pass
    # retranslateUi

