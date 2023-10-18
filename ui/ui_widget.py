# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(252, 169)
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 20, 108, 116))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.port_scanner_button = QPushButton(self.widget)
        self.port_scanner_button.setObjectName(u"port_scanner_button")

        self.verticalLayout.addWidget(self.port_scanner_button)

        self.dos_button = QPushButton(self.widget)
        self.dos_button.setObjectName(u"dos_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dos_button.sizePolicy().hasHeightForWidth())
        self.dos_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.dos_button)

        self.sniffer_button = QPushButton(self.widget)
        self.sniffer_button.setObjectName(u"sniffer_button")

        self.verticalLayout.addWidget(self.sniffer_button)

        self.brute_force_button = QPushButton(self.widget)
        self.brute_force_button.setObjectName(u"brute_force_button")

        self.verticalLayout.addWidget(self.brute_force_button)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Form", None))
        self.port_scanner_button.setText(QCoreApplication.translate("Widget", u"Port scanner", None))
        self.dos_button.setText(QCoreApplication.translate("Widget", u"Dos", None))
        self.sniffer_button.setText(QCoreApplication.translate("Widget", u"Sniffer", None))
        self.brute_force_button.setText(QCoreApplication.translate("Widget", u"Brute Force", None))
    # retranslateUi

