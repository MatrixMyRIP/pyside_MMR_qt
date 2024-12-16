# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weatherOqeyEo.ui'
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
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(371, 292)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_latedit = QLineEdit(Form)
        self.line_latedit.setObjectName(u"line_latedit")
        self.line_latedit.setMinimumSize(QSize(131, 21))

        self.horizontalLayout.addWidget(self.line_latedit)

        self.line_lonedit = QLineEdit(Form)
        self.line_lonedit.setObjectName(u"line_lonedit")
        self.line_lonedit.setMinimumSize(QSize(131, 21))

        self.horizontalLayout.addWidget(self.line_lonedit)

        self.start_stop_Button = QPushButton(Form)
        self.start_stop_Button.setObjectName(u"start_stop_Button")
        self.start_stop_Button.setText("Определить")
        self.start_stop_Button.setCheckable(True)
        self.start_stop_Button.setChecked(False)

        self.horizontalLayout.addWidget(self.start_stop_Button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEditDelay = QLineEdit(Form)
        self.lineEditDelay.setObjectName(u"lineEditDelay")
        self.lineEditDelay.setMinimumSize(QSize(131, 21))

        self.horizontalLayout_2.addWidget(self.lineEditDelay)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.plainTextEdit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Weather", None))
        self.line_latedit.setPlaceholderText(QCoreApplication.translate("Form", u"Latitude (\u0428\u0438\u0440\u043e\u0442\u0430)", None))
        self.line_lonedit.setPlaceholderText(QCoreApplication.translate("Form", u"Longitude (\u0414\u043e\u043b\u0433\u0430\u0442\u0430)", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u0434\u0435\u0440\u0436\u043a\u0430 (\u0441\u0435\u043a)", None))
    # retranslateUi

