# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_catalogos_tareo.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_CatalogosTareo(object):
    def setupUi(self, CatalogosTareo):
        if not CatalogosTareo.objectName():
            CatalogosTareo.setObjectName(u"CatalogosTareo")
        CatalogosTareo.resize(1000, 620)
        self.lytRoot = QVBoxLayout(CatalogosTareo)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lblTitulo = QLabel(CatalogosTareo)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.tabs = QTabWidget(CatalogosTareo)
        self.tabs.setObjectName(u"tabs")
        self.tabAct = QWidget()
        self.tabAct.setObjectName(u"tabAct")
        self.lytA = QVBoxLayout(self.tabAct)
        self.lytA.setObjectName(u"lytA")
        self.lytFA = QHBoxLayout()
        self.lytFA.setSpacing(8)
        self.lytFA.setObjectName(u"lytFA")
        self.laN = QLabel(self.tabAct)
        self.laN.setObjectName(u"laN")

        self.lytFA.addWidget(self.laN)

        self.txtActNombre = QLineEdit(self.tabAct)
        self.txtActNombre.setObjectName(u"txtActNombre")

        self.lytFA.addWidget(self.txtActNombre)

        self.laD = QLabel(self.tabAct)
        self.laD.setObjectName(u"laD")

        self.lytFA.addWidget(self.laD)

        self.txtActDesc = QLineEdit(self.tabAct)
        self.txtActDesc.setObjectName(u"txtActDesc")

        self.lytFA.addWidget(self.txtActDesc)

        self.btnActAgregar = QPushButton(self.tabAct)
        self.btnActAgregar.setObjectName(u"btnActAgregar")
        self.btnActAgregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFA.addWidget(self.btnActAgregar)


        self.lytA.addLayout(self.lytFA)

        self.tblActividades = QTableWidget(self.tabAct)
        self.tblActividades.setObjectName(u"tblActividades")

        self.lytA.addWidget(self.tblActividades)

        self.lytBA = QHBoxLayout()
        self.lytBA.setObjectName(u"lytBA")
        self.spA = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBA.addItem(self.spA)

        self.btnActEditar = QPushButton(self.tabAct)
        self.btnActEditar.setObjectName(u"btnActEditar")
        self.btnActEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBA.addWidget(self.btnActEditar)

        self.btnActEliminar = QPushButton(self.tabAct)
        self.btnActEliminar.setObjectName(u"btnActEliminar")
        self.btnActEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBA.addWidget(self.btnActEliminar)


        self.lytA.addLayout(self.lytBA)

        self.tabs.addTab(self.tabAct, "")
        self.tabLab = QWidget()
        self.tabLab.setObjectName(u"tabLab")
        self.lytL = QVBoxLayout(self.tabLab)
        self.lytL.setObjectName(u"lytL")
        self.lytFL = QHBoxLayout()
        self.lytFL.setSpacing(8)
        self.lytFL.setObjectName(u"lytFL")
        self.lpA = QLabel(self.tabLab)
        self.lpA.setObjectName(u"lpA")

        self.lytFL.addWidget(self.lpA)

        self.cboLabActividad = QComboBox(self.tabLab)
        self.cboLabActividad.setObjectName(u"cboLabActividad")

        self.lytFL.addWidget(self.cboLabActividad)

        self.lpN = QLabel(self.tabLab)
        self.lpN.setObjectName(u"lpN")

        self.lytFL.addWidget(self.lpN)

        self.txtLabNombre = QLineEdit(self.tabLab)
        self.txtLabNombre.setObjectName(u"txtLabNombre")

        self.lytFL.addWidget(self.txtLabNombre)

        self.lpB = QLabel(self.tabLab)
        self.lpB.setObjectName(u"lpB")

        self.lytFL.addWidget(self.lpB)

        self.spLabBono = QDoubleSpinBox(self.tabLab)
        self.spLabBono.setObjectName(u"spLabBono")
        self.spLabBono.setMaximum(9999.989999999999782)
        self.spLabBono.setDecimals(2)

        self.lytFL.addWidget(self.spLabBono)

        self.btnLabAgregar = QPushButton(self.tabLab)
        self.btnLabAgregar.setObjectName(u"btnLabAgregar")
        self.btnLabAgregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFL.addWidget(self.btnLabAgregar)


        self.lytL.addLayout(self.lytFL)

        self.lytFiltL = QHBoxLayout()
        self.lytFiltL.setObjectName(u"lytFiltL")
        self.lFil = QLabel(self.tabLab)
        self.lFil.setObjectName(u"lFil")

        self.lytFiltL.addWidget(self.lFil)

        self.cboLabFiltro = QComboBox(self.tabLab)
        self.cboLabFiltro.setObjectName(u"cboLabFiltro")

        self.lytFiltL.addWidget(self.cboLabFiltro)

        self.spLF = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytFiltL.addItem(self.spLF)


        self.lytL.addLayout(self.lytFiltL)

        self.tblLabores = QTableWidget(self.tabLab)
        self.tblLabores.setObjectName(u"tblLabores")

        self.lytL.addWidget(self.tblLabores)

        self.lytBL = QHBoxLayout()
        self.lytBL.setObjectName(u"lytBL")
        self.spL = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBL.addItem(self.spL)

        self.btnLabEditar = QPushButton(self.tabLab)
        self.btnLabEditar.setObjectName(u"btnLabEditar")
        self.btnLabEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBL.addWidget(self.btnLabEditar)

        self.btnLabEliminar = QPushButton(self.tabLab)
        self.btnLabEliminar.setObjectName(u"btnLabEliminar")
        self.btnLabEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBL.addWidget(self.btnLabEliminar)


        self.lytL.addLayout(self.lytBL)

        self.tabs.addTab(self.tabLab, "")

        self.lytRoot.addWidget(self.tabs)


        self.retranslateUi(CatalogosTareo)

        QMetaObject.connectSlotsByName(CatalogosTareo)
    # setupUi

    def retranslateUi(self, CatalogosTareo):
        self.lblTitulo.setText(QCoreApplication.translate("CatalogosTareo", u"Cat\u00e1logos de Tareo", None))
        self.laN.setText(QCoreApplication.translate("CatalogosTareo", u"Nombre:", None))
        self.txtActNombre.setPlaceholderText(QCoreApplication.translate("CatalogosTareo", u"Ej: Riego", None))
        self.laD.setText(QCoreApplication.translate("CatalogosTareo", u"Descripci\u00f3n:", None))
        self.btnActAgregar.setText(QCoreApplication.translate("CatalogosTareo", u"+ Agregar", None))
        self.btnActEditar.setText(QCoreApplication.translate("CatalogosTareo", u"Editar selecci\u00f3n", None))
        self.btnActEliminar.setText(QCoreApplication.translate("CatalogosTareo", u"Eliminar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabAct), QCoreApplication.translate("CatalogosTareo", u"Actividades", None))
        self.lpA.setText(QCoreApplication.translate("CatalogosTareo", u"Actividad:", None))
        self.lpN.setText(QCoreApplication.translate("CatalogosTareo", u"Nombre:", None))
        self.txtLabNombre.setPlaceholderText(QCoreApplication.translate("CatalogosTareo", u"Ej: Cosecha de palto", None))
        self.lpB.setText(QCoreApplication.translate("CatalogosTareo", u"Bono S/. /h:", None))
        self.btnLabAgregar.setText(QCoreApplication.translate("CatalogosTareo", u"+ Agregar", None))
        self.lFil.setText(QCoreApplication.translate("CatalogosTareo", u"Filtrar por actividad:", None))
        self.btnLabEditar.setText(QCoreApplication.translate("CatalogosTareo", u"Editar selecci\u00f3n", None))
        self.btnLabEliminar.setText(QCoreApplication.translate("CatalogosTareo", u"Eliminar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabLab), QCoreApplication.translate("CatalogosTareo", u"Labores y Bonos", None))
        pass
    # retranslateUi

