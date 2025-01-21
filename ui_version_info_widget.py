# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'version_info_widgetZjNEmU.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

from advanced_wids import VersionEdit

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(536, 289)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkBox_enable = QCheckBox(Form)
        self.checkBox_enable.setObjectName(u"checkBox_enable")

        self.verticalLayout.addWidget(self.checkBox_enable)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.label_company_name = QLabel(self.groupBox)
        self.label_company_name.setObjectName(u"label_company_name")

        self.verticalLayout_4.addWidget(self.label_company_name)

        self.label_product_introduct = QLabel(self.groupBox)
        self.label_product_introduct.setObjectName(u"label_product_introduct")

        self.verticalLayout_4.addWidget(self.label_product_introduct)

        self.label_file_introduct = QLabel(self.groupBox)
        self.label_file_introduct.setObjectName(u"label_file_introduct")

        self.verticalLayout_4.addWidget(self.label_file_introduct)

        self.label_law_copyright = QLabel(self.groupBox)
        self.label_law_copyright.setObjectName(u"label_law_copyright")

        self.verticalLayout_4.addWidget(self.label_law_copyright)

        self.label_law_trademark = QLabel(self.groupBox)
        self.label_law_trademark.setObjectName(u"label_law_trademark")

        self.verticalLayout_4.addWidget(self.label_law_trademark)

        self.label_orig_filename = QLabel(self.groupBox)
        self.label_orig_filename.setObjectName(u"label_orig_filename")

        self.verticalLayout_4.addWidget(self.label_orig_filename)

        self.label_comment = QLabel(self.groupBox)
        self.label_comment.setObjectName(u"label_comment")

        self.verticalLayout_4.addWidget(self.label_comment)

        self.label_product_version = QLabel(self.groupBox)
        self.label_product_version.setObjectName(u"label_product_version")

        self.verticalLayout_4.addWidget(self.label_product_version)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.lineEdit_company_name = QLineEdit(self.groupBox)
        self.lineEdit_company_name.setObjectName(u"lineEdit_company_name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_company_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_company_name.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.lineEdit_company_name)

        self.lineEdit_product_name = QLineEdit(self.groupBox)
        self.lineEdit_product_name.setObjectName(u"lineEdit_product_name")
        sizePolicy.setHeightForWidth(self.lineEdit_product_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_product_name.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.lineEdit_product_name)

        self.lineEdit_file_desc = QLineEdit(self.groupBox)
        self.lineEdit_file_desc.setObjectName(u"lineEdit_file_desc")
        sizePolicy.setHeightForWidth(self.lineEdit_file_desc.sizePolicy().hasHeightForWidth())
        self.lineEdit_file_desc.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.lineEdit_file_desc)

        self.lineEdit_legal_copyr = QLineEdit(self.groupBox)
        self.lineEdit_legal_copyr.setObjectName(u"lineEdit_legal_copyr")
        sizePolicy.setHeightForWidth(self.lineEdit_legal_copyr.sizePolicy().hasHeightForWidth())
        self.lineEdit_legal_copyr.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.lineEdit_legal_copyr)

        self.lineEdit_legal_trademark = QLineEdit(self.groupBox)
        self.lineEdit_legal_trademark.setObjectName(u"lineEdit_legal_trademark")
        sizePolicy.setHeightForWidth(self.lineEdit_legal_trademark.sizePolicy().hasHeightForWidth())
        self.lineEdit_legal_trademark.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.lineEdit_legal_trademark)

        self.lineEdit_orig_filename = QLineEdit(self.groupBox)
        self.lineEdit_orig_filename.setObjectName(u"lineEdit_orig_filename")
        sizePolicy.setHeightForWidth(self.lineEdit_orig_filename.sizePolicy().hasHeightForWidth())
        self.lineEdit_orig_filename.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.lineEdit_orig_filename)

        self.lineEdit_comment = QLineEdit(self.groupBox)
        self.lineEdit_comment.setObjectName(u"lineEdit_comment")
        sizePolicy.setHeightForWidth(self.lineEdit_comment.sizePolicy().hasHeightForWidth())
        self.lineEdit_comment.setSizePolicy(sizePolicy)

        self.verticalLayout_5.addWidget(self.lineEdit_comment)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.lineEdit_product_version = VersionEdit(self.groupBox)
        self.lineEdit_product_version.setObjectName(u"lineEdit_product_version")

        self.horizontalLayout_2.addWidget(self.lineEdit_product_version)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit_fileversion = VersionEdit(self.groupBox)
        self.lineEdit_fileversion.setObjectName(u"lineEdit_fileversion")

        self.horizontalLayout_2.addWidget(self.lineEdit_fileversion)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_inside_name = QLineEdit(self.groupBox)
        self.lineEdit_inside_name.setObjectName(u"lineEdit_inside_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_inside_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_inside_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lineEdit_inside_name)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addLayout(self.verticalLayout_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout)


        self.verticalLayout.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.checkBox_enable.setText(QCoreApplication.translate("Form", u"\u53ef\u6267\u884c\u6587\u4ef6\u4e2d\u5199\u5165\u7248\u672c\u4fe1\u606f", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u7248\u672c\u4fe1\u606f", None))
        self.label_company_name.setText(QCoreApplication.translate("Form", u"\u516c\u53f8\u540d\u79f0\uff1a", None))
        self.label_product_introduct.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u540d\u79f0\uff1a", None))
        self.label_file_introduct.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u63cf\u8ff0\uff1a", None))
        self.label_law_copyright.setText(QCoreApplication.translate("Form", u"\u6cd5\u5f8b\u7248\u6743\uff1a", None))
        self.label_law_trademark.setText(QCoreApplication.translate("Form", u"\u6cd5\u5f8b\u5546\u6807\uff1a", None))
        self.label_orig_filename.setText(QCoreApplication.translate("Form", u"\u539f\u59cb\u6587\u4ef6\u540d\uff1a", None))
        self.label_comment.setText(QCoreApplication.translate("Form", u"\u6ce8\u91ca\uff1a", None))
        self.label_product_version.setText(QCoreApplication.translate("Form", u"\u4ea7\u54c1\u7248\u672c\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6587\u4ef6\u7248\u672c\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5185\u90e8\u540d\u79f0\uff1a", None))
    # retranslateUi

