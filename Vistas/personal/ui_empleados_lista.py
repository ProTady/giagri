# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_empleados_lista.ui'
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

class Ui_EmpleadosLista(object):
    def setupUi(self, EmpleadosLista):
        if not EmpleadosLista.objectName():
            EmpleadosLista.setObjectName(u"EmpleadosLista")
        EmpleadosLista.resize(1100, 620)
        self.lytRoot = QVBoxLayout(EmpleadosLista)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lytTit = QHBoxLayout()
        self.lytTit.setObjectName(u"lytTit")
        self.lblTitulo = QLabel(EmpleadosLista)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytTit.addWidget(self.lblTitulo)

        self.spT = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytTit.addItem(self.spT)

        self.lblTotal = QLabel(EmpleadosLista)
        self.lblTotal.setObjectName(u"lblTotal")

        self.lytTit.addWidget(self.lblTotal)


        self.lytRoot.addLayout(self.lytTit)

        self.lytFiltros = QHBoxLayout()
        self.lytFiltros.setSpacing(10)
        self.lytFiltros.setObjectName(u"lytFiltros")
        self.txtBuscar = QLineEdit(EmpleadosLista)
        self.txtBuscar.setObjectName(u"txtBuscar")
        self.txtBuscar.setMinimumSize(QSize(320, 0))

        self.lytFiltros.addWidget(self.txtBuscar)

        self.cboEstado = QComboBox(EmpleadosLista)
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.setObjectName(u"cboEstado")

        self.lytFiltros.addWidget(self.cboEstado)

        self.spF = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytFiltros.addItem(self.spF)

        self.btnNuevo = QPushButton(EmpleadosLista)
        self.btnNuevo.setObjectName(u"btnNuevo")
        self.btnNuevo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFiltros.addWidget(self.btnNuevo)

        self.btnEditar = QPushButton(EmpleadosLista)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFiltros.addWidget(self.btnEditar)

        self.btnEliminar = QPushButton(EmpleadosLista)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFiltros.addWidget(self.btnEliminar)


        self.lytRoot.addLayout(self.lytFiltros)

        self.tblEmpleados = QTableWidget(EmpleadosLista)
        self.tblEmpleados.setObjectName(u"tblEmpleados")

        self.lytRoot.addWidget(self.tblEmpleados)


        self.retranslateUi(EmpleadosLista)

        QMetaObject.connectSlotsByName(EmpleadosLista)
    # setupUi

    def retranslateUi(self, EmpleadosLista):
        self.lblTitulo.setText(QCoreApplication.translate("EmpleadosLista", u"Empleados", None))
        self.lblTotal.setText(QCoreApplication.translate("EmpleadosLista", u"0 empleados", None))
        self.txtBuscar.setPlaceholderText(QCoreApplication.translate("EmpleadosLista", u"Buscar por c\u00f3digo, DNI, apellidos o nombres...", None))
        self.cboEstado.setItemText(0, QCoreApplication.translate("EmpleadosLista", u"Todos los estados", None))
        self.cboEstado.setItemText(1, QCoreApplication.translate("EmpleadosLista", u"Activo", None))
        self.cboEstado.setItemText(2, QCoreApplication.translate("EmpleadosLista", u"Cesado", None))
        self.cboEstado.setItemText(3, QCoreApplication.translate("EmpleadosLista", u"Vacaciones", None))
        self.cboEstado.setItemText(4, QCoreApplication.translate("EmpleadosLista", u"Suspendido", None))

        self.btnNuevo.setText(QCoreApplication.translate("EmpleadosLista", u"+ Nuevo Empleado", None))
        self.btnEditar.setText(QCoreApplication.translate("EmpleadosLista", u"Editar", None))
        self.btnEliminar.setText(QCoreApplication.translate("EmpleadosLista", u"Eliminar", None))
        pass
    # retranslateUi

