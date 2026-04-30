# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_DialogLogin(object):
    def setupUi(self, DialogLogin):
        if not DialogLogin.objectName():
            DialogLogin.setObjectName(u"DialogLogin")
        DialogLogin.resize(440, 520)
        self.verticalLayout = QVBoxLayout(DialogLogin)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(35, 25, 35, 25)
        self.lblLogo = QLabel(DialogLogin)
        self.lblLogo.setObjectName(u"lblLogo")
        self.lblLogo.setMinimumSize(QSize(0, 140))
        self.lblLogo.setMaximumSize(QSize(16777215, 140))
        self.lblLogo.setAlignment(Qt.AlignCenter)
        self.lblLogo.setScaledContents(False)

        self.verticalLayout.addWidget(self.lblLogo)

        self.lblTitulo = QLabel(DialogLogin)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.lblSub = QLabel(DialogLogin)
        self.lblSub.setObjectName(u"lblSub")
        self.lblSub.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblSub)

        self.sp1 = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.sp1)

        self.lblUsuario = QLabel(DialogLogin)
        self.lblUsuario.setObjectName(u"lblUsuario")

        self.verticalLayout.addWidget(self.lblUsuario)

        self.txtUsuario = QLineEdit(DialogLogin)
        self.txtUsuario.setObjectName(u"txtUsuario")

        self.verticalLayout.addWidget(self.txtUsuario)

        self.lblClave = QLabel(DialogLogin)
        self.lblClave.setObjectName(u"lblClave")

        self.verticalLayout.addWidget(self.lblClave)

        self.txtClave = QLineEdit(DialogLogin)
        self.txtClave.setObjectName(u"txtClave")
        self.txtClave.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.txtClave)

        self.lblError = QLabel(DialogLogin)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setAlignment(Qt.AlignCenter)
        self.lblError.setMinimumSize(QSize(0, 18))

        self.verticalLayout.addWidget(self.lblError)

        self.hLayBotones = QHBoxLayout()
        self.hLayBotones.setSpacing(10)
        self.hLayBotones.setObjectName(u"hLayBotones")
        self.btnCancelar = QPushButton(DialogLogin)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.hLayBotones.addWidget(self.btnCancelar)

        self.btnIngresar = QPushButton(DialogLogin)
        self.btnIngresar.setObjectName(u"btnIngresar")
        self.btnIngresar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.hLayBotones.addWidget(self.btnIngresar)


        self.verticalLayout.addLayout(self.hLayBotones)

        QWidget.setTabOrder(self.txtUsuario, self.txtClave)
        QWidget.setTabOrder(self.txtClave, self.btnIngresar)
        QWidget.setTabOrder(self.btnIngresar, self.btnCancelar)

        self.retranslateUi(DialogLogin)

        self.btnIngresar.setDefault(True)


        QMetaObject.connectSlotsByName(DialogLogin)
    # setupUi

    def retranslateUi(self, DialogLogin):
        DialogLogin.setWindowTitle(QCoreApplication.translate("DialogLogin", u"GIAGRI - Iniciar sesi\u00f3n", None))
        self.lblLogo.setText("")
        self.lblTitulo.setText(QCoreApplication.translate("DialogLogin", u"GIAGRI", None))
        self.lblSub.setText(QCoreApplication.translate("DialogLogin", u"Sistema de Gesti\u00f3n Agr\u00edcola", None))
        self.lblUsuario.setText(QCoreApplication.translate("DialogLogin", u"Usuario", None))
        self.txtUsuario.setPlaceholderText(QCoreApplication.translate("DialogLogin", u"Ingrese su usuario", None))
        self.lblClave.setText(QCoreApplication.translate("DialogLogin", u"Contrase\u00f1a", None))
        self.txtClave.setPlaceholderText(QCoreApplication.translate("DialogLogin", u"Ingrese su contrase\u00f1a", None))
        self.lblError.setText("")
        self.btnCancelar.setText(QCoreApplication.translate("DialogLogin", u"Cancelar", None))
        self.btnIngresar.setText(QCoreApplication.translate("DialogLogin", u"Ingresar", None))
    # retranslateUi

