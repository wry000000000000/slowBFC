from ui_add_file_dialog import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QSize
import os


class AddFileDialog(QWidget, Ui_Form):
    def __init__(self, parent=...):
        parent = None if parent == ... else parent
        super().__init__(parent)

        self.setupUi(self)
        self.setUpSignal()

        self.label_preview.setText("\t")

    def setUpSignal(self):
        self.pushButton_browse.clicked.connect(self.browse)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_del.clicked.connect(self.del_)

        self.lineEdit.textChanged.connect(
            (lambda: self.updatePixMap(self.lineEdit.text()))
        )

    def del_(self):
        self.listWidget.takeItem(self.listWidget.currentIndex().row())

    def add(self):
        _ = QFileDialog.getOpenFileNames(
            self, "浏览文件", os.path.expanduser("~"), "所有文件(*.*)"
        )
        if not _[0]:
            return 0
        else:
            for i in _[0]:
                self.listWidget.addItem(i.replace("/", "\\"))

    def browse(self):
        _ = QFileDialog.getOpenFileName(
            self, "浏览文件", os.path.expanduser("~"), "图标文件(*.ico)"
        )
        if not _[0]:
            return 0
        else:
            self.lineEdit.setText(_[0])

    def updatePixMap(self, path: str):
        path = path.strip(" ")
        if not os.path.exists(path):
            if not path:
                self.label_preview.setText("\t")
                return 0
            self.label_preview.setText("图标文件\n不存在")
            self.label_preview.setStyleSheet("color:gray")
            return 0
        self.label_preview.setStyleSheet("color:black")
        _pixmap = QPixmap(path)
        _pixmap = _pixmap.scaled(
            QSize(self.label_preview.width(), self.label_preview.height())
        )
        self.label_preview.setPixmap(_pixmap)


if __name__ == "__main__":
    qa = QApplication(list())
    afd = AddFileDialog()
    afd.show()
    qa.exec()
