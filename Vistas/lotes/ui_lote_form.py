# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_lote_form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QDialog, QDoubleSpinBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSpinBox,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_LoteForm(object):
    def setupUi(self, LoteForm):
        if not LoteForm.objectName():
            LoteForm.setObjectName(u"LoteForm")
        LoteForm.resize(680, 720)
        self.lytRoot = QVBoxLayout(LoteForm)
        self.lytRoot.setSpacing(10)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 16, 20, 16)
        self.lblTitulo = QLabel(LoteForm)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.lineSep = QFrame(LoteForm)
        self.lineSep.setObjectName(u"lineSep")
        self.lineSep.setFrameShape(QFrame.HLine)
        self.lineSep.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep)

        self.tabs = QTabWidget(LoteForm)
        self.tabs.setObjectName(u"tabs")
        self.tabGeneral = QWidget()
        self.tabGeneral.setObjectName(u"tabGeneral")
        self.lytGen = QFormLayout(self.tabGeneral)
        self.lytGen.setObjectName(u"lytGen")
        self.lytGen.setHorizontalSpacing(14)
        self.lytGen.setVerticalSpacing(10)
        self.lytGen.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.l1 = QLabel(self.tabGeneral)
        self.l1.setObjectName(u"l1")

        self.lytGen.setWidget(0, QFormLayout.LabelRole, self.l1)

        self.txtCodigo = QLineEdit(self.tabGeneral)
        self.txtCodigo.setObjectName(u"txtCodigo")

        self.lytGen.setWidget(0, QFormLayout.FieldRole, self.txtCodigo)

        self.l2 = QLabel(self.tabGeneral)
        self.l2.setObjectName(u"l2")

        self.lytGen.setWidget(1, QFormLayout.LabelRole, self.l2)

        self.txtNombre = QLineEdit(self.tabGeneral)
        self.txtNombre.setObjectName(u"txtNombre")

        self.lytGen.setWidget(1, QFormLayout.FieldRole, self.txtNombre)

        self.l3 = QLabel(self.tabGeneral)
        self.l3.setObjectName(u"l3")

        self.lytGen.setWidget(2, QFormLayout.LabelRole, self.l3)

        self.cboCultivo = QComboBox(self.tabGeneral)
        self.cboCultivo.setObjectName(u"cboCultivo")

        self.lytGen.setWidget(2, QFormLayout.FieldRole, self.cboCultivo)

        self.l4 = QLabel(self.tabGeneral)
        self.l4.setObjectName(u"l4")

        self.lytGen.setWidget(3, QFormLayout.LabelRole, self.l4)

        self.cboVariedad = QComboBox(self.tabGeneral)
        self.cboVariedad.setObjectName(u"cboVariedad")

        self.lytGen.setWidget(3, QFormLayout.FieldRole, self.cboVariedad)

        self.l5 = QLabel(self.tabGeneral)
        self.l5.setObjectName(u"l5")

        self.lytGen.setWidget(4, QFormLayout.LabelRole, self.l5)

        self.cboPatron = QComboBox(self.tabGeneral)
        self.cboPatron.setObjectName(u"cboPatron")

        self.lytGen.setWidget(4, QFormLayout.FieldRole, self.cboPatron)

        self.l6 = QLabel(self.tabGeneral)
        self.l6.setObjectName(u"l6")

        self.lytGen.setWidget(5, QFormLayout.LabelRole, self.l6)

        self.cboEstado = QComboBox(self.tabGeneral)
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.setObjectName(u"cboEstado")

        self.lytGen.setWidget(5, QFormLayout.FieldRole, self.cboEstado)

        self.tabs.addTab(self.tabGeneral, "")
        self.tabTecnico = QWidget()
        self.tabTecnico.setObjectName(u"tabTecnico")
        self.lytTec = QFormLayout(self.tabTecnico)
        self.lytTec.setObjectName(u"lytTec")
        self.lytTec.setHorizontalSpacing(14)
        self.lytTec.setVerticalSpacing(10)
        self.lytTec.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.l10 = QLabel(self.tabTecnico)
        self.l10.setObjectName(u"l10")

        self.lytTec.setWidget(0, QFormLayout.LabelRole, self.l10)

        self.spHa = QDoubleSpinBox(self.tabTecnico)
        self.spHa.setObjectName(u"spHa")
        self.spHa.setMaximum(99999.999899999995250)
        self.spHa.setDecimals(4)

        self.lytTec.setWidget(0, QFormLayout.FieldRole, self.spHa)

        self.l11 = QLabel(self.tabTecnico)
        self.l11.setObjectName(u"l11")

        self.lytTec.setWidget(1, QFormLayout.LabelRole, self.l11)

        self.lyFs = QHBoxLayout()
        self.lyFs.setObjectName(u"lyFs")
        self.chkFs = QCheckBox(self.tabTecnico)
        self.chkFs.setObjectName(u"chkFs")

        self.lyFs.addWidget(self.chkFs)

        self.dtSiembra = QDateEdit(self.tabTecnico)
        self.dtSiembra.setObjectName(u"dtSiembra")
        self.dtSiembra.setCalendarPopup(True)
        self.dtSiembra.setEnabled(False)

        self.lyFs.addWidget(self.dtSiembra)


        self.lytTec.setLayout(1, QFormLayout.FieldRole, self.lyFs)

        self.l12 = QLabel(self.tabTecnico)
        self.l12.setObjectName(u"l12")

        self.lytTec.setWidget(2, QFormLayout.LabelRole, self.l12)

        self.lyFp = QHBoxLayout()
        self.lyFp.setObjectName(u"lyFp")
        self.chkFp = QCheckBox(self.tabTecnico)
        self.chkFp.setObjectName(u"chkFp")

        self.lyFp.addWidget(self.chkFp)

        self.dtProd = QDateEdit(self.tabTecnico)
        self.dtProd.setObjectName(u"dtProd")
        self.dtProd.setCalendarPopup(True)
        self.dtProd.setEnabled(False)

        self.lyFp.addWidget(self.dtProd)


        self.lytTec.setLayout(2, QFormLayout.FieldRole, self.lyFp)

        self.l13 = QLabel(self.tabTecnico)
        self.l13.setObjectName(u"l13")

        self.lytTec.setWidget(3, QFormLayout.LabelRole, self.l13)

        self.spDens = QSpinBox(self.tabTecnico)
        self.spDens.setObjectName(u"spDens")
        self.spDens.setMaximum(99999)

        self.lytTec.setWidget(3, QFormLayout.FieldRole, self.spDens)

        self.l14 = QLabel(self.tabTecnico)
        self.l14.setObjectName(u"l14")

        self.lytTec.setWidget(4, QFormLayout.LabelRole, self.l14)

        self.spTotal = QSpinBox(self.tabTecnico)
        self.spTotal.setObjectName(u"spTotal")
        self.spTotal.setMaximum(9999999)

        self.lytTec.setWidget(4, QFormLayout.FieldRole, self.spTotal)

        self.l15 = QLabel(self.tabTecnico)
        self.l15.setObjectName(u"l15")

        self.lytTec.setWidget(5, QFormLayout.LabelRole, self.l15)

        self.spDistP = QDoubleSpinBox(self.tabTecnico)
        self.spDistP.setObjectName(u"spDistP")
        self.spDistP.setMaximum(99.989999999999995)
        self.spDistP.setDecimals(2)

        self.lytTec.setWidget(5, QFormLayout.FieldRole, self.spDistP)

        self.l16 = QLabel(self.tabTecnico)
        self.l16.setObjectName(u"l16")

        self.lytTec.setWidget(6, QFormLayout.LabelRole, self.l16)

        self.spDistF = QDoubleSpinBox(self.tabTecnico)
        self.spDistF.setObjectName(u"spDistF")
        self.spDistF.setMaximum(99.989999999999995)
        self.spDistF.setDecimals(2)

        self.lytTec.setWidget(6, QFormLayout.FieldRole, self.spDistF)

        self.l17 = QLabel(self.tabTecnico)
        self.l17.setObjectName(u"l17")

        self.lytTec.setWidget(7, QFormLayout.LabelRole, self.l17)

        self.cboRiego = QComboBox(self.tabTecnico)
        self.cboRiego.addItem("")
        self.cboRiego.addItem("")
        self.cboRiego.addItem("")
        self.cboRiego.addItem("")
        self.cboRiego.addItem("")
        self.cboRiego.setObjectName(u"cboRiego")

        self.lytTec.setWidget(7, QFormLayout.FieldRole, self.cboRiego)

        self.l18 = QLabel(self.tabTecnico)
        self.l18.setObjectName(u"l18")

        self.lytTec.setWidget(8, QFormLayout.LabelRole, self.l18)

        self.txtObs = QPlainTextEdit(self.tabTecnico)
        self.txtObs.setObjectName(u"txtObs")
        self.txtObs.setMaximumSize(QSize(16777215, 90))

        self.lytTec.setWidget(8, QFormLayout.FieldRole, self.txtObs)

        self.tabs.addTab(self.tabTecnico, "")

        self.lytRoot.addWidget(self.tabs)

        self.lblError = QLabel(LoteForm)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setMinimumSize(QSize(0, 18))

        self.lytRoot.addWidget(self.lblError)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.spB = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtns.addItem(self.spB)

        self.btnCancelar = QPushButton(LoteForm)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnCancelar)

        self.btnGuardar = QPushButton(LoteForm)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnGuardar)


        self.lytRoot.addLayout(self.lytBtns)


        self.retranslateUi(LoteForm)

        self.btnGuardar.setDefault(True)


        QMetaObject.connectSlotsByName(LoteForm)
    # setupUi

    def retranslateUi(self, LoteForm):
        LoteForm.setWindowTitle(QCoreApplication.translate("LoteForm", u"Lote", None))
        self.lblTitulo.setText(QCoreApplication.translate("LoteForm", u"Nuevo Lote", None))
        self.l1.setText(QCoreApplication.translate("LoteForm", u"C\u00f3digo *", None))
        self.txtCodigo.setPlaceholderText(QCoreApplication.translate("LoteForm", u"L-001", None))
        self.l2.setText(QCoreApplication.translate("LoteForm", u"Nombre *", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("LoteForm", u"Ej: Lote Norte 1", None))
        self.l3.setText(QCoreApplication.translate("LoteForm", u"Tipo de cultivo", None))
        self.l4.setText(QCoreApplication.translate("LoteForm", u"Variedad", None))
        self.l5.setText(QCoreApplication.translate("LoteForm", u"Patr\u00f3n", None))
        self.l6.setText(QCoreApplication.translate("LoteForm", u"Estado *", None))
        self.cboEstado.setItemText(0, QCoreApplication.translate("LoteForm", u"Activo", None))
        self.cboEstado.setItemText(1, QCoreApplication.translate("LoteForm", u"En desarrollo", None))
        self.cboEstado.setItemText(2, QCoreApplication.translate("LoteForm", u"Inactivo", None))
        self.cboEstado.setItemText(3, QCoreApplication.translate("LoteForm", u"Erradicado", None))

        self.tabs.setTabText(self.tabs.indexOf(self.tabGeneral), QCoreApplication.translate("LoteForm", u"Identificaci\u00f3n", None))
        self.l10.setText(QCoreApplication.translate("LoteForm", u"Hect\u00e1reas", None))
        self.spHa.setSuffix(QCoreApplication.translate("LoteForm", u" ha", None))
        self.l11.setText(QCoreApplication.translate("LoteForm", u"Fecha siembra", None))
        self.chkFs.setText(QCoreApplication.translate("LoteForm", u"Tiene fecha", None))
        self.dtSiembra.setDisplayFormat(QCoreApplication.translate("LoteForm", u"dd/MM/yyyy", None))
        self.l12.setText(QCoreApplication.translate("LoteForm", u"Inicio producci\u00f3n", None))
        self.chkFp.setText(QCoreApplication.translate("LoteForm", u"Tiene fecha", None))
        self.dtProd.setDisplayFormat(QCoreApplication.translate("LoteForm", u"dd/MM/yyyy", None))
        self.l13.setText(QCoreApplication.translate("LoteForm", u"Densidad (pl/ha)", None))
        self.l14.setText(QCoreApplication.translate("LoteForm", u"Total plantas", None))
        self.l15.setText(QCoreApplication.translate("LoteForm", u"Distancia plantas (m)", None))
        self.l16.setText(QCoreApplication.translate("LoteForm", u"Distancia filas (m)", None))
        self.l17.setText(QCoreApplication.translate("LoteForm", u"Sistema de riego", None))
        self.cboRiego.setItemText(0, QCoreApplication.translate("LoteForm", u"(no especificado)", None))
        self.cboRiego.setItemText(1, QCoreApplication.translate("LoteForm", u"Goteo", None))
        self.cboRiego.setItemText(2, QCoreApplication.translate("LoteForm", u"Aspersion", None))
        self.cboRiego.setItemText(3, QCoreApplication.translate("LoteForm", u"Microaspersion", None))
        self.cboRiego.setItemText(4, QCoreApplication.translate("LoteForm", u"Gravedad", None))

        self.l18.setText(QCoreApplication.translate("LoteForm", u"Observaciones", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabTecnico), QCoreApplication.translate("LoteForm", u"Datos t\u00e9cnicos", None))
        self.lblError.setText("")
        self.btnCancelar.setText(QCoreApplication.translate("LoteForm", u"Cancelar", None))
        self.btnGuardar.setText(QCoreApplication.translate("LoteForm", u"Guardar", None))
    # retranslateUi

