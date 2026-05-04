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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QListView, QListWidget, QListWidgetItem, QProgressBar,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CapturarRostro(object):
    def setupUi(self, CapturarRostro):
        if not CapturarRostro.objectName():
            CapturarRostro.setObjectName(u"CapturarRostro")
        CapturarRostro.resize(900, 660)
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

        self.lytCuerpo = QHBoxLayout()
        self.lytCuerpo.setSpacing(14)
        self.lytCuerpo.setObjectName(u"lytCuerpo")
        self.lytIzq = QVBoxLayout()
        self.lytIzq.setObjectName(u"lytIzq")
        self.lblVideo = QLabel(CapturarRostro)
        self.lblVideo.setObjectName(u"lblVideo")
        self.lblVideo.setMinimumSize(QSize(560, 420))
        self.lblVideo.setAlignment(Qt.AlignCenter)
        self.lblVideo.setStyleSheet(u"background:#222; color:#aaa; border-radius:6px;")

        self.lytIzq.addWidget(self.lblVideo)

        self.lblInstr = QLabel(CapturarRostro)
        self.lblInstr.setObjectName(u"lblInstr")
        self.lblInstr.setAlignment(Qt.AlignCenter)
        self.lblInstr.setMinimumSize(QSize(0, 40))

        self.lytIzq.addWidget(self.lblInstr)

        self.prgEstable = QProgressBar(CapturarRostro)
        self.prgEstable.setObjectName(u"prgEstable")
        self.prgEstable.setValue(0)
        self.prgEstable.setTextVisible(False)
        self.prgEstable.setMaximum(100)
        self.prgEstable.setMaximumSize(QSize(16777215, 10))

        self.lytIzq.addWidget(self.prgEstable)


        self.lytCuerpo.addLayout(self.lytIzq)

        self.lytLado = QVBoxLayout()
        self.lytLado.setSpacing(10)
        self.lytLado.setObjectName(u"lytLado")
        self.lblPasoTit = QLabel(CapturarRostro)
        self.lblPasoTit.setObjectName(u"lblPasoTit")

        self.lytLado.addWidget(self.lblPasoTit)

        self.lstObjetivos = QListWidget(CapturarRostro)
        self.lstObjetivos.setObjectName(u"lstObjetivos")
        self.lstObjetivos.setIconSize(QSize(32, 32))
        self.lstObjetivos.setMinimumSize(QSize(240, 0))
        self.lstObjetivos.setMaximumSize(QSize(280, 16777215))

        self.lytLado.addWidget(self.lstObjetivos)

        self.lblYaReg = QLabel(CapturarRostro)
        self.lblYaReg.setObjectName(u"lblYaReg")

        self.lytLado.addWidget(self.lblYaReg)

        self.lstRegistrados = QListWidget(CapturarRostro)
        self.lstRegistrados.setObjectName(u"lstRegistrados")
        self.lstRegistrados.setIconSize(QSize(56, 56))
        self.lstRegistrados.setViewMode(QListView.IconMode)
        self.lstRegistrados.setResizeMode(QListView.Adjust)
        self.lstRegistrados.setMovement(QListView.Static)

        self.lytLado.addWidget(self.lstRegistrados)

        self.btnEliminarSel = QPushButton(CapturarRostro)
        self.btnEliminarSel.setObjectName(u"btnEliminarSel")
        self.btnEliminarSel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytLado.addWidget(self.btnEliminarSel)


        self.lytCuerpo.addLayout(self.lytLado)


        self.lytRoot.addLayout(self.lytCuerpo)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.btnReiniciar = QPushButton(CapturarRostro)
        self.btnReiniciar.setObjectName(u"btnReiniciar")
        self.btnReiniciar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnReiniciar)

        self.btnCapturarManual = QPushButton(CapturarRostro)
        self.btnCapturarManual.setObjectName(u"btnCapturarManual")
        self.btnCapturarManual.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnCapturarManual)

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
        self.lblVideo.setText(QCoreApplication.translate("CapturarRostro", u"Iniciando c\u00e1mara...", None))
        self.lblInstr.setText(QCoreApplication.translate("CapturarRostro", u"Ac\u00e9rcate a la c\u00e1mara", None))
        self.lblPasoTit.setText(QCoreApplication.translate("CapturarRostro", u"Capturas", None))
        self.lblYaReg.setText(QCoreApplication.translate("CapturarRostro", u"Registrados", None))
        self.btnEliminarSel.setText(QCoreApplication.translate("CapturarRostro", u"Eliminar seleccionado", None))
        self.btnReiniciar.setText(QCoreApplication.translate("CapturarRostro", u"Reiniciar gu\u00eda", None))
        self.btnCapturarManual.setText(QCoreApplication.translate("CapturarRostro", u"Capturar manual", None))
        self.btnCerrar.setText(QCoreApplication.translate("CapturarRostro", u"Cerrar", None))
    # retranslateUi

