# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_tareo_diario.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_TareoDiario(object):
    def setupUi(self, TareoDiario):
        if not TareoDiario.objectName():
            TareoDiario.setObjectName(u"TareoDiario")
        TareoDiario.resize(1280, 660)
        self.lytRoot = QVBoxLayout(TareoDiario)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lytTit = QHBoxLayout()
        self.lytTit.setObjectName(u"lytTit")
        self.lblTitulo = QLabel(TareoDiario)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytTit.addWidget(self.lblTitulo)

        self.spT = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytTit.addItem(self.spT)

        self.lblTotales = QLabel(TareoDiario)
        self.lblTotales.setObjectName(u"lblTotales")

        self.lytTit.addWidget(self.lblTotales)


        self.lytRoot.addLayout(self.lytTit)

        self.lytFil = QHBoxLayout()
        self.lytFil.setSpacing(10)
        self.lytFil.setObjectName(u"lytFil")
        self.lblFecha = QLabel(TareoDiario)
        self.lblFecha.setObjectName(u"lblFecha")

        self.lytFil.addWidget(self.lblFecha)

        self.dtFecha = QDateEdit(TareoDiario)
        self.dtFecha.setObjectName(u"dtFecha")
        self.dtFecha.setCalendarPopup(True)

        self.lytFil.addWidget(self.dtFecha)

        self.btnHoy = QPushButton(TareoDiario)
        self.btnHoy.setObjectName(u"btnHoy")
        self.btnHoy.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnHoy)

        self.btnAyer = QPushButton(TareoDiario)
        self.btnAyer.setObjectName(u"btnAyer")
        self.btnAyer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnAyer)

        self.spF = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytFil.addItem(self.spF)

        self.btnNuevo = QPushButton(TareoDiario)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnNuevo)

        self.btnDuplicar = QPushButton(TareoDiario)
        self.btnDuplicar.setObjectName(u"btnDuplicar")
        self.btnDuplicar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnDuplicar)

        self.btnEditar = QPushButton(TareoDiario)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(TareoDiario)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFil.addWidget(self.btnEliminar)


        self.lytRoot.addLayout(self.lytFil)

        self.tblTareo = QTableWidget(TareoDiario)
        self.tblTareo.setObjectName(u"tblTareo")

        self.lytRoot.addWidget(self.tblTareo)


        self.retranslateUi(TareoDiario)

        QMetaObject.connectSlotsByName(TareoDiario)
    # setupUi

    def retranslateUi(self, TareoDiario):
        self.lblTitulo.setText(QCoreApplication.translate("TareoDiario", u"Tareo Diario", None))
        self.lblTotales.setText(QCoreApplication.translate("TareoDiario", u"Total horas: --  \u00b7  Personas: --  \u00b7  Bono: --", None))
        self.lblFecha.setText(QCoreApplication.translate("TareoDiario", u"Fecha:", None))
        self.dtFecha.setDisplayFormat(QCoreApplication.translate("TareoDiario", u"dd/MM/yyyy", None))
        self.btnHoy.setText(QCoreApplication.translate("TareoDiario", u"Hoy", None))
        self.btnAyer.setText(QCoreApplication.translate("TareoDiario", u"Ayer", None))
        self.btnNuevo.setText(QCoreApplication.translate("TareoDiario", u"+ Nueva fila", None))
        self.btnDuplicar.setText(QCoreApplication.translate("TareoDiario", u"Duplicar", None))
        self.btnEditar.setText(QCoreApplication.translate("TareoDiario", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("TareoDiario", u"Eliminar", None))
        pass
    # retranslateUi

