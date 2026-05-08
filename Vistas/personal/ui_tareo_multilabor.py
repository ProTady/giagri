# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_tareo_multilabor.ui'
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
    QHeaderView, QLabel, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_TareoMultiLabor(object):
    def setupUi(self, TareoMultiLabor):
        if not TareoMultiLabor.objectName():
            TareoMultiLabor.setObjectName(u"TareoMultiLabor")
        TareoMultiLabor.resize(980, 660)
        self.lytRoot = QVBoxLayout(TareoMultiLabor)
        self.lytRoot.setSpacing(10)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 16, 20, 16)
        self.lblTitulo = QLabel(TareoMultiLabor)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.lblSub = QLabel(TareoMultiLabor)
        self.lblSub.setObjectName(u"lblSub")

        self.lytRoot.addWidget(self.lblSub)

        self.lineSep1 = QFrame(TareoMultiLabor)
        self.lineSep1.setObjectName(u"lineSep1")
        self.lineSep1.setFrameShape(QFrame.HLine)
        self.lineSep1.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep1)

        self.lytEnc = QHBoxLayout()
        self.lytEnc.setSpacing(14)
        self.lytEnc.setObjectName(u"lytEnc")
        self.l1 = QLabel(TareoMultiLabor)
        self.l1.setObjectName(u"l1")

        self.lytEnc.addWidget(self.l1)

        self.dtFecha = QDateEdit(TareoMultiLabor)
        self.dtFecha.setObjectName(u"dtFecha")
        self.dtFecha.setCalendarPopup(True)

        self.lytEnc.addWidget(self.dtFecha)

        self.l2 = QLabel(TareoMultiLabor)
        self.l2.setObjectName(u"l2")

        self.lytEnc.addWidget(self.l2)

        self.cboEmpleado = QComboBox(TareoMultiLabor)
        self.cboEmpleado.setObjectName(u"cboEmpleado")
        self.cboEmpleado.setEditable(True)
        self.cboEmpleado.setInsertPolicy(QComboBox.NoInsert)
        self.cboEmpleado.setMinimumSize(QSize(320, 0))

        self.lytEnc.addWidget(self.cboEmpleado)

        self.l3 = QLabel(TareoMultiLabor)
        self.l3.setObjectName(u"l3")

        self.lytEnc.addWidget(self.l3)

        self.cboCargo = QComboBox(TareoMultiLabor)
        self.cboCargo.setObjectName(u"cboCargo")

        self.lytEnc.addWidget(self.cboCargo)

        self.spE = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytEnc.addItem(self.spE)


        self.lytRoot.addLayout(self.lytEnc)

        self.lineSep2 = QFrame(TareoMultiLabor)
        self.lineSep2.setObjectName(u"lineSep2")
        self.lineSep2.setFrameShape(QFrame.HLine)
        self.lineSep2.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep2)

        self.lblFila = QLabel(TareoMultiLabor)
        self.lblFila.setObjectName(u"lblFila")
        self.lblFila.setStyleSheet(u"font-weight:bold;")

        self.lytRoot.addWidget(self.lblFila)

        self.lytFila = QHBoxLayout()
        self.lytFila.setSpacing(8)
        self.lytFila.setObjectName(u"lytFila")
        self.lytF1 = QFormLayout()
        self.lytF1.setObjectName(u"lytF1")
        self.lytF1.setHorizontalSpacing(10)
        self.lytF1.setVerticalSpacing(6)
        self.lf1 = QLabel(TareoMultiLabor)
        self.lf1.setObjectName(u"lf1")

        self.lytF1.setWidget(0, QFormLayout.LabelRole, self.lf1)

        self.cboLote = QComboBox(TareoMultiLabor)
        self.cboLote.setObjectName(u"cboLote")

        self.lytF1.setWidget(0, QFormLayout.FieldRole, self.cboLote)

        self.lf2 = QLabel(TareoMultiLabor)
        self.lf2.setObjectName(u"lf2")

        self.lytF1.setWidget(1, QFormLayout.LabelRole, self.lf2)

        self.cboActividad = QComboBox(TareoMultiLabor)
        self.cboActividad.setObjectName(u"cboActividad")

        self.lytF1.setWidget(1, QFormLayout.FieldRole, self.cboActividad)

        self.lf3 = QLabel(TareoMultiLabor)
        self.lf3.setObjectName(u"lf3")

        self.lytF1.setWidget(2, QFormLayout.LabelRole, self.lf3)

        self.cboLabor = QComboBox(TareoMultiLabor)
        self.cboLabor.setObjectName(u"cboLabor")

        self.lytF1.setWidget(2, QFormLayout.FieldRole, self.cboLabor)


        self.lytFila.addLayout(self.lytF1)

        self.lytF2 = QFormLayout()
        self.lytF2.setObjectName(u"lytF2")
        self.lytF2.setHorizontalSpacing(10)
        self.lytF2.setVerticalSpacing(6)
        self.lf4 = QLabel(TareoMultiLabor)
        self.lf4.setObjectName(u"lf4")

        self.lytF2.setWidget(0, QFormLayout.LabelRole, self.lf4)

        self.spHM = QDoubleSpinBox(TareoMultiLabor)
        self.spHM.setObjectName(u"spHM")
        self.spHM.setMaximum(24.000000000000000)
        self.spHM.setDecimals(2)

        self.lytF2.setWidget(0, QFormLayout.FieldRole, self.spHM)

        self.lf5 = QLabel(TareoMultiLabor)
        self.lf5.setObjectName(u"lf5")

        self.lytF2.setWidget(1, QFormLayout.LabelRole, self.lf5)

        self.spHT = QDoubleSpinBox(TareoMultiLabor)
        self.spHT.setObjectName(u"spHT")
        self.spHT.setMaximum(24.000000000000000)
        self.spHT.setDecimals(2)

        self.lytF2.setWidget(1, QFormLayout.FieldRole, self.spHT)

        self.lf6 = QLabel(TareoMultiLabor)
        self.lf6.setObjectName(u"lf6")

        self.lytF2.setWidget(2, QFormLayout.LabelRole, self.lf6)

        self.spHE = QDoubleSpinBox(TareoMultiLabor)
        self.spHE.setObjectName(u"spHE")
        self.spHE.setMaximum(24.000000000000000)
        self.spHE.setDecimals(2)

        self.lytF2.setWidget(2, QFormLayout.FieldRole, self.spHE)


        self.lytFila.addLayout(self.lytF2)

        self.lytF3 = QVBoxLayout()
        self.lytF3.setSpacing(6)
        self.lytF3.setObjectName(u"lytF3")
        self.lf7 = QLabel(TareoMultiLabor)
        self.lf7.setObjectName(u"lf7")

        self.lytF3.addWidget(self.lf7)

        self.txtComent = QPlainTextEdit(TareoMultiLabor)
        self.txtComent.setObjectName(u"txtComent")
        self.txtComent.setMaximumSize(QSize(16777215, 80))

        self.lytF3.addWidget(self.txtComent)

        self.btnAgregar = QPushButton(TareoMultiLabor)
        self.btnAgregar.setObjectName(u"btnAgregar")
        self.btnAgregar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytF3.addWidget(self.btnAgregar)


        self.lytFila.addLayout(self.lytF3)


        self.lytRoot.addLayout(self.lytFila)

        self.lineSep3 = QFrame(TareoMultiLabor)
        self.lineSep3.setObjectName(u"lineSep3")
        self.lineSep3.setFrameShape(QFrame.HLine)
        self.lineSep3.setFrameShadow(QFrame.Plain)

        self.lytRoot.addWidget(self.lineSep3)

        self.lblListaTit = QLabel(TareoMultiLabor)
        self.lblListaTit.setObjectName(u"lblListaTit")
        self.lblListaTit.setStyleSheet(u"font-weight:bold;")

        self.lytRoot.addWidget(self.lblListaTit)

        self.tblFilas = QTableWidget(TareoMultiLabor)
        self.tblFilas.setObjectName(u"tblFilas")

        self.lytRoot.addWidget(self.tblFilas)

        self.lytAcc = QHBoxLayout()
        self.lytAcc.setObjectName(u"lytAcc")
        self.btnQuitar = QPushButton(TareoMultiLabor)
        self.btnQuitar.setObjectName(u"btnQuitar")
        self.btnQuitar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytAcc.addWidget(self.btnQuitar)

        self.sp1 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytAcc.addItem(self.sp1)

        self.lblTotales = QLabel(TareoMultiLabor)
        self.lblTotales.setObjectName(u"lblTotales")

        self.lytAcc.addWidget(self.lblTotales)


        self.lytRoot.addLayout(self.lytAcc)

        self.lblError = QLabel(TareoMultiLabor)
        self.lblError.setObjectName(u"lblError")
        self.lblError.setMinimumSize(QSize(0, 18))

        self.lytRoot.addWidget(self.lblError)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.sp2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtns.addItem(self.sp2)

        self.btnCancelar = QPushButton(TareoMultiLabor)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnCancelar)

        self.btnGuardar = QPushButton(TareoMultiLabor)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnGuardar)


        self.lytRoot.addLayout(self.lytBtns)


        self.retranslateUi(TareoMultiLabor)

        self.btnGuardar.setDefault(True)


        QMetaObject.connectSlotsByName(TareoMultiLabor)
    # setupUi

    def retranslateUi(self, TareoMultiLabor):
        TareoMultiLabor.setWindowTitle(QCoreApplication.translate("TareoMultiLabor", u"Tareo M\u00faltiples Labores", None))
        self.lblTitulo.setText(QCoreApplication.translate("TareoMultiLabor", u"Tareo M\u00faltiples Labores", None))
        self.lblSub.setText(QCoreApplication.translate("TareoMultiLabor", u"Un empleado realizando varias labores en uno o varios lotes en el d\u00eda.", None))
        self.l1.setText(QCoreApplication.translate("TareoMultiLabor", u"Fecha:", None))
        self.dtFecha.setDisplayFormat(QCoreApplication.translate("TareoMultiLabor", u"dd/MM/yyyy", None))
        self.l2.setText(QCoreApplication.translate("TareoMultiLabor", u"Empleado:", None))
        self.l3.setText(QCoreApplication.translate("TareoMultiLabor", u"Cargo com\u00fan:", None))
        self.lblFila.setText(QCoreApplication.translate("TareoMultiLabor", u"Agregar fila a la lista", None))
        self.lf1.setText(QCoreApplication.translate("TareoMultiLabor", u"Lote:", None))
        self.lf2.setText(QCoreApplication.translate("TareoMultiLabor", u"Actividad:", None))
        self.lf3.setText(QCoreApplication.translate("TareoMultiLabor", u"Labor:", None))
        self.lf4.setText(QCoreApplication.translate("TareoMultiLabor", u"H. Ma\u00f1ana:", None))
        self.spHM.setSuffix(QCoreApplication.translate("TareoMultiLabor", u" h", None))
        self.lf5.setText(QCoreApplication.translate("TareoMultiLabor", u"H. Tarde:", None))
        self.spHT.setSuffix(QCoreApplication.translate("TareoMultiLabor", u" h", None))
        self.lf6.setText(QCoreApplication.translate("TareoMultiLabor", u"H. Extras:", None))
        self.spHE.setSuffix(QCoreApplication.translate("TareoMultiLabor", u" h", None))
        self.lf7.setText(QCoreApplication.translate("TareoMultiLabor", u"Comentario:", None))
        self.btnAgregar.setText(QCoreApplication.translate("TareoMultiLabor", u"+ Agregar a la lista", None))
        self.lblListaTit.setText(QCoreApplication.translate("TareoMultiLabor", u"Filas pendientes de guardar", None))
        self.btnQuitar.setText(QCoreApplication.translate("TareoMultiLabor", u"Quitar fila seleccionada", None))
        self.lblTotales.setText(QCoreApplication.translate("TareoMultiLabor", u"Total: 0 filas \u00b7 0.00 h \u00b7 S/. 0.00", None))
        self.lblError.setText("")
        self.btnCancelar.setText(QCoreApplication.translate("TareoMultiLabor", u"Cancelar", None))
        self.btnGuardar.setText(QCoreApplication.translate("TareoMultiLabor", u"Guardar todo", None))
    # retranslateUi

