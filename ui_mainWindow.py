# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextEdit,
    QVBoxLayout, QWidget)

from add_file_dialog import AddFileDialog
from exe_behavior_widget import ExeBehaviorWidget
from versionInfoWidget import VersionInfoWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(826, 427)
        self.action_new = QAction(MainWindow)
        self.action_new.setObjectName(u"action_new")
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_saveas = QAction(MainWindow)
        self.action_saveas.setObjectName(u"action_saveas")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.action_undo = QAction(MainWindow)
        self.action_undo.setObjectName(u"action_undo")
        self.action_redo = QAction(MainWindow)
        self.action_redo.setObjectName(u"action_redo")
        self.action_copy = QAction(MainWindow)
        self.action_copy.setObjectName(u"action_copy")
        self.action_paste = QAction(MainWindow)
        self.action_paste.setObjectName(u"action_paste")
        self.action_del = QAction(MainWindow)
        self.action_del.setObjectName(u"action_del")
        self.action_selall = QAction(MainWindow)
        self.action_selall.setObjectName(u"action_selall")
        self.action_cut = QAction(MainWindow)
        self.action_cut.setObjectName(u"action_cut")
        self.action_Compile = QAction(MainWindow)
        self.action_Compile.setObjectName(u"action_Compile")
        self.action_Settings = QAction(MainWindow)
        self.action_Settings.setObjectName(u"action_Settings")
        self.action_H = QAction(MainWindow)
        self.action_H.setObjectName(u"action_H")
        self.action_About = QAction(MainWindow)
        self.action_About.setObjectName(u"action_About")
        self.action_AboutQt = QAction(MainWindow)
        self.action_AboutQt.setObjectName(u"action_AboutQt")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.pushButton_new = QPushButton(self.centralwidget)
        self.pushButton_new.setObjectName(u"pushButton_new")

        self.horizontalLayout.addWidget(self.pushButton_new)

        self.pushButton_open = QPushButton(self.centralwidget)
        self.pushButton_open.setObjectName(u"pushButton_open")

        self.horizontalLayout.addWidget(self.pushButton_open)

        self.pushButton_save = QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.pushButton_undo = QPushButton(self.centralwidget)
        self.pushButton_undo.setObjectName(u"pushButton_undo")

        self.horizontalLayout.addWidget(self.pushButton_undo)

        self.pushButton_redo = QPushButton(self.centralwidget)
        self.pushButton_redo.setObjectName(u"pushButton_redo")

        self.horizontalLayout.addWidget(self.pushButton_redo)

        self.pushButton_cut = QPushButton(self.centralwidget)
        self.pushButton_cut.setObjectName(u"pushButton_cut")

        self.horizontalLayout.addWidget(self.pushButton_cut)

        self.pushButton_copy = QPushButton(self.centralwidget)
        self.pushButton_copy.setObjectName(u"pushButton_copy")

        self.horizontalLayout.addWidget(self.pushButton_copy)

        self.pushButton_paste = QPushButton(self.centralwidget)
        self.pushButton_paste.setObjectName(u"pushButton_paste")

        self.horizontalLayout.addWidget(self.pushButton_paste)

        self.pushButton_compile = QPushButton(self.centralwidget)
        self.pushButton_compile.setObjectName(u"pushButton_compile")

        self.horizontalLayout.addWidget(self.pushButton_compile)

        self.pushButton_settings = QPushButton(self.centralwidget)
        self.pushButton_settings.setObjectName(u"pushButton_settings")

        self.horizontalLayout.addWidget(self.pushButton_settings)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout = QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_3 = QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_version_info = VersionInfoWidget(self.tab_2)
        self.widget_version_info.setObjectName(u"widget_version_info")

        self.verticalLayout_3.addWidget(self.widget_version_info)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_4 = QVBoxLayout(self.tab_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_add_file = AddFileDialog(self.tab_3)
        self.widget_add_file.setObjectName(u"widget_add_file")

        self.verticalLayout_4.addWidget(self.widget_add_file)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_5 = QVBoxLayout(self.tab_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_exe_behavior = ExeBehaviorWidget(self.tab_4)
        self.widget_exe_behavior.setObjectName(u"widget_exe_behavior")

        self.verticalLayout_5.addWidget(self.widget_exe_behavior)

        self.tabWidget.addTab(self.tab_4, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.verticalLayout_6.addLayout(self.verticalLayout_2)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setMaximumSize(QSize(16777215, 60))

        self.verticalLayout_6.addWidget(self.listWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 826, 33))
        self.menu_F = QMenu(self.menubar)
        self.menu_F.setObjectName(u"menu_F")
        self.menu_E = QMenu(self.menubar)
        self.menu_E.setObjectName(u"menu_E")
        self.menu_Y = QMenu(self.menubar)
        self.menu_Y.setObjectName(u"menu_Y")
        self.menu_H = QMenu(self.menubar)
        self.menu_H.setObjectName(u"menu_H")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu_F.menuAction())
        self.menubar.addAction(self.menu_E.menuAction())
        self.menubar.addAction(self.menu_Y.menuAction())
        self.menubar.addAction(self.menu_H.menuAction())
        self.menu_F.addAction(self.action_new)
        self.menu_F.addAction(self.action_open)
        self.menu_F.addAction(self.action_save)
        self.menu_F.addAction(self.action_saveas)
        self.menu_F.addSeparator()
        self.menu_F.addAction(self.action_exit)
        self.menu_E.addAction(self.action_undo)
        self.menu_E.addAction(self.action_redo)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.action_cut)
        self.menu_E.addAction(self.action_copy)
        self.menu_E.addAction(self.action_paste)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.action_del)
        self.menu_E.addSeparator()
        self.menu_E.addAction(self.action_selall)
        self.menu_Y.addAction(self.action_Compile)
        self.menu_Y.addAction(self.action_Settings)
        self.menu_H.addAction(self.action_About)
        self.menu_H.addAction(self.action_AboutQt)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SlowBFC", None))
        self.action_new.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa(&N)", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00(&O)", None))
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58(&S)", None))
        self.action_saveas.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a(&A)", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa(&E)", None))
        self.action_undo.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500(&T)    Ctrl+Z", None))
        self.action_redo.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u505a(&U)    Ctrl+Y", None))
        self.action_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236(&W)    Ctrl+C", None))
        self.action_paste.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34(&X)    Ctrl+V", None))
        self.action_del.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664(&Y)    Del", None))
        self.action_selall.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009(&Z)    Ctrl+A", None))
        self.action_cut.setText(QCoreApplication.translate("MainWindow", u"\u526a\u5207(&V)    Ctrl+X", None))
        self.action_Compile.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8bd1(&C)", None))
        self.action_Settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e(&S)", None))
        self.action_H.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
        self.action_About.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e(&A)", None))
        self.action_AboutQt.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8eQt", None))
        self.pushButton_new.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.pushButton_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.pushButton_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.pushButton_undo.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500", None))
        self.pushButton_redo.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u505a", None))
        self.pushButton_cut.setText(QCoreApplication.translate("MainWindow", u"\u526a\u5207", None))
        self.pushButton_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.pushButton_paste.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34", None))
        self.pushButton_compile.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.pushButton_settings.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u7248\u672c\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u9644\u52a0\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"EXE\u884c\u4e3a", None))
        self.menu_F.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(&F)", None))
        self.menu_E.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91(&E)", None))
        self.menu_Y.setTitle(QCoreApplication.translate("MainWindow", u"\u5de5\u7a0b(&Y)", None))
        self.menu_H.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e(&A)", None))
    # retranslateUi

