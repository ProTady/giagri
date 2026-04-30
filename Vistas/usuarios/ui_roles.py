# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_roles.ui'
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
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QSpacerItem, QSplitter, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_RolesPermisos(object):
    def setupUi(self, RolesPermisos):
        if not RolesPermisos.objectName():
            RolesPermisos.setObjectName(u"RolesPermisos")
        RolesPermisos.resize(1100, 660)
        self.lytRoot = QVBoxLayout(RolesPermisos)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lblTitulo = QLabel(RolesPermisos)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.splitter = QSplitter(RolesPermisos)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.paneRoles = QFrame(self.splitter)
        self.paneRoles.setObjectName(u"paneRoles")
        self.paneRoles.setMinimumSize(QSize(280, 0))
        self.paneRoles.setMaximumSize(QSize(360, 16777215))
        self.lytRoles = QVBoxLayout(self.paneRoles)
        self.lytRoles.setSpacing(8)
        self.lytRoles.setObjectName(u"lytRoles")
        self.lytRoles.setContentsMargins(0, 0, 0, 0)
        self.lblRolesTit = QLabel(self.paneRoles)
        self.lblRolesTit.setObjectName(u"lblRolesTit")

        self.lytRoles.addWidget(self.lblRolesTit)

        self.lstRoles = QListWidget(self.paneRoles)
        self.lstRoles.setObjectName(u"lstRoles")

        self.lytRoles.addWidget(self.lstRoles)

        self.lytBtnsRol = QHBoxLayout()
        self.lytBtnsRol.setSpacing(6)
        self.lytBtnsRol.setObjectName(u"lytBtnsRol")
        self.btnNuevoRol = QPushButton(self.paneRoles)
        self.btnNuevoRol.setObjectName(u"btnNuevoRol")
        self.btnNuevoRol.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtnsRol.addWidget(self.btnNuevoRol)

        self.btnRenombrar = QPushButton(self.paneRoles)
        self.btnRenombrar.setObjectName(u"btnRenombrar")
        self.btnRenombrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtnsRol.addWidget(self.btnRenombrar)

        self.btnEliminarRol = QPushButton(self.paneRoles)
        self.btnEliminarRol.setObjectName(u"btnEliminarRol")
        self.btnEliminarRol.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtnsRol.addWidget(self.btnEliminarRol)


        self.lytRoles.addLayout(self.lytBtnsRol)

        self.splitter.addWidget(self.paneRoles)
        self.panePermisos = QFrame(self.splitter)
        self.panePermisos.setObjectName(u"panePermisos")
        self.lytPerm = QVBoxLayout(self.panePermisos)
        self.lytPerm.setSpacing(8)
        self.lytPerm.setObjectName(u"lytPerm")
        self.lytPerm.setContentsMargins(14, 0, 0, 0)
        self.lblPermTit = QLabel(self.panePermisos)
        self.lblPermTit.setObjectName(u"lblPermTit")

        self.lytPerm.addWidget(self.lblPermTit)

        self.lblRolSeleccionado = QLabel(self.panePermisos)
        self.lblRolSeleccionado.setObjectName(u"lblRolSeleccionado")

        self.lytPerm.addWidget(self.lblRolSeleccionado)

        self.treePermisos = QTreeWidget(self.panePermisos)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(4, u"Eliminar");
        __qtreewidgetitem.setText(3, u"Editar");
        __qtreewidgetitem.setText(2, u"Crear");
        __qtreewidgetitem.setText(1, u"Ver");
        __qtreewidgetitem.setText(0, u"M\u00f3dulo");
        self.treePermisos.setHeaderItem(__qtreewidgetitem)
        self.treePermisos.setObjectName(u"treePermisos")
        self.treePermisos.setAlternatingRowColors(True)
        self.treePermisos.setRootIsDecorated(True)
        self.treePermisos.setIndentation(18)

        self.lytPerm.addWidget(self.treePermisos)

        self.lytBtnsPerm = QHBoxLayout()
        self.lytBtnsPerm.setObjectName(u"lytBtnsPerm")
        self.lblAyuda = QLabel(self.panePermisos)
        self.lblAyuda.setObjectName(u"lblAyuda")

        self.lytBtnsPerm.addWidget(self.lblAyuda)

        self.spP = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtnsPerm.addItem(self.spP)

        self.btnGuardarPerm = QPushButton(self.panePermisos)
        self.btnGuardarPerm.setObjectName(u"btnGuardarPerm")
        self.btnGuardarPerm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtnsPerm.addWidget(self.btnGuardarPerm)


        self.lytPerm.addLayout(self.lytBtnsPerm)

        self.splitter.addWidget(self.panePermisos)

        self.lytRoot.addWidget(self.splitter)


        self.retranslateUi(RolesPermisos)

        QMetaObject.connectSlotsByName(RolesPermisos)
    # setupUi

    def retranslateUi(self, RolesPermisos):
        self.lblTitulo.setText(QCoreApplication.translate("RolesPermisos", u"Roles y Permisos", None))
        self.lblRolesTit.setText(QCoreApplication.translate("RolesPermisos", u"Roles del fundo", None))
        self.btnNuevoRol.setText(QCoreApplication.translate("RolesPermisos", u"+ Nuevo", None))
        self.btnRenombrar.setText(QCoreApplication.translate("RolesPermisos", u"Renombrar", None))
        self.btnEliminarRol.setText(QCoreApplication.translate("RolesPermisos", u"Eliminar", None))
        self.lblPermTit.setText(QCoreApplication.translate("RolesPermisos", u"Permisos del rol", None))
        self.lblRolSeleccionado.setText(QCoreApplication.translate("RolesPermisos", u"(Selecciona un rol)", None))
        self.lblAyuda.setText(QCoreApplication.translate("RolesPermisos", u"Tip: marcar \"Ver\" en un padre activa tambi\u00e9n sus hijos autom\u00e1ticamente.", None))
        self.btnGuardarPerm.setText(QCoreApplication.translate("RolesPermisos", u"Guardar Permisos", None))
        pass
    # retranslateUi

