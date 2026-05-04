# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_capturar_rostro.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QLabel, QListView, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CapturarRostro(object):
    def setupUi(self, CapturarRostro):
        if not CapturarRostro.objectName():
            CapturarRostro.setObjectName(u"CapturarRostro")
        CapturarRostro.resize(820, 620)
        self.lytRoot = QVBoxLayout(CapturarRostro)
        self.lytRoot.setSpacing(10)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(16, 14, 16, 14)
        self.lblTitulo = QLabel(CapturarRostro)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytRoot.addWidget(self.lblTitulo)

        self.lblEmpleado = QLabel(CapturarRostro)
        self.lblEmpleado.setObjectName(u"lblEmpleado")

        self.lytRoot.addWidget(self.lblEmpleado)

        self.lblInstr = QLabel(CapturarRostro)
        self.lblInstr.setObjectName(u"lblInstr")
        self.lblInstr.setWordWrap(True)

        self.lytRoot.addWidget(self.lblInstr)

        self.lytCuerpo = QHBoxLayout()
        self.lytCuerpo.setSpacing(14)
        self.lytCuerpo.setObjectName(u"lytCuerpo")
        self.lblVideo = QLabel(CapturarRostro)
        self.lblVideo.setObjectName(u"lblVideo")
        self.lblVideo.setMinimumSize(QSize(500, 400))
        self.lblVideo.setAlignment(Qt.AlignCenter)
        self.lblVideo.setStyleSheet(u"background:#222; color:#aaa; border-radius:6px;")

        self.lytCuerpo.addWidget(self.lblVideo)

        self.lytLado = QVBoxLayout()
        self.lytLado.setSpacing(10)
        self.lytLado.setObjectName(u"lytLado")
        self.lblEstado = QLabel(CapturarRostro)
        self.lblEstado.setObjectName(u"lblEstado")

        self.lytLado.addWidget(self.lblEstado)

        self.lblCalidad = QLabel(CapturarRostro)
        self.lblCalidad.setObjectName(u"lblCalidad")

        self.lytLado.addWidget(self.lblCalidad)

        self.lblConteo = QLabel(CapturarRostro)
        self.lblConteo.setObjectName(u"lblConteo")

        self.lytLado.addWidget(self.lblConteo)

        self.cboAngulo = QComboBox(CapturarRostro)
        self.cboAngulo.addItem("")
        self.cboAngulo.addItem("")
        self.cboAngulo.addItem("")
        self.cboAngulo.addItem("")
        self.cboAngulo.addItem("")
        self.cboAngulo.setObjectName(u"cboAngulo")

        self.lytLado.addWidget(self.cboAngulo)

        self.btnCapturar = QPushButton(CapturarRostro)
        self.btnCapturar.setObjectName(u"btnCapturar")
        self.btnCapturar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCapturar.setMinimumSize(QSize(0, 40))

        self.lytLado.addWidget(self.btnCapturar)

        self.spLado = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.lytLado.addItem(self.spLado)

        self.lblYaReg = QLabel(CapturarRostro)
        self.lblYaReg.setObjectName(u"lblYaReg")

        self.lytLado.addWidget(self.lblYaReg)

        self.lstRegistrados = QListWidget(CapturarRostro)
        self.lstRegistrados.setObjectName(u"lstRegistrados")
        self.lstRegistrados.setIconSize(QSize(64, 64))
        self.lstRegistrados.setViewMode(QListView.IconMode)
        self.lstRegistrados.setResizeMode(QListView.Adjust)
        self.lstRegistrados.setMovement(QListView.Static)
        self.lstRegistrados.setMinimumSize(QSize(240, 0))

        self.lytLado.addWidget(self.lstRegistrados)

        self.btnEliminarSel = QPushButton(CapturarRostro)
        self.btnEliminarSel.setObjectName(u"btnEliminarSel")
        self.btnEliminarSel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytLado.addWidget(self.btnEliminarSel)


        self.lytCuerpo.addLayout(self.lytLado)


        self.lytRoot.addLayout(self.lytCuerpo)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.spB = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytBtns.addItem(self.spB)

        self.btnCerrar = QPushButton(CapturarRostro)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnCerrar)


        self.lytRoot.addLayout(self.lytBtns)


        self.retranslateUi(CapturarRostro)

        QMetaObject.connectSlotsByName(CapturarRostro)
    # setupUi

    def retranslateUi(self, CapturarRostro):
        CapturarRostro.setWindowTitle(QCoreApplication.translate("CapturarRostro", u"Registrar Rostro", None))
        self.lblTitulo.setText(QCoreApplication.translate("CapturarRostro", u"Registrar Rostro", None))
        self.lblEmpleado.setText(QCoreApplication.translate("CapturarRostro", u"Empleado", None))
        self.lblInstr.setText(QCoreApplication.translate("CapturarRostro", u"Mira a la c\u00e1mara y presiona \"Capturar\". Captura al menos 3 fotos en distintos \u00e1ngulos (frente, izquierda, derecha).", None))
        self.lblVideo.setText(QCoreApplication.translate("CapturarRostro", u"Iniciando c\u00e1mara...", None))
        self.lblEstado.setText(QCoreApplication.translate("CapturarRostro", u"Detectando rostro...", None))
        self.lblCalidad.setText(QCoreApplication.translate("CapturarRostro", u"Calidad: --", None))
        self.lblConteo.setText(QCoreApplication.translate("CapturarRostro", u"Capturados: 0", None))
        self.cboAngulo.setItemText(0, QCoreApplication.translate("CapturarRostro", u"Frente", None))
        self.cboAngulo.setItemText(1, QCoreApplication.translate("CapturarRostro", u"Izquierda", None))
        self.cboAngulo.setItemText(2, QCoreApplication.translate("CapturarRostro", u"Derecha", None))
        self.cboAngulo.setItemText(3, QCoreApplication.translate("CapturarRostro", u"Arriba", None))
        self.cboAngulo.setItemText(4, QCoreApplication.translate("CapturarRostro", u"Abajo", None))

        self.btnCapturar.setText(QCoreApplication.translate("CapturarRostro", u"Capturar", None))
        self.lblYaReg.setText(QCoreApplication.translate("CapturarRostro", u"Ya registrados:", None))
        self.btnEliminarSel.setText(QCoreApplication.translate("CapturarRostro", u"Eliminar seleccionado", None))
        self.btnCerrar.setText(QCoreApplication.translate("CapturarRostro", u"Cerrar", None))
    # retranslateUi

