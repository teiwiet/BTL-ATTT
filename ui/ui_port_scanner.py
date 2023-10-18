# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'port_scanner.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_port_scanner(object):
    def setupUi(self, port_scanner):
        if not port_scanner.objectName():
            port_scanner.setObjectName(u"port_scanner")
        port_scanner.resize(328, 96)
        self.horizontalLayout_2 = QHBoxLayout(port_scanner)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(port_scanner)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.line_edit_1 = QLineEdit(port_scanner)
        self.line_edit_1.setObjectName(u"line_edit_1")

        self.horizontalLayout.addWidget(self.line_edit_1)

        self.start_button = QPushButton(port_scanner)
        self.start_button.setObjectName(u"start_button")

        self.horizontalLayout.addWidget(self.start_button)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(port_scanner)

        QMetaObject.connectSlotsByName(port_scanner)
    # setupUi

    def retranslateUi(self, port_scanner):
        port_scanner.setWindowTitle(QCoreApplication.translate("port_scanner", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("port_scanner", u"Target:", None))
        self.start_button.setText(QCoreApplication.translate("port_scanner", u"Start", None))
    # retranslateUi

