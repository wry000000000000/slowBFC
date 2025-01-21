from ui_about_dialog import Ui_Dialog
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox
from PySide6.QtCore import QTranslator
import constants, webbrowser


class AboutDialog(Ui_Dialog, QDialog):
    def __init__(self, parent=...):
        parent = None if parent == ... else parent
        super().__init__(parent)
        self.setupUi(self)

        self.setWindowTitle("关于SlowBFC")
        self.setUpSignal()

    def setUpSignal(self):
        self.pushButton_about_Qt.clicked.connect(lambda: QMessageBox.aboutQt(self))
        self.pushButton_mit_license.clicked.connect(
            lambda: QMessageBox.information(
                self, "MIT许可证", constants.MIT_LICENSE_TEXT
            )
        )

        self.pushButton_sbili.clicked.connect(
            lambda: webbrowser.open(constants.B_WEBSITE)
        )
        self.label_GH.mouseReleaseEvent = lambda *what: webbrowser.open(
            constants.G_WEBSITE
        )


if __name__ == "__main__":
    qt = QTranslator()
    qt.load("qt_zh_CN.qm", "./translate/")
    qa = QApplication()
    qa.installTranslator(qt)
    ad = AboutDialog()
    ad.show()
    qa.exec()
