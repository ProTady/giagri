# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'v_reconocimiento_vivo.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_ReconocimientoVivo(object):
    def setupUi(self, ReconocimientoVivo):
        if not ReconocimientoVivo.objectName():
            ReconocimientoVivo.setObjectName(u"ReconocimientoVivo")
        ReconocimientoVivo.resize(1100, 620)
        self.lytRoot = QVBoxLayout(ReconocimientoVivo)
        self.lytRoot.setSpacing(14)
        self.lytRoot.setObjectName(u"lytRoot")
        self.lytRoot.setContentsMargins(20, 20, 20, 20)
        self.lytTit = QHBoxLayout()
        self.lytTit.setObjectName(u"lytTit")
        self.lblTitulo = QLabel(ReconocimientoVivo)
        self.lblTitulo.setObjectName(u"lblTitulo")

        self.lytTit.addWidget(self.lblTitulo)

        self.spT = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.lytTit.addItem(self.spT)

        self.lblFps = QLabel(ReconocimientoVivo)
        self.lblFps.setObjectName(u"lblFps")

        self.lytTit.addWidget(self.lblFps)

        self.lblCount = QLabel(ReconocimientoVivo)
        self.lblCount.setObjectName(u"lblCount")

        self.lytTit.addWidget(self.lblCount)


        self.lytRoot.addLayout(self.lytTit)

        self.lytCuerpo = QHBoxLayout()
        self.lytCuerpo.setSpacing(14)
        self.lytCuerpo.setObjectName(u"lytCuerpo")
        self.lblVideo = QLabel(ReconocimientoVivo)
        self.lblVideo.setObjectName(u"lblVideo")
        self.lblVideo.setMinimumSize(QSize(720, 540))
        self.lblVideo.setAlignment(Qt.AlignCenter)
        self.lblVideo.setStyleSheet(u"background:#222; color:#aaa; border-radius:6px;")

        self.lytCuerpo.addWidget(self.lblVideo)

        self.lytLado = QVBoxLayout()
        self.lytLado.setSpacing(10)
        self.lytLado.setObjectName(u"lytLado")
        self.lblDeteccionTit = QLabel(ReconocimientoVivo)
        self.lblDeteccionTit.setObjectName(u"lblDeteccionTit")

        self.lytLado.addWidget(self.lblDeteccionTit)

        self.lstDetecciones = QListWidget(ReconocimientoVivo)
        self.lstDetecciones.setObjectName(u"lstDetecciones")
        self.lstDetecciones.setIconSize(QSize(48, 48))

        self.lytLado.addWidget(self.lstDetecciones)

        self.lytBtns = QHBoxLayout()
        self.lytBtns.setObjectName(u"lytBtns")
        self.btnRecargar = QPushButton(ReconocimientoVivo)
        self.btnRecargar.setObjectName(u"btnRecargar")
        self.btnRecargar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnRecargar)

        self.btnIniciar = QPushButton(ReconocimientoVivo)
        self.btnIniciar.setObjectName(u"btnIniciar")
        self.btnIniciar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnIniciar)

        self.btnDetener = QPushButton(ReconocimientoVivo)
        self.btnDetener.setObjectName(u"btnDetener")
        self.btnDetener.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.lytBtns.addWidget(self.btnDetener)


        self.lytLado.addLayout(self.lytBtns)


        self.lytCuerpo.addLayout(self.lytLado)


        self.lytRoot.addLayout(self.lytCuerpo)


        self.retranslateUi(ReconocimientoVivo)

        QMetaObject.connectSlotsByName(ReconocimientoVivo)
    # setupUi

    def retranslateUi(self, ReconocimientoVivo):
        self.lblTitulo.setText(QCoreApplication.translate("ReconocimientoVivo", u"Reconocimiento Facial en Vivo", None))
        self.lblFps.setText(QCoreApplication.translate("ReconocimientoVivo", u"FPS: --", None))
        self.lblCount.setText(QCoreApplication.translate("ReconocimientoVivo", u"Empleados con rostro: --", None))
        self.lblVideo.setText(QCoreApplication.translate("ReconocimientoVivo", u"Iniciando c\u00e1mara...", None))
        self.lblDeteccionTit.setText(QCoreApplication.translate("ReconocimientoVivo", u"Detecciones recientes", None))
        self.btnRecargar.setText(QCoreApplication.translate("ReconocimientoVivo", u"Recargar", None))
        self.btnIniciar.setText(QCoreApplication.translate("ReconocimientoVivo", u"Iniciar", None))
        self.btnDetener.setText(QCoreApplication.translate("ReconocimientoVivo", u"Detener", None))
        pass
    # retranslateUi

