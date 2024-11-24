# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ship_parambfpkrU.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(325, 200)
        Form.setMinimumSize(QSize(325, 200))
        Form.setMaximumSize(QSize(16777215, 200))
        Form.setStyleSheet(u"background-color: rgb(136, 136, 136);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.temp_bort = QLabel(self.groupBox)
        self.temp_bort.setObjectName(u"temp_bort")
        self.temp_bort.setMinimumSize(QSize(150, 0))
        self.temp_bort.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.temp_bort.setFont(font1)

        self.horizontalLayout_2.addWidget(self.temp_bort)

        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: rgb(255, 170, 0);")
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.temp_bort_2 = QLabel(self.groupBox)
        self.temp_bort_2.setObjectName(u"temp_bort_2")
        self.temp_bort_2.setMinimumSize(QSize(150, 0))
        self.temp_bort_2.setFont(font1)

        self.horizontalLayout_3.addWidget(self.temp_bort_2)

        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.lineEdit_2.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.temp_bort_3 = QLabel(self.groupBox)
        self.temp_bort_3.setObjectName(u"temp_bort_3")
        self.temp_bort_3.setMinimumSize(QSize(150, 0))
        self.temp_bort_3.setFont(font1)

        self.horizontalLayout_4.addWidget(self.temp_bort_3)

        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.lineEdit_3.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.temp_bort_5 = QLabel(self.groupBox)
        self.temp_bort_5.setObjectName(u"temp_bort_5")
        self.temp_bort_5.setMinimumSize(QSize(150, 0))
        self.temp_bort_5.setFont(font1)

        self.horizontalLayout_6.addWidget(self.temp_bort_5)

        self.lineEdit_5 = QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.lineEdit_5.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.lineEdit_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.temp_bort_4 = QLabel(self.groupBox)
        self.temp_bort_4.setObjectName(u"temp_bort_4")
        self.temp_bort_4.setMinimumSize(QSize(150, 0))
        self.temp_bort_4.setFont(font1)

        self.horizontalLayout_5.addWidget(self.temp_bort_4)

        self.lineEdit_4 = QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.lineEdit_4.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.lineEdit_4)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.groupBox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u041f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u043a\u043e\u0440\u043e\u0431\u043b\u044f", None))
        self.temp_bort.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>\u0422\u0435\u043c\u043f\u0435\u0440\u0430\u0442\u0443\u0440\u0430 \u043d\u0430 \u0431\u043e\u0440\u0442\u0443</p></body></html>", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"22 \u0421", None))
        self.temp_bort_2.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u0433\u0435\u0440\u043c\u0435\u0442\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u0441\u0443\u0442\u0432\u0443\u0435\u0442", None))
        self.temp_bort_3.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21161", None))
        self.lineEdit_3.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.temp_bort_5.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21163", None))
        self.lineEdit_5.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
        self.temp_bort_4.setText(QCoreApplication.translate("Form", u"\u0411\u0430\u043a \u21162", None))
        self.lineEdit_4.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0440\u043c\u0430", None))
    # retranslateUi

