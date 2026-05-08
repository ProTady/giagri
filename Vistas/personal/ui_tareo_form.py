# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_tareo_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QDoubleSpinBox, QFormLayout, QFrame, QHBoxLayout,
    QLabel, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_TareoForm(object):
    def setupUi(self, TareoForm):
        if not TareoForm.objectName():
            TareoForm.setObjectName(u"TareoForm")
        TareoForm.resize(620, 560)
        self.lytRoot = QVBoxLayout(TareoForm)
        self.lytRoot.setSpacing(10)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 16, 20, 16)
        self.lblTitulo = QLabel(TareoForm)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.lineSep = QFrame(TareoForm)
        self.lineSep.setObjectName(u"lineSep")
        self.lineSep.setFrameShape(QFrame.HLine)
        self.lineSep.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep)

        self.lytForm = QFormLayout()
        self.lytForm.setObjectName(u"lytForm")
        self.lytForm.setHorizontalSpacing(14)
        self.lytForm.setVerticalSpacing(10)
        self.lytForm.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.l1 = QLabel(TareoForm)
        self.l1.setObjectName(u"l1")

        self.lytForm.setWidget(0, QFormLayout.LabelRole, self.l1)

        self.dtFecha = QDateEdit(TareoForm)
        self.dtFecha.setObjectName(u"dtFecha")
        self.dtFecha.setCalendarPopup(True)

        self.lytForm.setWidget(0, QFormLayout.FieldRole, self.dtFecha)

        self.l2 = QLabel(TareoForm)
        self.l2.setObjectName(u"l2")

        self.lytForm.setWidget(1, QFormLayout.LabelRole, self.l2)

        self.cboEmpleado = QComboBox(TareoForm)
        self.cboEmpleado.setObjectName(u"cboEmpleado")
        self.cboEmpleado.setEditable(True)
        self.cboEmpleado.setInsertPolicy(QComboBox.NoInsert)

        self.lytForm.setWidget(1, QFormLayout.FieldRole, self.cboEmpleado)

        self.l3 = QLabel(TareoForm)
        self.l3.setObjectName(u"l3")

        self.lytForm.setWidget(2, QFormLayout.LabelRole, self.l3)

        self.cboCargo = QComboBox(TareoForm)
        self.cboCargo.setObjectName(u"cboCargo")

        self.lytForm.setWidget(2, QFormLayout.FieldRole, self.cboCargo)

        self.l4 = QLabel(TareoForm)
        self.l4.setObjectName(u"l4")

        self.lytForm.setWidget(3, QFormLayout.LabelRole, self.l4)

        self.cboLote = QComboBox(TareoForm)
        self.cboLote.setObjectName(u"cboLote")

        self.lytForm.setWidget(3, QFormLayout.FieldRole, self.cboLote)

        self.l5 = QLabel(TareoForm)
        self.l5.setObjectName(u"l5")

        self.lytForm.setWidget(4, QFormLayout.LabelRole, self.l5)

        self.cboActividad = QComboBox(TareoForm)
        self.cboActividad.setObjectName(u"cboActividad")

        self.lytForm.setWidget(4, QFormLayout.FieldRole, self.cboActividad)

        self.l6 = QLabel(TareoForm)
        self.l6.setObjectName(u"l6")

        self.lytForm.setWidget(5, QFormLayout.LabelRole, self.l6)

        self.cboLabor = QComboBox(TareoForm)
        self.cboLabor.setObjectName(u"cboLabor")

        self.lytForm.setWidget(5, QFormLayout.FieldRole, self.cboLabor)

        self.l7 = QLabel(TareoForm)
        self.l7.setObjectName(u"l7")

        self.lytForm.setWidget(6, QFormLayout.LabelRole, self.l7)

        self.spHM = QDoubleSpinBox(TareoForm)
        self.spHM.setObjectName(u"spHM")
        self.spHM.setMaximum(24.000000000000000)
        self.spHM.setDecimals(2)

        self.lytForm.setWidget(6, QFormLayout.FieldRole, self.spHM)

        self.l8 = QLabel(TareoForm)
        self.l8.setObjectName(u"l8")

        self.lytForm.setWidget(7, QFormLayout.LabelRole, self.l8)

        self.spHT = QDoubleSpinBox(TareoForm)
        self.spHT.setObjectName(u"spHT")
        self.spHT.setMaximum(24.000000000000000)
        self.spHT.setDecimals(2)

        self.lytForm.setWidget(7, QFormLayout.FieldRole, self.spHT)

        self.l9 = QLabel(TareoForm)
        self.l9.setObjectName(u"l9")

        self.lytForm.setWidget(8, QFormLayout.LabelRole, self.l9)

        self.spHE = QDoubleSpinBox(TareoForm)
        self.spHE.setObjectName(u"spHE")
        self.spHE.setMaximum(24.000000000000000)
        self.spHE.setDecimals(2)

        self.lytForm.setWidget(8, QFormLayout.FieldRole, self.spHE)

        self.l10 = QLabel(TareoForm)
        self.l10.setObjectName(u"l10")

        self.lytForm.setWidget(9, QFormLayout.LabelRole, self.l10)

        self.lblTotal = QLabel(TareoForm)
        self.lblTotal.setObjectName(u"lblTotal")
        self.lblTotal.setStyleSheet(u"font-weight:bold; color:#0F5F5C;")

        self.lytForm.setWidget(9, QFormLayout.FieldRole, self.lblTotal)

        self.l11 = QLabel(TareoForm)
        self.l11.setObjectName(u"l11")

        self.lytForm.setWidget(10, QFormLayout.LabelRole, self.l11)

        self.lblBono = QLabel(TareoForm)
        self.lblBono.setObjectName(u"lblBono")
        self.lblBono.setStyleSheet(u"color:#3DBA3F; font-weight:bold;")

        self.lytForm.setWidget(10, QFormLayout.FieldRole, self.lblBono)

        self.l12 = QLabel(TareoForm)
        self.l12.setObjectName(u"l12")

        self.lytForm.setWidget(11, QFormLayout.LabelRole, self.l12)

        self.txtComent = QPlainTextEdit(TareoForm)
        self.txtComent.setObjectName(u"txtComent")
        self.txtComent.setMaximumSize(QSize(16777215, 80))

        self.lytForm.setWidget(11, QFormLayout.FieldRole, self.txtComent)


        self.lytRoot.addLayout(self.lytForm)

        self.lblError = QLabel(TareoForm)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setMinimumSize(QSize(0, 18))

        self.lytRoot.addWidget(self.lblError)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.spB = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtns.addItem(self.spB)

        self.btnCancelar = QPushButton(TareoForm)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnCancelar)

        self.btnGuardar = QPushButton(TareoForm)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnGuardar)


        self.lytRoot.addLayout(self.lytBtns)


        self.retranslateUi(TareoForm)

        self.btnGuardar.setDefault(True)


        QMetaObject.connectSlotsByName(TareoForm)
    # setupUi

    def retranslateUi(self, TareoForm):
        TareoForm.setWindowTitle(QCoreApplication.translate("TareoForm", u"Tareo", None))
        self.lblTitulo.setText(QCoreApplication.translate("TareoForm", u"Nueva fila de Tareo", None))
        self.l1.setText(QCoreApplication.translate("TareoForm", u"Fecha *", None))
        self.dtFecha.setDisplayFormat(QCoreApplication.translate("TareoForm", u"dd/MM/yyyy", None))
        self.l2.setText(QCoreApplication.translate("TareoForm", u"Empleado *", None))
        self.l3.setText(QCoreApplication.translate("TareoForm", u"Cargo", None))
        self.l4.setText(QCoreApplication.translate("TareoForm", u"Lote", None))
        self.l5.setText(QCoreApplication.translate("TareoForm", u"Actividad", None))
        self.l6.setText(QCoreApplication.translate("TareoForm", u"Labor", None))
        self.l7.setText(QCoreApplication.translate("TareoForm", u"Horas Ma\u00f1ana", None))
        self.spHM.setSuffix(QCoreApplication.translate("TareoForm", u" h", None))
        self.l8.setText(QCoreApplication.translate("TareoForm", u"Horas Tarde", None))
        self.spHT.setSuffix(QCoreApplication.translate("TareoForm", u" h", None))
        self.l9.setText(QCoreApplication.translate("TareoForm", u"Horas Extras", None))
        self.spHE.setSuffix(QCoreApplication.translate("TareoForm", u" h", None))
        self.l10.setText(QCoreApplication.translate("TareoForm", u"Total", None))
        self.lblTotal.setText(QCoreApplication.translate("TareoForm", u"0.00 h", None))
        self.l11.setText(QCoreApplication.translate("TareoForm", u"Bono labor", None))
        self.lblBono.setText(QCoreApplication.translate("TareoForm", u"S/. 0.00", None))
        self.l12.setText(QCoreApplication.translate("TareoForm", u"Comentario", None))
        self.lblError.setText("")
        self.btnCancelar.setText(QCoreApplication.translate("TareoForm", u"Cancelar", None))
        self.btnGuardar.setText(QCoreApplication.translate("TareoForm", u"Guardar", None))
    # retranslateUi

