# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'system_infokijhWj.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(245, 110)
        Form.setMinimumSize(QSize(245, 110))
        Form.setMaximumSize(QSize(245, 110))
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.CPULabel = QLabel(Form)
        self.CPULabel.setObjectName(u"CPULabel")
        self.CPULabel.setMinimumSize(QSize(125, 25))

        self.verticalLayout.addWidget(self.CPULabel)

        self.RAMLabel = QLabel(Form)
        self.RAMLabel.setObjectName(u"RAMLabel")
        self.RAMLabel.setMinimumSize(QSize(125, 25))

        self.verticalLayout.addWidget(self.RAMLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Delaylabel = QLabel(Form)
        self.Delaylabel.setObjectName(u"Delaylabel")
        self.Delaylabel.setMinimumSize(QSize(100, 25))

        self.horizontalLayout.addWidget(self.Delaylabel)

        self.DelayLineEdit = QLineEdit(Form)
        self.DelayLineEdit.setObjectName(u"DelayLineEdit")
        self.DelayLineEdit.setMinimumSize(QSize(100, 25))

        self.horizontalLayout.addWidget(self.DelayLineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"SystemInfo", None))
        self.CPULabel.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 CPU: ", None))
        self.RAMLabel.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 RAM: ", None))
        self.Delaylabel.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u043c\u044f \u0437\u0430\u0434\u0435\u0440\u0436\u043a\u0438", None))
        self.DelayLineEdit.setText(QCoreApplication.translate("Form", u"1", None))
    # retranslateUi

