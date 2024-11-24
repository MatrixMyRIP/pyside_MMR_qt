# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(390, 135)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(200, 135))
        Form.setMaximumSize(QSize(500, 135))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labellogin = QLabel(Form)
        self.labellogin.setObjectName(u"labellogin")
        self.labellogin.setMinimumSize(QSize(80, 20))

        self.horizontalLayout.addWidget(self.labellogin)

        self.lineEditloginenter = QLineEdit(Form)
        self.lineEditloginenter.setObjectName(u"lineEditloginenter")

        self.horizontalLayout.addWidget(self.lineEditloginenter)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.labelpassenter = QLabel(Form)
        self.labelpassenter.setObjectName(u"labelpassenter")
        self.labelpassenter.setMinimumSize(QSize(80, 20))

        self.horizontalLayout_2.addWidget(self.labelpassenter)

        self.labelpassword = QLineEdit(Form)
        self.labelpassword.setObjectName(u"labelpassword")
        self.labelpassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_2.addWidget(self.labelpassword)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonlogin = QPushButton(Form)
        self.pushButtonlogin.setObjectName(u"pushButtonlogin")

        self.horizontalLayout_3.addWidget(self.pushButtonlogin)

        self.pushButtoncancel = QPushButton(Form)
        self.pushButtoncancel.setObjectName(u"pushButtoncancel")

        self.horizontalLayout_3.addWidget(self.pushButtoncancel)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.pushButtonreg = QPushButton(Form)
        self.pushButtonreg.setObjectName(u"pushButtonreg")

        self.verticalLayout.addWidget(self.pushButtonreg)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.labellogin.setText(QCoreApplication.translate("Form", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.lineEditloginenter.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043b\u043e\u0433\u0438\u043d", None))
        self.labelpassenter.setText(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.labelpassword.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u043f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButtonlogin.setText(QCoreApplication.translate("Form", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.pushButtoncancel.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.pushButtonreg.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f", None))
    # retranslateUi

