# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_empleado_form.ui'
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
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_EmpleadoForm(object):
    def setupUi(self, EmpleadoForm):
        if not EmpleadoForm.objectName():
            EmpleadoForm.setObjectName(u"EmpleadoForm")
        EmpleadoForm.resize(720, 720)
        self.lytRoot = QVBoxLayout(EmpleadoForm)
        self.lytRoot.setSpacing(10)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 16, 20, 16)
        self.lblTitulo = QLabel(EmpleadoForm)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.lineSep = QFrame(EmpleadoForm)
        self.lineSep.setObjectName(u"lineSep")
        self.lineSep.setFrameShape(QFrame.HLine)
        self.lineSep.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep)

        self.tabs = QTabWidget(EmpleadoForm)
        self.tabs.setObjectName(u"tabs")
        self.tabPersonal = QWidget()
        self.tabPersonal.setObjectName(u"tabPersonal")
        self.lytPers = QFormLayout(self.tabPersonal)
        self.lytPers.setObjectName(u"lytPers")
        self.lytPers.setHorizontalSpacing(14)
        self.lytPers.setVerticalSpacing(10)
        self.lytPers.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.l1 = QLabel(self.tabPersonal)
        self.l1.setObjectName(u"l1")

        self.lytPers.setWidget(0, QFormLayout.LabelRole, self.l1)

        self.txtCodigo = QLineEdit(self.tabPersonal)
        self.txtCodigo.setObjectName(u"txtCodigo")

        self.lytPers.setWidget(0, QFormLayout.FieldRole, self.txtCodigo)

        self.l2 = QLabel(self.tabPersonal)
        self.l2.setObjectName(u"l2")

        self.lytPers.setWidget(1, QFormLayout.LabelRole, self.l2)

        self.txtDni = QLineEdit(self.tabPersonal)
        self.txtDni.setObjectName(u"txtDni")
        self.txtDni.setMaxLength(15)

        self.lytPers.setWidget(1, QFormLayout.FieldRole, self.txtDni)

        self.l3 = QLabel(self.tabPersonal)
        self.l3.setObjectName(u"l3")

        self.lytPers.setWidget(2, QFormLayout.LabelRole, self.l3)

        self.txtApPaterno = QLineEdit(self.tabPersonal)
        self.txtApPaterno.setObjectName(u"txtApPaterno")

        self.lytPers.setWidget(2, QFormLayout.FieldRole, self.txtApPaterno)

        self.l4 = QLabel(self.tabPersonal)
        self.l4.setObjectName(u"l4")

        self.lytPers.setWidget(3, QFormLayout.LabelRole, self.l4)

        self.txtApMaterno = QLineEdit(self.tabPersonal)
        self.txtApMaterno.setObjectName(u"txtApMaterno")

        self.lytPers.setWidget(3, QFormLayout.FieldRole, self.txtApMaterno)

        self.l5 = QLabel(self.tabPersonal)
        self.l5.setObjectName(u"l5")

        self.lytPers.setWidget(4, QFormLayout.LabelRole, self.l5)

        self.txtNombres = QLineEdit(self.tabPersonal)
        self.txtNombres.setObjectName(u"txtNombres")

        self.lytPers.setWidget(4, QFormLayout.FieldRole, self.txtNombres)

        self.l6 = QLabel(self.tabPersonal)
        self.l6.setObjectName(u"l6")

        self.lytPers.setWidget(5, QFormLayout.LabelRole, self.l6)

        self.dtNac = QDateEdit(self.tabPersonal)
        self.dtNac.setObjectName(u"dtNac")
        self.dtNac.setCalendarPopup(True)

        self.lytPers.setWidget(5, QFormLayout.FieldRole, self.dtNac)

        self.l7 = QLabel(self.tabPersonal)
        self.l7.setObjectName(u"l7")

        self.lytPers.setWidget(6, QFormLayout.LabelRole, self.l7)

        self.cboSexo = QComboBox(self.tabPersonal)
        self.cboSexo.addItem("")
        self.cboSexo.addItem("")
        self.cboSexo.addItem("")
        self.cboSexo.setObjectName(u"cboSexo")

        self.lytPers.setWidget(6, QFormLayout.FieldRole, self.cboSexo)

        self.l8 = QLabel(self.tabPersonal)
        self.l8.setObjectName(u"l8")

        self.lytPers.setWidget(7, QFormLayout.LabelRole, self.l8)

        self.cboEstadoCivil = QComboBox(self.tabPersonal)
        self.cboEstadoCivil.addItem("")
        self.cboEstadoCivil.addItem("")
        self.cboEstadoCivil.addItem("")
        self.cboEstadoCivil.addItem("")
        self.cboEstadoCivil.addItem("")
        self.cboEstadoCivil.addItem("")
        self.cboEstadoCivil.setObjectName(u"cboEstadoCivil")
        self.cboEstadoCivil.setEditable(False)

        self.lytPers.setWidget(7, QFormLayout.FieldRole, self.cboEstadoCivil)

        self.l9 = QLabel(self.tabPersonal)
        self.l9.setObjectName(u"l9")

        self.lytPers.setWidget(8, QFormLayout.LabelRole, self.l9)

        self.txtDireccion = QLineEdit(self.tabPersonal)
        self.txtDireccion.setObjectName(u"txtDireccion")

        self.lytPers.setWidget(8, QFormLayout.FieldRole, self.txtDireccion)

        self.l10 = QLabel(self.tabPersonal)
        self.l10.setObjectName(u"l10")

        self.lytPers.setWidget(9, QFormLayout.LabelRole, self.l10)

        self.txtTelefono = QLineEdit(self.tabPersonal)
        self.txtTelefono.setObjectName(u"txtTelefono")

        self.lytPers.setWidget(9, QFormLayout.FieldRole, self.txtTelefono)

        self.l11 = QLabel(self.tabPersonal)
        self.l11.setObjectName(u"l11")

        self.lytPers.setWidget(10, QFormLayout.LabelRole, self.l11)

        self.txtCorreo = QLineEdit(self.tabPersonal)
        self.txtCorreo.setObjectName(u"txtCorreo")

        self.lytPers.setWidget(10, QFormLayout.FieldRole, self.txtCorreo)

        self.tabs.addTab(self.tabPersonal, "")
        self.tabLaboral = QWidget()
        self.tabLaboral.setObjectName(u"tabLaboral")
        self.lytLab = QFormLayout(self.tabLaboral)
        self.lytLab.setObjectName(u"lytLab")
        self.lytLab.setHorizontalSpacing(14)
        self.lytLab.setVerticalSpacing(10)
        self.lytLab.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.l20 = QLabel(self.tabLaboral)
        self.l20.setObjectName(u"l20")

        self.lytLab.setWidget(0, QFormLayout.LabelRole, self.l20)

        self.cboCargo = QComboBox(self.tabLaboral)
        self.cboCargo.setObjectName(u"cboCargo")

        self.lytLab.setWidget(0, QFormLayout.FieldRole, self.cboCargo)

        self.l21 = QLabel(self.tabLaboral)
        self.l21.setObjectName(u"l21")

        self.lytLab.setWidget(1, QFormLayout.LabelRole, self.l21)

        self.cboArea = QComboBox(self.tabLaboral)
        self.cboArea.setObjectName(u"cboArea")

        self.lytLab.setWidget(1, QFormLayout.FieldRole, self.cboArea)

        self.l22 = QLabel(self.tabLaboral)
        self.l22.setObjectName(u"l22")

        self.lytLab.setWidget(2, QFormLayout.LabelRole, self.l22)

        self.dtIngreso = QDateEdit(self.tabLaboral)
        self.dtIngreso.setObjectName(u"dtIngreso")
        self.dtIngreso.setCalendarPopup(True)

        self.lytLab.setWidget(2, QFormLayout.FieldRole, self.dtIngreso)

        self.l23 = QLabel(self.tabLaboral)
        self.l23.setObjectName(u"l23")

        self.lytLab.setWidget(3, QFormLayout.LabelRole, self.l23)

        self.lytCese = QHBoxLayout()
        self.lytCese.setObjectName(u"lytCese")
        self.chkCese = QCheckBox(self.tabLaboral)
        self.chkCese.setObjectName(u"chkCese")

        self.lytCese.addWidget(self.chkCese)

        self.dtCese = QDateEdit(self.tabLaboral)
        self.dtCese.setObjectName(u"dtCese")
        self.dtCese.setCalendarPopup(True)
        self.dtCese.setEnabled(False)

        self.lytCese.addWidget(self.dtCese)


        self.lytLab.setLayout(3, QFormLayout.FieldRole, self.lytCese)

        self.l24 = QLabel(self.tabLaboral)
        self.l24.setObjectName(u"l24")

        self.lytLab.setWidget(4, QFormLayout.LabelRole, self.l24)

        self.cboEstado = QComboBox(self.tabLaboral)
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.addItem("")
        self.cboEstado.setObjectName(u"cboEstado")

        self.lytLab.setWidget(4, QFormLayout.FieldRole, self.cboEstado)

        self.l25 = QLabel(self.tabLaboral)
        self.l25.setObjectName(u"l25")

        self.lytLab.setWidget(5, QFormLayout.LabelRole, self.l25)

        self.spSueldo = QDoubleSpinBox(self.tabLaboral)
        self.spSueldo.setObjectName(u"spSueldo")
        self.spSueldo.setMaximum(999999.989999999990687)
        self.spSueldo.setDecimals(2)

        self.lytLab.setWidget(5, QFormLayout.FieldRole, self.spSueldo)

        self.l26 = QLabel(self.tabLaboral)
        self.l26.setObjectName(u"l26")

        self.lytLab.setWidget(6, QFormLayout.LabelRole, self.l26)

        self.txtBanco = QLineEdit(self.tabLaboral)
        self.txtBanco.setObjectName(u"txtBanco")

        self.lytLab.setWidget(6, QFormLayout.FieldRole, self.txtBanco)

        self.l27 = QLabel(self.tabLaboral)
        self.l27.setObjectName(u"l27")

        self.lytLab.setWidget(7, QFormLayout.LabelRole, self.l27)

        self.txtCuenta = QLineEdit(self.tabLaboral)
        self.txtCuenta.setObjectName(u"txtCuenta")

        self.lytLab.setWidget(7, QFormLayout.FieldRole, self.txtCuenta)

        self.l28 = QLabel(self.tabLaboral)
        self.l28.setObjectName(u"l28")

        self.lytLab.setWidget(8, QFormLayout.LabelRole, self.l28)

        self.txtObs = QPlainTextEdit(self.tabLaboral)
        self.txtObs.setObjectName(u"txtObs")
        self.txtObs.setMaximumSize(QSize(16777215, 90))

        self.lytLab.setWidget(8, QFormLayout.FieldRole, self.txtObs)

        self.tabs.addTab(self.tabLaboral, "")

        self.lytRoot.addWidget(self.tabs)

        self.lblError = QLabel(EmpleadoForm)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setMinimumSize(QSize(0, 18))

        self.lytRoot.addWidget(self.lblError)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.spB = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtns.addItem(self.spB)

        self.btnCancelar = QPushButton(EmpleadoForm)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnCancelar)

        self.btnGuardar = QPushButton(EmpleadoForm)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnGuardar)


        self.lytRoot.addLayout(self.lytBtns)


        self.retranslateUi(EmpleadoForm)

        self.btnGuardar.setDefault(True)


        QMetaObject.connectSlotsByName(EmpleadoForm)
    # setupUi

    def retranslateUi(self, EmpleadoForm):
        EmpleadoForm.setWindowTitle(QCoreApplication.translate("EmpleadoForm", u"Empleado", None))
        self.lblTitulo.setText(QCoreApplication.translate("EmpleadoForm", u"Nuevo Empleado", None))
        self.l1.setText(QCoreApplication.translate("EmpleadoForm", u"C\u00f3digo *", None))
        self.txtCodigo.setPlaceholderText(QCoreApplication.translate("EmpleadoForm", u"EMP-001", None))
        self.l2.setText(QCoreApplication.translate("EmpleadoForm", u"DNI *", None))
        self.l3.setText(QCoreApplication.translate("EmpleadoForm", u"Apellido paterno *", None))
        self.l4.setText(QCoreApplication.translate("EmpleadoForm", u"Apellido materno", None))
        self.l5.setText(QCoreApplication.translate("EmpleadoForm", u"Nombres *", None))
        self.l6.setText(QCoreApplication.translate("EmpleadoForm", u"Fecha nacimiento", None))
        self.dtNac.setDisplayFormat(QCoreApplication.translate("EmpleadoForm", u"dd/MM/yyyy", None))
        self.l7.setText(QCoreApplication.translate("EmpleadoForm", u"Sexo", None))
        self.cboSexo.setItemText(0, QCoreApplication.translate("EmpleadoForm", u"(no especificado)", None))
        self.cboSexo.setItemText(1, QCoreApplication.translate("EmpleadoForm", u"Masculino", None))
        self.cboSexo.setItemText(2, QCoreApplication.translate("EmpleadoForm", u"Femenino", None))

        self.l8.setText(QCoreApplication.translate("EmpleadoForm", u"Estado civil", None))
        self.cboEstadoCivil.setItemText(0, "")
        self.cboEstadoCivil.setItemText(1, QCoreApplication.translate("EmpleadoForm", u"Soltero(a)", None))
        self.cboEstadoCivil.setItemText(2, QCoreApplication.translate("EmpleadoForm", u"Casado(a)", None))
        self.cboEstadoCivil.setItemText(3, QCoreApplication.translate("EmpleadoForm", u"Conviviente", None))
        self.cboEstadoCivil.setItemText(4, QCoreApplication.translate("EmpleadoForm", u"Divorciado(a)", None))
        self.cboEstadoCivil.setItemText(5, QCoreApplication.translate("EmpleadoForm", u"Viudo(a)", None))

        self.l9.setText(QCoreApplication.translate("EmpleadoForm", u"Direcci\u00f3n", None))
        self.l10.setText(QCoreApplication.translate("EmpleadoForm", u"Tel\u00e9fono", None))
        self.l11.setText(QCoreApplication.translate("EmpleadoForm", u"Correo", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabPersonal), QCoreApplication.translate("EmpleadoForm", u"Datos personales", None))
        self.l20.setText(QCoreApplication.translate("EmpleadoForm", u"Cargo", None))
        self.l21.setText(QCoreApplication.translate("EmpleadoForm", u"\u00c1rea de trabajo", None))
        self.l22.setText(QCoreApplication.translate("EmpleadoForm", u"Fecha ingreso *", None))
        self.dtIngreso.setDisplayFormat(QCoreApplication.translate("EmpleadoForm", u"dd/MM/yyyy", None))
        self.l23.setText(QCoreApplication.translate("EmpleadoForm", u"Fecha cese", None))
        self.chkCese.setText(QCoreApplication.translate("EmpleadoForm", u"Tiene fecha de cese", None))
        self.dtCese.setDisplayFormat(QCoreApplication.translate("EmpleadoForm", u"dd/MM/yyyy", None))
        self.l24.setText(QCoreApplication.translate("EmpleadoForm", u"Estado *", None))
        self.cboEstado.setItemText(0, QCoreApplication.translate("EmpleadoForm", u"Activo", None))
        self.cboEstado.setItemText(1, QCoreApplication.translate("EmpleadoForm", u"Vacaciones", None))
        self.cboEstado.setItemText(2, QCoreApplication.translate("EmpleadoForm", u"Suspendido", None))
        self.cboEstado.setItemText(3, QCoreApplication.translate("EmpleadoForm", u"Cesado", None))

        self.l25.setText(QCoreApplication.translate("EmpleadoForm", u"Sueldo base", None))
        self.l26.setText(QCoreApplication.translate("EmpleadoForm", u"Banco", None))
        self.l27.setText(QCoreApplication.translate("EmpleadoForm", u"Cuenta bancaria", None))
        self.l28.setText(QCoreApplication.translate("EmpleadoForm", u"Observaciones", None))
        self.tabs.setTabText(self.tabs.indexOf(self.tabLaboral), QCoreApplication.translate("EmpleadoForm", u"Datos laborales", None))
        self.lblError.setText("")
        self.btnCancelar.setText(QCoreApplication.translate("EmpleadoForm", u"Cancelar", None))
        self.btnGuardar.setText(QCoreApplication.translate("EmpleadoForm", u"Guardar", None))
    # retranslateUi

