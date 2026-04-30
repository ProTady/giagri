# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_fundo_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_FundoForm(object):
    def setupUi(self, FundoForm):
        if not FundoForm.objectName():
            FundoForm.setObjectName(u"FundoForm")
        FundoForm.resize(720, 500)
        self.lytRoot = QVBoxLayout(FundoForm)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lblTitulo = QLabel(FundoForm)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.lblSub = QLabel(FundoForm)
        self.lblSub.setObjectName(u"lblSub")

        self.lytRoot.addWidget(self.lblSub)

        self.lineSep = QFrame(FundoForm)
        self.lineSep.setObjectName(u"lineSep")
        self.lineSep.setFrameShape(QFrame.HLine)
        self.lineSep.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep)

        self.lytForm = QFormLayout()
        self.lytForm.setObjectName(u"lytForm")
        self.lytForm.setHorizontalSpacing(14)
        self.lytForm.setVerticalSpacing(10)
        self.lytForm.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.l1 = QLabel(FundoForm)
        self.l1.setObjectName(u"l1")

        self.lytForm.setWidget(0, QFormLayout.LabelRole, self.l1)

        self.txtCodigo = QLineEdit(FundoForm)
        self.txtCodigo.setObjectName(u"txtCodigo")
        self.txtCodigo.setReadOnly(True)

        self.lytForm.setWidget(0, QFormLayout.FieldRole, self.txtCodigo)

        self.l2 = QLabel(FundoForm)
        self.l2.setObjectName(u"l2")

        self.lytForm.setWidget(1, QFormLayout.LabelRole, self.l2)

        self.txtNombre = QLineEdit(FundoForm)
        self.txtNombre.setObjectName(u"txtNombre")

        self.lytForm.setWidget(1, QFormLayout.FieldRole, self.txtNombre)

        self.l3 = QLabel(FundoForm)
        self.l3.setObjectName(u"l3")

        self.lytForm.setWidget(2, QFormLayout.LabelRole, self.l3)

        self.txtRuc = QLineEdit(FundoForm)
        self.txtRuc.setObjectName(u"txtRuc")
        self.txtRuc.setMaxLength(11)

        self.lytForm.setWidget(2, QFormLayout.FieldRole, self.txtRuc)

        self.l4 = QLabel(FundoForm)
        self.l4.setObjectName(u"l4")

        self.lytForm.setWidget(3, QFormLayout.LabelRole, self.l4)

        self.txtDireccion = QLineEdit(FundoForm)
        self.txtDireccion.setObjectName(u"txtDireccion")

        self.lytForm.setWidget(3, QFormLayout.FieldRole, self.txtDireccion)

        self.l5 = QLabel(FundoForm)
        self.l5.setObjectName(u"l5")

        self.lytForm.setWidget(4, QFormLayout.LabelRole, self.l5)

        self.txtTelefono = QLineEdit(FundoForm)
        self.txtTelefono.setObjectName(u"txtTelefono")

        self.lytForm.setWidget(4, QFormLayout.FieldRole, self.txtTelefono)


        self.lytRoot.addLayout(self.lytForm)

        self.lblMsg = QLabel(FundoForm)
        self.lblMsg.setObjectName(u"lblMsg")
        self.lblMsg.setMinimumSize(QSize(0, 20))

        self.lytRoot.addWidget(self.lblMsg)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.spB = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtns.addItem(self.spB)

        self.btnGuardar = QPushButton(FundoForm)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnGuardar)


        self.lytRoot.addLayout(self.lytBtns)

        self.spF = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.lytRoot.addItem(self.spF)


        self.retranslateUi(FundoForm)

        QMetaObject.connectSlotsByName(FundoForm)
    # setupUi

    def retranslateUi(self, FundoForm):
        self.lblTitulo.setText(QCoreApplication.translate("FundoForm", u"Datos del Fundo", None))
        self.lblSub.setText(QCoreApplication.translate("FundoForm", u"Informaci\u00f3n general que aparecer\u00e1 en reportes y documentos.", None))
        self.l1.setText(QCoreApplication.translate("FundoForm", u"C\u00f3digo", None))
        self.l2.setText(QCoreApplication.translate("FundoForm", u"Nombre *", None))
        self.l3.setText(QCoreApplication.translate("FundoForm", u"RUC", None))
        self.txtRuc.setPlaceholderText(QCoreApplication.translate("FundoForm", u"11 d\u00edgitos", None))
        self.l4.setText(QCoreApplication.translate("FundoForm", u"Direcci\u00f3n", None))
        self.l5.setText(QCoreApplication.translate("FundoForm", u"Tel\u00e9fono", None))
        self.lblMsg.setText("")
        self.btnGuardar.setText(QCoreApplication.translate("FundoForm", u"Guardar Cambios", None))
        pass
    # retranslateUi

