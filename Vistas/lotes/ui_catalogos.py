# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_catalogos.ui'
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
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_CatalogosAgricolas(object):
    def setupUi(self, CatalogosAgricolas):
        if not CatalogosAgricolas.objectName():
            CatalogosAgricolas.setObjectName(u"CatalogosAgricolas")
        CatalogosAgricolas.resize(900, 620)
        self.lytRoot = QVBoxLayout(CatalogosAgricolas)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lblTitulo = QLabel(CatalogosAgricolas)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.tabs = QTabWidget(CatalogosAgricolas)
        self.tabs.setObjectName(u"tabs")
        self.tabCultivos = QWidget()
        self.tabCultivos.setObjectName(u"tabCultivos")
        self.lytC = QVBoxLayout(self.tabCultivos)
        self.lytC.setObjectName(u"lytC")
        self.lytFormC = QHBoxLayout()
        self.lytFormC.setSpacing(8)
        self.lytFormC.setObjectName(u"lytFormC")
        self.lcN = QLabel(self.tabCultivos)
        self.lcN.setObjectName(u"lcN")

        self.lytFormC.addWidget(self.lcN)

        self.txtCultivoNombre = QLineEdit(self.tabCultivos)
        self.txtCultivoNombre.setObjectName(u"txtCultivoNombre")

        self.lytFormC.addWidget(self.txtCultivoNombre)

        self.lcSci = QLabel(self.tabCultivos)
        self.lcSci.setObjectName(u"lcSci")

        self.lytFormC.addWidget(self.lcSci)

        self.txtCultivoSci = QLineEdit(self.tabCultivos)
        self.txtCultivoSci.setObjectName(u"txtCultivoSci")

        self.lytFormC.addWidget(self.txtCultivoSci)

        self.btnCultivoAgregar = QPushButton(self.tabCultivos)
        self.btnCultivoAgregar.setObjectName(u"btnCultivoAgregar")
        self.btnCultivoAgregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFormC.addWidget(self.btnCultivoAgregar)


        self.lytC.addLayout(self.lytFormC)

        self.tblCultivos = QTableWidget(self.tabCultivos)
        self.tblCultivos.setObjectName(u"tblCultivos")

        self.lytC.addWidget(self.tblCultivos)

        self.lytBC = QHBoxLayout()
        self.lytBC.setObjectName(u"lytBC")
        self.spC = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBC.addItem(self.spC)

        self.btnCultivoEditar = QPushButton(self.tabCultivos)
        self.btnCultivoEditar.setObjectName(u"btnCultivoEditar")
        self.btnCultivoEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBC.addWidget(self.btnCultivoEditar)

        self.btnCultivoEliminar = QPushButton(self.tabCultivos)
        self.btnCultivoEliminar.setObjectName(u"btnCultivoEliminar")
        self.btnCultivoEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBC.addWidget(self.btnCultivoEliminar)


        self.lytC.addLayout(self.lytBC)

        self.tabs.addTab(self.tabCultivos, "")
        self.tabVariedades = QWidget()
        self.tabVariedades.setObjectName(u"tabVariedades")
        self.lytV = QVBoxLayout(self.tabVariedades)
        self.lytV.setObjectName(u"lytV")
        self.lytFormV = QHBoxLayout()
        self.lytFormV.setSpacing(8)
        self.lytFormV.setObjectName(u"lytFormV")
        self.lvT = QLabel(self.tabVariedades)
        self.lvT.setObjectName(u"lvT")

        self.lytFormV.addWidget(self.lvT)

        self.cboVarCultivo = QComboBox(self.tabVariedades)
        self.cboVarCultivo.setObjectName(u"cboVarCultivo")

        self.lytFormV.addWidget(self.cboVarCultivo)

        self.lvN = QLabel(self.tabVariedades)
        self.lvN.setObjectName(u"lvN")

        self.lytFormV.addWidget(self.lvN)

        self.txtVarNombre = QLineEdit(self.tabVariedades)
        self.txtVarNombre.setObjectName(u"txtVarNombre")

        self.lytFormV.addWidget(self.txtVarNombre)

        self.lvD = QLabel(self.tabVariedades)
        self.lvD.setObjectName(u"lvD")

        self.lytFormV.addWidget(self.lvD)

        self.txtVarDesc = QLineEdit(self.tabVariedades)
        self.txtVarDesc.setObjectName(u"txtVarDesc")

        self.lytFormV.addWidget(self.txtVarDesc)

        self.btnVarAgregar = QPushButton(self.tabVariedades)
        self.btnVarAgregar.setObjectName(u"btnVarAgregar")
        self.btnVarAgregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFormV.addWidget(self.btnVarAgregar)


        self.lytV.addLayout(self.lytFormV)

        self.lytFiltV = QHBoxLayout()
        self.lytFiltV.setObjectName(u"lytFiltV")
        self.lvFil = QLabel(self.tabVariedades)
        self.lvFil.setObjectName(u"lvFil")

        self.lytFiltV.addWidget(self.lvFil)

        self.cboVarFiltro = QComboBox(self.tabVariedades)
        self.cboVarFiltro.setObjectName(u"cboVarFiltro")

        self.lytFiltV.addWidget(self.cboVarFiltro)

        self.spVF = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytFiltV.addItem(self.spVF)


        self.lytV.addLayout(self.lytFiltV)

        self.tblVariedades = QTableWidget(self.tabVariedades)
        self.tblVariedades.setObjectName(u"tblVariedades")

        self.lytV.addWidget(self.tblVariedades)

        self.lytBV = QHBoxLayout()
        self.lytBV.setObjectName(u"lytBV")
        self.spV = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBV.addItem(self.spV)

        self.btnVarEditar = QPushButton(self.tabVariedades)
        self.btnVarEditar.setObjectName(u"btnVarEditar")
        self.btnVarEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBV.addWidget(self.btnVarEditar)

        self.btnVarEliminar = QPushButton(self.tabVariedades)
        self.btnVarEliminar.setObjectName(u"btnVarEliminar")
        self.btnVarEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBV.addWidget(self.btnVarEliminar)


        self.lytV.addLayout(self.lytBV)

        self.tabs.addTab(self.tabVariedades, "")
        self.tabPatrones = QWidget()
        self.tabPatrones.setObjectName(u"tabPatrones")
        self.lytP = QVBoxLayout(self.tabPatrones)
        self.lytP.setObjectName(u"lytP")
        self.lytFormP = QHBoxLayout()
        self.lytFormP.setSpacing(8)
        self.lytFormP.setObjectName(u"lytFormP")
        self.lpT = QLabel(self.tabPatrones)
        self.lpT.setObjectName(u"lpT")

        self.lytFormP.addWidget(self.lpT)

        self.cboPatCultivo = QComboBox(self.tabPatrones)
        self.cboPatCultivo.setObjectName(u"cboPatCultivo")

        self.lytFormP.addWidget(self.cboPatCultivo)

        self.lpN = QLabel(self.tabPatrones)
        self.lpN.setObjectName(u"lpN")

        self.lytFormP.addWidget(self.lpN)

        self.txtPatNombre = QLineEdit(self.tabPatrones)
        self.txtPatNombre.setObjectName(u"txtPatNombre")

        self.lytFormP.addWidget(self.txtPatNombre)

        self.lpD = QLabel(self.tabPatrones)
        self.lpD.setObjectName(u"lpD")

        self.lytFormP.addWidget(self.lpD)

        self.txtPatDesc = QLineEdit(self.tabPatrones)
        self.txtPatDesc.setObjectName(u"txtPatDesc")

        self.lytFormP.addWidget(self.txtPatDesc)

        self.btnPatAgregar = QPushButton(self.tabPatrones)
        self.btnPatAgregar.setObjectName(u"btnPatAgregar")
        self.btnPatAgregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytFormP.addWidget(self.btnPatAgregar)


        self.lytP.addLayout(self.lytFormP)

        self.lytFiltP = QHBoxLayout()
        self.lytFiltP.setObjectName(u"lytFiltP")
        self.lpFil = QLabel(self.tabPatrones)
        self.lpFil.setObjectName(u"lpFil")

        self.lytFiltP.addWidget(self.lpFil)

        self.cboPatFiltro = QComboBox(self.tabPatrones)
        self.cboPatFiltro.setObjectName(u"cboPatFiltro")

        self.lytFiltP.addWidget(self.cboPatFiltro)

        self.spPF = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytFiltP.addItem(self.spPF)


        self.lytP.addLayout(self.lytFiltP)

        self.tblPatrones = QTableWidget(self.tabPatrones)
        self.tblPatrones.setObjectName(u"tblPatrones")

        self.lytP.addWidget(self.tblPatrones)

        self.lytBP = QHBoxLayout()
        self.lytBP.setObjectName(u"lytBP")
        self.spP = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBP.addItem(self.spP)

        self.btnPatEditar = QPushButton(self.tabPatrones)
        self.btnPatEditar.setObjectName(u"btnPatEditar")
        self.btnPatEditar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBP.addWidget(self.btnPatEditar)

        self.btnPatEliminar = QPushButton(self.tabPatrones)
        self.btnPatEliminar.setObjectName(u"btnPatEliminar")
        self.btnPatEliminar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBP.addWidget(self.btnPatEliminar)


        self.lytP.addLayout(self.lytBP)

        self.tabs.addTab(self.tabPatrones, "")

        self.lytRoot.addWidget(self.tabs)


        self.retranslateUi(CatalogosAgricolas)

        QMetaObject.connectSlotsByName(CatalogosAgricolas)
    # setupUi

    def retranslateUi(self, CatalogosAgricolas):
        self.lblTitulo.setText(QCoreApplication.translate("CatalogosAgricolas", u"Cat\u00e1logos Agr\u00edcolas", None))
        self.lcN.setText(QCoreApplication.translate("CatalogosAgricolas", u"Nombre:", None))
        self.txtCultivoNombre.setPlaceholderText(QCoreApplication.translate("CatalogosAgricolas", u"Ej: C\u00edtrico", None))
        self.lcSci.setText(QCoreApplication.translate("CatalogosAgricolas", u"Nombre cient\u00edfico:", None))
        self.txtCultivoSci.setPlaceholderText(QCoreApplication.translate("CatalogosAgricolas", u"Citrus sp. (opcional)", None))
        self.btnCultivoAgregar.setText(QCoreApplication.translate("CatalogosAgricolas", u"+ Agregar", None))
        self.btnCultivoEditar.setText(QCoreApplication.translate("CatalogosAgricolas", u"Editar selecci\u00f3n", None))
        self.btnCultivoEliminar.setText(QCoreApplication.translate("CatalogosAgricolas", u"Eliminar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabCultivos), QCoreApplication.translate("CatalogosAgricolas", u"Tipos de Cultivo", None))
        self.lvT.setText(QCoreApplication.translate("CatalogosAgricolas", u"Cultivo:", None))
        self.lvN.setText(QCoreApplication.translate("CatalogosAgricolas", u"Nombre:", None))
        self.lvD.setText(QCoreApplication.translate("CatalogosAgricolas", u"Descripci\u00f3n:", None))
        self.btnVarAgregar.setText(QCoreApplication.translate("CatalogosAgricolas", u"+ Agregar", None))
        self.lvFil.setText(QCoreApplication.translate("CatalogosAgricolas", u"Filtrar por cultivo:", None))
        self.btnVarEditar.setText(QCoreApplication.translate("CatalogosAgricolas", u"Editar selecci\u00f3n", None))
        self.btnVarEliminar.setText(QCoreApplication.translate("CatalogosAgricolas", u"Eliminar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabVariedades), QCoreApplication.translate("CatalogosAgricolas", u"Variedades", None))
        self.lpT.setText(QCoreApplication.translate("CatalogosAgricolas", u"Cultivo:", None))
        self.lpN.setText(QCoreApplication.translate("CatalogosAgricolas", u"Nombre:", None))
        self.lpD.setText(QCoreApplication.translate("CatalogosAgricolas", u"Descripci\u00f3n:", None))
        self.btnPatAgregar.setText(QCoreApplication.translate("CatalogosAgricolas", u"+ Agregar", None))
        self.lpFil.setText(QCoreApplication.translate("CatalogosAgricolas", u"Filtrar por cultivo:", None))
        self.btnPatEditar.setText(QCoreApplication.translate("CatalogosAgricolas", u"Editar selecci\u00f3n", None))
        self.btnPatEliminar.setText(QCoreApplication.translate("CatalogosAgricolas", u"Eliminar", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabPatrones), QCoreApplication.translate("CatalogosAgricolas", u"Patrones", None))
        pass
    # retranslateUi

