# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settingsWindowssHbQS.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QDialog,
    QDialogButtonBox, QFormLayout, QGroupBox, QLabel,
    QLayout, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModality.WindowModal)
        Dialog.resize(409, 531)
        self.formLayout = QFormLayout(Dialog)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout_2 = QFormLayout(self.groupBox)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioButton_cmdline = QRadioButton(self.groupBox)
        self.radioButton_cmdline.setObjectName(u"radioButton_cmdline")

        self.verticalLayout_2.addWidget(self.radioButton_cmdline)

        self.radioButton_ghost = QRadioButton(self.groupBox)
        self.radioButton_ghost.setObjectName(u"radioButton_ghost")

        self.verticalLayout_2.addWidget(self.radioButton_ghost)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.verticalLayout_2)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_3 = QFormLayout(self.groupBox_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.checkBox_samename = QCheckBox(self.groupBox_2)
        self.checkBox_samename.setObjectName(u"checkBox_samename")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.checkBox_samename)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Dialog)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_4 = QFormLayout(self.groupBox_3)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.lineEdit_font = QLineEdit(self.groupBox_3)
        self.lineEdit_font.setObjectName(u"lineEdit_font")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.lineEdit_font)

        self.pushButton_font = QPushButton(self.groupBox_3)
        self.pushButton_font.setObjectName(u"pushButton_font")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.pushButton_font)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(Dialog)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.formLayout_5 = QFormLayout(self.groupBox_4)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.checkBox_pause = QCheckBox(self.groupBox_4)
        self.checkBox_pause.setObjectName(u"checkBox_pause")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.checkBox_pause)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.label)

        self.checkBox_closetarbar = QCheckBox(self.groupBox_4)
        self.checkBox_closetarbar.setObjectName(u"checkBox_closetarbar")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.checkBox_closetarbar)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.checkBox_admin = QCheckBox(self.groupBox_4)
        self.checkBox_admin.setObjectName(u"checkBox_admin")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.checkBox_admin)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_5.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_5.setWidget(6, QFormLayout.LabelRole, self.label_4)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(Dialog)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.formLayout_6 = QFormLayout(self.groupBox_5)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.lineEdit_path = QLineEdit(self.groupBox_5)
        self.lineEdit_path.setObjectName(u"lineEdit_path")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.lineEdit_path)

        self.pushButton_browse = QPushButton(self.groupBox_5)
        self.pushButton_browse.setObjectName(u"pushButton_browse")

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.pushButton_browse)


        self.verticalLayout.addWidget(self.groupBox_5)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u8f93\u51faEXE\u7c7b\u578b", None))
#if QT_CONFIG(whatsthis)
        self.radioButton_cmdline.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u8fd9\u79cd\u5e94\u7528\u7a0b\u5e8f\u7c7b\u578b\u5c06\u4f1a\u521b\u5efa\u6807\u51c6\u7684\u7a97\u53e3\u63a7\u5236\u53f0\u7a0b\u5e8f</p><p>\u5b8c\u5168\u6a21\u62df\u6807\u51c6BAT\u6587\u4ef6\u7684\u6267\u884c\uff0c\u53ef\u63a5\u6536\u7528\u6237\u8f93\u5165\u3002</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.radioButton_cmdline.setText(QCoreApplication.translate("Dialog", u"\u63a7\u5236\u53f0\u7a0b\u5e8f", None))
#if QT_CONFIG(whatsthis)
        self.radioButton_ghost.setWhatsThis(QCoreApplication.translate("Dialog", u"<html><head/><body><p>\u8fd9\u79cd\u5e94\u7528\u7a0b\u5e8f\u7c7b\u578b\u5c06\u4e0d\u4f1a\u521b\u5efa\u547d\u4ee4\u884c\u7a97\u53e3\u3002</p><p>\u5bf9\u4e8e\u9759\u9ed8\u5b89\u88c5\u975e\u5e38\u6709\u7528\uff01</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.radioButton_ghost.setText(QCoreApplication.translate("Dialog", u"\u5e7d\u7075\u7a0b\u5e8f", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u8f93\u51fa\u6587\u4ef6\u540d\u79f0", None))
        self.checkBox_samename.setText(QCoreApplication.translate("Dialog", u"\u548c\u539f\u59cb\u6587\u4ef6\u4f7f\u7528\u76f8\u540c\u7684\u540d\u79f0\u548c\u4f4d\u7f6e", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u7f16\u8f91\u5668\u5b57\u4f53", None))
        self.pushButton_font.setText(QCoreApplication.translate("Dialog", u"\u5b57\u4f53...", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u9ed8\u8ba4\u8f93\u51faEXE\u884c\u4e3a", None))
        self.checkBox_pause.setText(QCoreApplication.translate("Dialog", u"\u8f93\u51fa\u7a0b\u5e8f\u8fd0\u884c\u540e\u6682\u505c\u7ec8\u7aef", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"      \u4ec5\u63a7\u5236\u53f0\u7a0b\u5e8f\u53ef\u7528", None))
        self.checkBox_closetarbar.setText(QCoreApplication.translate("Dialog", u"\u5728\u4efb\u52a1\u680f\u6258\u76d8\u663e\u793a\u5173\u95ed\u952e", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"      \u5e7d\u7075\u7a0b\u5e8f\u5efa\u8bae\u4f7f\u7528", None))
        self.checkBox_admin.setText(QCoreApplication.translate("Dialog", u"\u81ea\u52a8\u8bf7\u6c42\u7ba1\u7406\u5458\u6743\u9650", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"      \u5b9e\u9a8c\u6027\u529f\u80fd\uff0c\u5c06\u4ea7\u751f\u65b0\u7684\u7ec8\u7aef\u7a97\u53e3\uff0c\u56e0\u6b64", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"    \u5efa\u8bae\u548c\u6682\u505c\u7ec8\u7aef\u540c\u65f6\u4f7f\u7528\uff0c\u4e14\u4e0d\u80fd\u7528\u4e8e\u7ba1\u9053\u8bfb\u5199", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"\u9ed8\u8ba4\u8f93\u51faEXE\u56fe\u6807", None))
        self.pushButton_browse.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8...", None))
    # retranslateUi

