# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_lotes_lista.ui'
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

class Ui_LotesLista(object):
    def setupUi(self, LotesLista):
        if not LotesLista.objectName():
            LotesLista.setObjectName(u"LotesLista")
        LotesLista.resize(1100, 620)
        self.lytRoot = QVBoxLayout(LotesLista)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lytTit = QHBoxLayout()
        self.lytTit.setObjectName(u"lytTit")
        self.lblTitulo = QLabel(LotesLista)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytTit.addWidget(self.lblTitulo)

        self.spT = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytTit.addItem(self.spT)

        self.lblTotal = QLabel(LotesLista)
        self.lblTotal.setObjectName(u"lblTotal")

        self.lytTit.addWidget(self.lblTotal)


        self.lytRoot.addLayout(self.lytTit)

        self.lytFil = QHBoxLayout()
        self.lytFil.setSpacing(10)
        self.lytFil.setObjectName(u"lytFil")
        self.txtBuscar = QLineEdit(LotesLista)
        self.txtBuscar.setObjectName(u"txtBuscar")
        self.txtBuscar.setMinimumSize(QSize(320, 0))

        self.lytFil.addWidget(self.txtBuscar)

        self.cboEstado = QComboBox(LotesLista)
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.setObjectName(u"cboEstado")

        self.lytFil.addWidget(self.cboEstado)

        self.spF = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytFil.addItem(self.spF)

        self.btnNuevo = QPushButton(LotesLista)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnNuevo)

        self.btnEditar = QPushButton(LotesLista)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(LotesLista)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnEliminar)


        self.lytRoot.addLayout(self.lytFil)

        self.tblLotes = QTableWidget(LotesLista)
        self.tblLotes.setObjectName(u"tblLotes")

        self.lytRoot.addWidget(self.tblLotes)


        self.retranslateUi(LotesLista)

        QMetaObject.connectSlotsByName(LotesLista)
    # setupUi

    def retranslateUi(self, LotesLista):
        self.lblTitulo.setText(QCoreApplication.translate("LotesLista", u"Lotes", None))
        self.lblTotal.setText(QCoreApplication.translate("LotesLista", u"0 lotes \u2014 0.0 ha", None))
        self.txtBuscar.setPlaceholderText(QCoreApplication.translate("LotesLista", u"Buscar por c\u00f3digo o nombre...", None))
        self.cboEstado.setItemText(0, QCoreApplication.translate("LotesLista", u"Todos los estados", None))
        self.cboEstado.setItemText(1, QCoreApplication.translate("LotesLista", u"Activo", None))
        self.cboEstado.setItemText(2, QCoreApplication.translate("LotesLista", u"En desarrollo", None))
        self.cboEstado.setItemText(3, QCoreApplication.translate("LotesLista", u"Inactivo", None))
        self.cboEstado.setItemText(4, QCoreApplication.translate("LotesLista", u"Erradicado", None))

        self.btnNuevo.setText(QCoreApplication.translate("LotesLista", u"+ Nuevo Lote", None))
        self.btnEditar.setText(QCoreApplication.translate("LotesLista", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("LotesLista", u"Eliminar", None))
        pass
    # retranslateUi

