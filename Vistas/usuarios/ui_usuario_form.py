# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_usuario_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_UsuarioForm(object):
    def setupUi(self, UsuarioForm):
        if not UsuarioForm.objectName():
            UsuarioForm.setObjectName(u"UsuarioForm")
        UsuarioForm.resize(520, 600)
        self.lytRoot = QVBoxLayout(UsuarioForm)
        self.lytRoot.setSpacing(10)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(25, 20, 25, 20)
        self.lblTitulo = QLabel(UsuarioForm)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.lineSep = QFrame(UsuarioForm)
        self.lineSep.setObjectName(u"lineSep")
        self.lineSep.setFrameShape(QFrame.HLine)
        self.lineSep.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep)

        self.lytForm = QFormLayout()
        self.lytForm.setObjectName(u"lytForm")
        self.lytForm.setHorizontalSpacing(14)
        self.lytForm.setVerticalSpacing(10)
        self.lytForm.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.l1 = QLabel(UsuarioForm)
        self.l1.setObjectName(u"l1")

        self.lytForm.setWidget(0, QFormLayout.LabelRole, self.l1)

        self.txtUsername = QLineEdit(UsuarioForm)
        self.txtUsername.setObjectName(u"txtUsername")

        self.lytForm.setWidget(0, QFormLayout.FieldRole, self.txtUsername)

        self.l2 = QLabel(UsuarioForm)
        self.l2.setObjectName(u"l2")

        self.lytForm.setWidget(1, QFormLayout.LabelRole, self.l2)

        self.txtNombre = QLineEdit(UsuarioForm)
        self.txtNombre.setObjectName(u"txtNombre")

        self.lytForm.setWidget(1, QFormLayout.FieldRole, self.txtNombre)

        self.l3 = QLabel(UsuarioForm)
        self.l3.setObjectName(u"l3")

        self.lytForm.setWidget(2, QFormLayout.LabelRole, self.l3)

        self.txtCorreo = QLineEdit(UsuarioForm)
        self.txtCorreo.setObjectName(u"txtCorreo")

        self.lytForm.setWidget(2, QFormLayout.FieldRole, self.txtCorreo)

        self.l4 = QLabel(UsuarioForm)
        self.l4.setObjectName(u"l4")

        self.lytForm.setWidget(3, QFormLayout.LabelRole, self.l4)

        self.txtClave = QLineEdit(UsuarioForm)
        self.txtClave.setObjectName(u"txtClave")
        self.txtClave.setEchoMode(QLineEdit.Password)

        self.lytForm.setWidget(3, QFormLayout.FieldRole, self.txtClave)

        self.l5 = QLabel(UsuarioForm)
        self.l5.setObjectName(u"l5")

        self.lytForm.setWidget(4, QFormLayout.LabelRole, self.l5)

        self.txtClave2 = QLineEdit(UsuarioForm)
        self.txtClave2.setObjectName(u"txtClave2")
        self.txtClave2.setEchoMode(QLineEdit.Password)

        self.lytForm.setWidget(4, QFormLayout.FieldRole, self.txtClave2)

        self.l6 = QLabel(UsuarioForm)
        self.l6.setObjectName(u"l6")

        self.lytForm.setWidget(5, QFormLayout.LabelRole, self.l6)

        self.chkAdmin = QCheckBox(UsuarioForm)
        self.chkAdmin.setObjectName(u"chkAdmin")

        self.lytForm.setWidget(5, QFormLayout.FieldRole, self.chkAdmin)

        self.l7 = QLabel(UsuarioForm)
        self.l7.setObjectName(u"l7")

        self.lytForm.setWidget(6, QFormLayout.LabelRole, self.l7)

        self.chkActivo = QCheckBox(UsuarioForm)
        self.chkActivo.setObjectName(u"chkActivo")
        self.chkActivo.setChecked(True)

        self.lytForm.setWidget(6, QFormLayout.FieldRole, self.chkActivo)


        self.lytRoot.addLayout(self.lytForm)

        self.lblRolesTit = QLabel(UsuarioForm)
        self.lblRolesTit.setObjectName(u"lblRolesTit")

        self.lytRoot.addWidget(self.lblRolesTit)

        self.lstRoles = QListWidget(UsuarioForm)
        self.lstRoles.setObjectName(u"lstRoles")
        self.lstRoles.setMinimumSize(QSize(0, 110))

        self.lytRoot.addWidget(self.lstRoles)

        self.lblError = QLabel(UsuarioForm)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setMinimumSize(QSize(0, 18))

        self.lytRoot.addWidget(self.lblError)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.spB = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtns.addItem(self.spB)

        self.btnCancelar = QPushButton(UsuarioForm)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnCancelar)

        self.btnGuardar = QPushButton(UsuarioForm)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnGuardar)


        self.lytRoot.addLayout(self.lytBtns)


        self.retranslateUi(UsuarioForm)

        self.btnGuardar.setDefault(True)


        QMetaObject.connectSlotsByName(UsuarioForm)
    # setupUi

    def retranslateUi(self, UsuarioForm):
        UsuarioForm.setWindowTitle(QCoreApplication.translate("UsuarioForm", u"Usuario", None))
        self.lblTitulo.setText(QCoreApplication.translate("UsuarioForm", u"Nuevo Usuario", None))
        self.l1.setText(QCoreApplication.translate("UsuarioForm", u"Usuario *", None))
        self.txtUsername.setPlaceholderText(QCoreApplication.translate("UsuarioForm", u"jperez", None))
        self.l2.setText(QCoreApplication.translate("UsuarioForm", u"Nombre completo *", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("UsuarioForm", u"Juan P\u00e9rez", None))
        self.l3.setText(QCoreApplication.translate("UsuarioForm", u"Correo", None))
        self.txtCorreo.setPlaceholderText(QCoreApplication.translate("UsuarioForm", u"juan@empresa.com", None))
        self.l4.setText(QCoreApplication.translate("UsuarioForm", u"Contrase\u00f1a *", None))
        self.txtClave.setPlaceholderText(QCoreApplication.translate("UsuarioForm", u"M\u00ednimo 6 caracteres", None))
        self.l5.setText(QCoreApplication.translate("UsuarioForm", u"Confirmar *", None))
        self.l6.setText(QCoreApplication.translate("UsuarioForm", u"Es administrador", None))
        self.chkAdmin.setText(QCoreApplication.translate("UsuarioForm", u"Acceso total al sistema", None))
        self.l7.setText(QCoreApplication.translate("UsuarioForm", u"Activo", None))
        self.chkActivo.setText(QCoreApplication.translate("UsuarioForm", u"Puede iniciar sesi\u00f3n", None))
        self.lblRolesTit.setText(QCoreApplication.translate("UsuarioForm", u"Roles asignados", None))
        self.lblError.setText("")
        self.btnCancelar.setText(QCoreApplication.translate("UsuarioForm", u"Cancelar", None))
        self.btnGuardar.setText(QCoreApplication.translate("UsuarioForm", u"Guardar", None))
    # retranslateUi

