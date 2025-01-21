# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'version_edithsyYGo.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(304, 106)
        Form.setStyleSheet(u"*{background-color:white;\n"
"border-bottom:1px solid black}\n"
"*:focus{border-bottom:1px solid rgb(0, 103, 192)}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_1_1 = QLineEdit(Form)
        self.lineEdit_1_1.setObjectName(u"lineEdit_1_1")
        self.lineEdit_1_1.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.lineEdit_1_1)

        self.lineEdit_1_2 = QLineEdit(Form)
        self.lineEdit_1_2.setObjectName(u"lineEdit_1_2")
        self.lineEdit_1_2.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.lineEdit_1_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit_2_1 = QLineEdit(Form)
        self.lineEdit_2_1.setObjectName(u"lineEdit_2_1")
        self.lineEdit_2_1.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.lineEdit_2_1)

        self.lineEdit_2_2 = QLineEdit(Form)
        self.lineEdit_2_2.setObjectName(u"lineEdit_2_2")
        self.lineEdit_2_2.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.lineEdit_2_2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_3_1 = QLineEdit(Form)
        self.lineEdit_3_1.setObjectName(u"lineEdit_3_1")
        self.lineEdit_3_1.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.lineEdit_3_1)

        self.lineEdit_3_2 = QLineEdit(Form)
        self.lineEdit_3_2.setObjectName(u"lineEdit_3_2")
        self.lineEdit_3_2.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.lineEdit_3_2)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_4_1 = QLineEdit(Form)
        self.lineEdit_4_1.setObjectName(u"lineEdit_4_1")
        self.lineEdit_4_1.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.lineEdit_4_1)

        self.lineEdit_4_2 = QLineEdit(Form)
        self.lineEdit_4_2.setObjectName(u"lineEdit_4_2")
        self.lineEdit_4_2.setStyleSheet(u"border:none")

        self.horizontalLayout.addWidget(self.lineEdit_4_2)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u".", None))
        self.label_2.setText(QCoreApplication.translate("Form", u".", None))
        self.label_3.setText(QCoreApplication.translate("Form", u".", None))
    # retranslateUi

