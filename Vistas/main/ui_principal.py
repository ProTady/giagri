# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_principal.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QStackedWidget, QStatusBar,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        if not VentanaPrincipal.objectName():
            VentanaPrincipal.setObjectName(u"VentanaPrincipal")
        VentanaPrincipal.resize(1280, 760)
        self.centralwidget = QWidget(VentanaPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lytRoot = QVBoxLayout(self.centralwidget)
        self.lytRoot.setSpacing(0)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(0, 0, 0, 0)
        self.frameHeader = QFrame(self.centralwidget)
        self.frameHeader.setObjectName(u"frameHeader")
        self.frameHeader.setMinimumSize(QSize(0, 64))
        self.frameHeader.setMaximumSize(QSize(16777215, 64))
        self.lytHeader = QHBoxLayout(self.frameHeader)
        self.lytHeader.setSpacing(12)
        self.lytHeader.setObjectName(u"lytHeader")
        self.lytHeader.setContentsMargins(16, 8, 16, 8)
        self.lblLogoMini = QLabel(self.frameHeader)
        self.lblLogoMini.setObjectName(u"lblLogoMini")
        self.lblLogoMini.setMinimumSize(QSize(48, 48))
        self.lblLogoMini.setMaximumSize(QSize(48, 48))

        self.lytHeader.addWidget(self.lblLogoMini)

        self.lblAppNombre = QLabel(self.frameHeader)
        self.lblAppNombre.setObjectName(u"lblAppNombre")

        self.lytHeader.addWidget(self.lblAppNombre)

        self.spHeader = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytHeader.addItem(self.spHeader)

        self.lblFundo = QLabel(self.frameHeader)
        self.lblFundo.setObjectName(u"lblFundo")

        self.lytHeader.addWidget(self.lblFundo)

        self.sepH1 = QFrame(self.frameHeader)
        self.sepH1.setObjectName(u"sepH1")
        self.sepH1.setFrameShape(QFrame.VLine)
        self.sepH1.setFrameShadow(QFrame.Plain)

        self.lytHeader.addWidget(self.sepH1)

        self.lblUsuario = QLabel(self.frameHeader)
        self.lblUsuario.setObjectName(u"lblUsuario")

        self.lytHeader.addWidget(self.lblUsuario)

        self.btnSalir = QPushButton(self.frameHeader)
        self.btnSalir.setObjectName(u"btnSalir")
        self.btnSalir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytHeader.addWidget(self.btnSalir)


        self.lytRoot.addWidget(self.frameHeader)

        self.splitterCuerpo = QSplitter(self.centralwidget)
        self.splitterCuerpo.setObjectName(u"splitterCuerpo")
        self.splitterCuerpo.setOrientation(Qt.Horizontal)
        self.splitterCuerpo.setChildrenCollapsible(False)
        self.frameMenu = QFrame(self.splitterCuerpo)
        self.frameMenu.setObjectName(u"frameMenu")
        self.frameMenu.setMinimumSize(QSize(240, 0))
        self.frameMenu.setMaximumSize(QSize(360, 16777215))
        self.lytMenu = QVBoxLayout(self.frameMenu)
        self.lytMenu.setSpacing(0)
        self.lytMenu.setObjectName(u"lytMenu")
        self.lytMenu.setContentsMargins(0, 0, 0, 0)
        self.lblMenuTitulo = QLabel(self.frameMenu)
        self.lblMenuTitulo.setObjectName(u"lblMenuTitulo")
        self.lblMenuTitulo.setMinimumSize(QSize(0, 32))

        self.lytMenu.addWidget(self.lblMenuTitulo)

        self.treeMenu = QTreeWidget(self.frameMenu)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeMenu.setHeaderItem(__qtreewidgetitem)
        self.treeMenu.setObjectName(u"treeMenu")
        self.treeMenu.setHeaderHidden(True)
        self.treeMenu.setIndentation(16)
        self.treeMenu.setAnimated(True)

        self.lytMenu.addWidget(self.treeMenu)

        self.splitterCuerpo.addWidget(self.frameMenu)
        self.stackContenido = QStackedWidget(self.splitterCuerpo)
        self.stackContenido.setObjectName(u"stackContenido")
        self.paginaInicio = QWidget()
        self.paginaInicio.setObjectName(u"paginaInicio")
        self.lytInicio = QVBoxLayout(self.paginaInicio)
        self.lytInicio.setObjectName(u"lytInicio")
        self.lblBienvenida = QLabel(self.paginaInicio)
        self.lblBienvenida.setObjectName(u"lblBienvenida")
        self.lblBienvenida.setAlignment(Qt.AlignCenter)

        self.lytInicio.addWidget(self.lblBienvenida)

        self.lblBienvenidaSub = QLabel(self.paginaInicio)
        self.lblBienvenidaSub.setObjectName(u"lblBienvenidaSub")
        self.lblBienvenidaSub.setAlignment(Qt.AlignCenter)

        self.lytInicio.addWidget(self.lblBienvenidaSub)

        self.stackContenido.addWidget(self.paginaInicio)
        self.splitterCuerpo.addWidget(self.stackContenido)

        self.lytRoot.addWidget(self.splitterCuerpo)

        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(VentanaPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        VentanaPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(VentanaPrincipal)

        QMetaObject.connectSlotsByName(VentanaPrincipal)
    # setupUi

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(QCoreApplication.translate("VentanaPrincipal", u"GIAGRI - Sistema de Gesti\u00f3n Agr\u00edcola", None))
        self.lblLogoMini.setText("")
        self.lblAppNombre.setText(QCoreApplication.translate("VentanaPrincipal", u"GIAGRI", None))
        self.lblFundo.setText(QCoreApplication.translate("VentanaPrincipal", u"Fundo", None))
        self.lblUsuario.setText(QCoreApplication.translate("VentanaPrincipal", u"Usuario", None))
        self.btnSalir.setText(QCoreApplication.translate("VentanaPrincipal", u"Cerrar sesi\u00f3n", None))
        self.lblMenuTitulo.setText(QCoreApplication.translate("VentanaPrincipal", u"  MEN\u00da", None))
        self.lblBienvenida.setText(QCoreApplication.translate("VentanaPrincipal", u"Bienvenido a GIAGRI", None))
        self.lblBienvenidaSub.setText(QCoreApplication.translate("VentanaPrincipal", u"Selecciona un m\u00f3dulo del men\u00fa lateral", None))
    # retranslateUi

