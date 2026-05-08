# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_tareo_masivo.ui'
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
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_TareoMasivo(object):
    def setupUi(self, TareoMasivo):
        if not TareoMasivo.objectName():
            TareoMasivo.setObjectName(u"TareoMasivo")
        TareoMasivo.resize(820, 700)
        self.lytRoot = QVBoxLayout(TareoMasivo)
        self.lytRoot.setSpacing(10)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 16, 20, 16)
        self.lblTitulo = QLabel(TareoMasivo)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.lblSub = QLabel(TareoMasivo)
        self.lblSub.setObjectName(u"lblSub")

        self.lytRoot.addWidget(self.lblSub)

        self.lineSep = QFrame(TareoMasivo)
        self.lineSep.setObjectName(u"lineSep")
        self.lineSep.setFrameShape(QFrame.HLine)
        self.lineSep.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep)

        self.lytCuerpo = QHBoxLayout()
        self.lytCuerpo.setSpacing(16)
        self.lytCuerpo.setObjectName(u"lytCuerpo")
        self.lytForm = QFormLayout()
        self.lytForm.setObjectName(u"lytForm")
        self.lytForm.setHorizontalSpacing(12)
        self.lytForm.setVerticalSpacing(10)
        self.lytForm.setLabelAlignment(Qt.AlignRight|Qt.AlignVCenter)
        self.l1 = QLabel(TareoMasivo)
        self.l1.setObjectName(u"l1")

        self.lytForm.setWidget(0, QFormLayout.LabelRole, self.l1)

        self.dtFecha = QDateEdit(TareoMasivo)
        self.dtFecha.setObjectName(u"dtFecha")
        self.dtFecha.setCalendarPopup(True)

        self.lytForm.setWidget(0, QFormLayout.FieldRole, self.dtFecha)

        self.l2 = QLabel(TareoMasivo)
        self.l2.setObjectName(u"l2")

        self.lytForm.setWidget(1, QFormLayout.LabelRole, self.l2)

        self.cboLote = QComboBox(TareoMasivo)
        self.cboLote.setObjectName(u"cboLote")

        self.lytForm.setWidget(1, QFormLayout.FieldRole, self.cboLote)

        self.l3 = QLabel(TareoMasivo)
        self.l3.setObjectName(u"l3")

        self.lytForm.setWidget(2, QFormLayout.LabelRole, self.l3)

        self.cboActividad = QComboBox(TareoMasivo)
        self.cboActividad.setObjectName(u"cboActividad")

        self.lytForm.setWidget(2, QFormLayout.FieldRole, self.cboActividad)

        self.l4 = QLabel(TareoMasivo)
        self.l4.setObjectName(u"l4")

        self.lytForm.setWidget(3, QFormLayout.LabelRole, self.l4)

        self.cboLabor = QComboBox(TareoMasivo)
        self.cboLabor.setObjectName(u"cboLabor")

        self.lytForm.setWidget(3, QFormLayout.FieldRole, self.cboLabor)

        self.l5 = QLabel(TareoMasivo)
        self.l5.setObjectName(u"l5")

        self.lytForm.setWidget(4, QFormLayout.LabelRole, self.l5)

        self.cboCargo = QComboBox(TareoMasivo)
        self.cboCargo.setObjectName(u"cboCargo")

        self.lytForm.setWidget(4, QFormLayout.FieldRole, self.cboCargo)

        self.l6 = QLabel(TareoMasivo)
        self.l6.setObjectName(u"l6")

        self.lytForm.setWidget(5, QFormLayout.LabelRole, self.l6)

        self.spHM = QDoubleSpinBox(TareoMasivo)
        self.spHM.setObjectName(u"spHM")
        self.spHM.setMaximum(24.000000000000000)
        self.spHM.setDecimals(2)
        self.spHM.setValue(4.000000000000000)

        self.lytForm.setWidget(5, QFormLayout.FieldRole, self.spHM)

        self.l7 = QLabel(TareoMasivo)
        self.l7.setObjectName(u"l7")

        self.lytForm.setWidget(6, QFormLayout.LabelRole, self.l7)

        self.spHT = QDoubleSpinBox(TareoMasivo)
        self.spHT.setObjectName(u"spHT")
        self.spHT.setMaximum(24.000000000000000)
        self.spHT.setDecimals(2)
        self.spHT.setValue(4.000000000000000)

        self.lytForm.setWidget(6, QFormLayout.FieldRole, self.spHT)

        self.l8 = QLabel(TareoMasivo)
        self.l8.setObjectName(u"l8")

        self.lytForm.setWidget(7, QFormLayout.LabelRole, self.l8)

        self.spHE = QDoubleSpinBox(TareoMasivo)
        self.spHE.setObjectName(u"spHE")
        self.spHE.setMaximum(24.000000000000000)
        self.spHE.setDecimals(2)

        self.lytForm.setWidget(7, QFormLayout.FieldRole, self.spHE)

        self.l9 = QLabel(TareoMasivo)
        self.l9.setObjectName(u"l9")

        self.lytForm.setWidget(8, QFormLayout.LabelRole, self.l9)

        self.txtComent = QLineEdit(TareoMasivo)
        self.txtComent.setObjectName(u"txtComent")

        self.lytForm.setWidget(8, QFormLayout.FieldRole, self.txtComent)


        self.lytCuerpo.addLayout(self.lytForm)

        self.lytLado = QVBoxLayout()
        self.lytLado.setSpacing(8)
        self.lytLado.setObjectName(u"lytLado")
        self.lblEmpTit = QLabel(TareoMasivo)
        self.lblEmpTit.setObjectName(u"lblEmpTit")

        self.lytLado.addWidget(self.lblEmpTit)

        self.txtBuscar = QLineEdit(TareoMasivo)
        self.txtBuscar.setObjectName(u"txtBuscar")

        self.lytLado.addWidget(self.txtBuscar)

        self.lytAccTodos = QHBoxLayout()
        self.lytAccTodos.setObjectName(u"lytAccTodos")
        self.btnTodos = QPushButton(TareoMasivo)
        self.btnTodos.setObjectName(u"btnTodos")
        self.btnTodos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytAccTodos.addWidget(self.btnTodos)

        self.btnNinguno = QPushButton(TareoMasivo)
        self.btnNinguno.setObjectName(u"btnNinguno")
        self.btnNinguno.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytAccTodos.addWidget(self.btnNinguno)

        self.btnInvertir = QPushButton(TareoMasivo)
        self.btnInvertir.setObjectName(u"btnInvertir")
        self.btnInvertir.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytAccTodos.addWidget(self.btnInvertir)


        self.lytLado.addLayout(self.lytAccTodos)

        self.lstEmpleados = QListWidget(TareoMasivo)
        self.lstEmpleados.setObjectName(u"lstEmpleados")
        self.lstEmpleados.setMinimumSize(QSize(320, 0))

        self.lytLado.addWidget(self.lstEmpleados)


        self.lytCuerpo.addLayout(self.lytLado)


        self.lytRoot.addLayout(self.lytCuerpo)

        self.lblResumen = QLabel(TareoMasivo)
        self.lblResumen.setObjectName(u"lblResumen")

        self.lytRoot.addWidget(self.lblResumen)

        self.lblError = QLabel(TareoMasivo)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setMinimumSize(QSize(0, 18))

        self.lytRoot.addWidget(self.lblError)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.spB = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtns.addItem(self.spB)

        self.btnCancelar = QPushButton(TareoMasivo)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnCancelar)

        self.btnGuardar = QPushButton(TareoMasivo)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnGuardar)


        self.lytRoot.addLayout(self.lytBtns)


        self.retranslateUi(TareoMasivo)

        self.btnGuardar.setDefault(True)


        QMetaObject.connectSlotsByName(TareoMasivo)
    # setupUi

    def retranslateUi(self, TareoMasivo):
        TareoMasivo.setWindowTitle(QCoreApplication.translate("TareoMasivo", u"Tareo Masivo \u2014 Cuadrilla", None))
        self.lblTitulo.setText(QCoreApplication.translate("TareoMasivo", u"Tareo Masivo", None))
        self.lblSub.setText(QCoreApplication.translate("TareoMasivo", u"Varias personas realizando la misma labor en el mismo lote y horario.", None))
        self.l1.setText(QCoreApplication.translate("TareoMasivo", u"Fecha *", None))
        self.dtFecha.setDisplayFormat(QCoreApplication.translate("TareoMasivo", u"dd/MM/yyyy", None))
        self.l2.setText(QCoreApplication.translate("TareoMasivo", u"Lote *", None))
        self.l3.setText(QCoreApplication.translate("TareoMasivo", u"Actividad", None))
        self.l4.setText(QCoreApplication.translate("TareoMasivo", u"Labor *", None))
        self.l5.setText(QCoreApplication.translate("TareoMasivo", u"Cargo com\u00fan", None))
        self.l6.setText(QCoreApplication.translate("TareoMasivo", u"Horas Ma\u00f1ana", None))
        self.spHM.setSuffix(QCoreApplication.translate("TareoMasivo", u" h", None))
        self.l7.setText(QCoreApplication.translate("TareoMasivo", u"Horas Tarde", None))
        self.spHT.setSuffix(QCoreApplication.translate("TareoMasivo", u" h", None))
        self.l8.setText(QCoreApplication.translate("TareoMasivo", u"Horas Extras", None))
        self.spHE.setSuffix(QCoreApplication.translate("TareoMasivo", u" h", None))
        self.l9.setText(QCoreApplication.translate("TareoMasivo", u"Comentario", None))
        self.lblEmpTit.setText(QCoreApplication.translate("TareoMasivo", u"Empleados (selecciona)", None))
        self.txtBuscar.setPlaceholderText(QCoreApplication.translate("TareoMasivo", u"Buscar por c\u00f3digo, apellido o nombre...", None))
        self.btnTodos.setText(QCoreApplication.translate("TareoMasivo", u"Todos", None))
        self.btnNinguno.setText(QCoreApplication.translate("TareoMasivo", u"Ninguno", None))
        self.btnInvertir.setText(QCoreApplication.translate("TareoMasivo", u"Invertir", None))
        self.lblResumen.setText(QCoreApplication.translate("TareoMasivo", u"Seleccionados: 0  \u00b7  Total horas: 0  \u00b7  Bono total: S/. 0.00", None))
        self.lblError.setText("")
        self.btnCancelar.setText(QCoreApplication.translate("TareoMasivo", u"Cancelar", None))
        self.btnGuardar.setText(QCoreApplication.translate("TareoMasivo", u"Guardar tareos", None))
    # retranslateUi

