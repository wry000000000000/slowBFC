from ui_exe_bahavior import Ui_Form
from PySide6.QtWidgets import QApplication, QWidget


class ExeBehaviorWidget(Ui_Form, QWidget):
    def __init__(self, parent=...):
        parent = None if parent == ... else parent
        super().__init__(parent)
        self.setupUi(self)


if __name__ == "__main__":
    qa = QApplication(list())
    eb = ExeBehaviorWidget()
    eb.show()
    qa.exec()
