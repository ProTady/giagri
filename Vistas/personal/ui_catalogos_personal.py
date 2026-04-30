# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_catalogos_personal.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_CatalogosPersonal(object):
    def setupUi(self, CatalogosPersonal):
        if not CatalogosPersonal.objectName():
            CatalogosPersonal.setObjectName(u"CatalogosPersonal")
        CatalogosPersonal.resize(900, 620)
        self.lytRoot = QVBoxLayout(CatalogosPersonal)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lblTitulo = QLabel(CatalogosPersonal)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.tabs = QTabWidget(CatalogosPersonal)
        self.tabs.setObjectName(u"tabs")
        self.tabCargos = QWidget()
        self.tabCargos.setObjectName(u"tabCargos")
        self.lytC = QVBoxLayout(self.tabCargos)
        self.lytC.setObjectName(u"lytC")
        self.lytFormC = QHBoxLayout()
        self.lytFormC.setSpacing(8)
        self.lytFormC.setObjectName(u"lytFormC")
        self.lcN = QLabel(self.tabCargos)
        self.lcN.setObjectName(u"lcN")

        self.lytFormC.addWidget(self.lcN)

        self.txtCargoNombre = QLineEdit(self.tabCargos)
        self.txtCargoNombre.setObjectName(u"txtCargoNombre")

        self.lytFormC.addWidget(self.txtCargoNombre)

        self.lcD = QLabel(self.tabCargos)
        self.lcD.setObjectName(u"lcD")

        self.lytFormC.addWidget(self.lcD)

        self.txtCargoDesc = QLineEdit(self.tabCargos)
        self.txtCargoDesc.setObjectName(u"txtCargoDesc")

        self.lytFormC.addWidget(self.txtCargoDesc)

        self.btnCargoAgregar = QPushButton(self.tabCargos)
        self.btnCargoAgregar.setObjectName(u"btnCargoAgregar")
        self.btnCargoAgregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFormC.addWidget(self.btnCargoAgregar)


        self.lytC.addLayout(self.lytFormC)

        self.tblCargos = QTableWidget(self.tabCargos)
        self.tblCargos.setObjectName(u"tblCargos")

        self.lytC.addWidget(self.tblCargos)

        self.lytBC = QHBoxLayout()
        self.lytBC.setObjectName(u"lytBC")
        self.spC = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBC.addItem(self.spC)

        self.btnCargoEditar = QPushButton(self.tabCargos)
        self.btnCargoEditar.setObjectName(u"btnCargoEditar")
        self.btnCargoEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBC.addWidget(self.btnCargoEditar)

        self.btnCargoEliminar = QPushButton(self.tabCargos)
        self.btnCargoEliminar.setObjectName(u"btnCargoEliminar")
        self.btnCargoEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBC.addWidget(self.btnCargoEliminar)


        self.lytC.addLayout(self.lytBC)

        self.tabs.addTab(self.tabCargos, "")
        self.tabAreas = QWidget()
        self.tabAreas.setObjectName(u"tabAreas")
        self.lytA = QVBoxLayout(self.tabAreas)
        self.lytA.setObjectName(u"lytA")
        self.lytFormA = QHBoxLayout()
        self.lytFormA.setSpacing(8)
        self.lytFormA.setObjectName(u"lytFormA")
        self.laN = QLabel(self.tabAreas)
        self.laN.setObjectName(u"laN")

        self.lytFormA.addWidget(self.laN)

        self.txtAreaNombre = QLineEdit(self.tabAreas)
        self.txtAreaNombre.setObjectName(u"txtAreaNombre")

        self.lytFormA.addWidget(self.txtAreaNombre)

        self.laD = QLabel(self.tabAreas)
        self.laD.setObjectName(u"laD")

        self.lytFormA.addWidget(self.laD)

        self.txtAreaDesc = QLineEdit(self.tabAreas)
        self.txtAreaDesc.setObjectName(u"txtAreaDesc")

        self.lytFormA.addWidget(self.txtAreaDesc)

        self.btnAreaAgregar = QPushButton(self.tabAreas)
        self.btnAreaAgregar.setObjectName(u"btnAreaAgregar")
        self.btnAreaAgregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFormA.addWidget(self.btnAreaAgregar)


        self.lytA.addLayout(self.lytFormA)

        self.tblAreas = QTableWidget(self.tabAreas)
        self.tblAreas.setObjectName(u"tblAreas")

        self.lytA.addWidget(self.tblAreas)

        self.lytBA = QHBoxLayout()
        self.lytBA.setObjectName(u"lytBA")
        self.spA = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBA.addItem(self.spA)

        self.btnAreaEditar = QPushButton(self.tabAreas)
        self.btnAreaEditar.setObjectName(u"btnAreaEditar")
        self.btnAreaEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBA.addWidget(self.btnAreaEditar)

        self.btnAreaEliminar = QPushButton(self.tabAreas)
        self.btnAreaEliminar.setObjectName(u"btnAreaEliminar")
        self.btnAreaEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBA.addWidget(self.btnAreaEliminar)


        self.lytA.addLayout(self.lytBA)

        self.tabs.addTab(self.tabAreas, "")

        self.lytRoot.addWidget(self.tabs)


        self.retranslateUi(CatalogosPersonal)

        QMetaObject.connectSlotsByName(CatalogosPersonal)
    # setupUi

    def retranslateUi(self, CatalogosPersonal):
        self.lblTitulo.setText(QCoreApplication.translate("CatalogosPersonal", u"Cat\u00e1logos de Personal", None))
        self.lcN.setText(QCoreApplication.translate("CatalogosPersonal", u"Nombre:", None))
        self.txtCargoNombre.setPlaceholderText(QCoreApplication.translate("CatalogosPersonal", u"Ej: Topiqueador", None))
        self.lcD.setText(QCoreApplication.translate("CatalogosPersonal", u"Descripci\u00f3n:", None))
        self.btnCargoAgregar.setText(QCoreApplication.translate("CatalogosPersonal", u"+ Agregar", None))
        self.btnCargoEditar.setText(QCoreApplication.translate("CatalogosPersonal", u"Editar selecci\u00f3n", None))
        self.btnCargoEliminar.setText(QCoreApplication.translate("CatalogosPersonal", u"Eliminar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabCargos), QCoreApplication.translate("CatalogosPersonal", u"Cargos", None))
        self.laN.setText(QCoreApplication.translate("CatalogosPersonal", u"Nombre:", None))
        self.txtAreaNombre.setPlaceholderText(QCoreApplication.translate("CatalogosPersonal", u"Ej: Vivero", None))
        self.laD.setText(QCoreApplication.translate("CatalogosPersonal", u"Descripci\u00f3n:", None))
        self.btnAreaAgregar.setText(QCoreApplication.translate("CatalogosPersonal", u"+ Agregar", None))
        self.btnAreaEditar.setText(QCoreApplication.translate("CatalogosPersonal", u"Editar selecci\u00f3n", None))
        self.btnAreaEliminar.setText(QCoreApplication.translate("CatalogosPersonal", u"Eliminar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabAreas), QCoreApplication.translate("CatalogosPersonal", u"\u00c1reas de Trabajo", None))
        pass
    # retranslateUi

