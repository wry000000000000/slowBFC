from PySide6.QtWidgets import QWidget, QApplication, QLineEdit
from ui_version_edit import Ui_Form
from PySide6.QtGui import QKeyEvent
from pykeyboard import PyKeyboard
from win32con import VK_TAB, VK_SHIFT

from logger import ConsoleLogger
from logger.constants import INFO, DEBUG


class _Fake_Function(object):
    def __init__(
        self,
        parent: object,
        code: str,
        accept: bool = True,
        logger: ConsoleLogger = ConsoleLogger("version_wid_event_control"),
    ):
        self.logger = logger

        self.code = code
        self.self = parent
        self.accept = accept

    def __call__(self, event):
        if self.accept:
            event.accept()
        else:
            event.ignore()
        QApplication.processEvents()
        code = self.code
        self.logger.log(DEBUG, code)
        self = self.self
        exec(code)


class VersionEdit(QWidget, Ui_Form):
    def __init__(
        self,
        parent=...,
        f=...,
        logger: ConsoleLogger = ConsoleLogger("version_edit_wid"),
    ):
        self.logger = logger
        parent = None if parent == ... else parent
        super().__init__(parent)
        self.setupUi(self)

        self.setText("_0._0._0._0")
        self.setUpSignal()

        self.kbd = PyKeyboard()

    def text(self):
        _t = (
            self.lineEdit_1_1.text()
            + self.lineEdit_1_2.text()
            + "."
            + self.lineEdit_2_1.text()
            + self.lineEdit_2_2.text()
            + "."
            + self.lineEdit_3_1.text()
            + self.lineEdit_3_2.text()
            + "."
            + self.lineEdit_4_1.text()
            + self.lineEdit_4_2.text()
        )
        return _t

    def setText(self, t0: str):
        l0 = t0.split(".")
        self.logger.log(INFO, f"设置的文本：{l0}")
        for i in range(4):
            l0[i] = l0[i].strip()
            if l0[i].__len__() <= 2:
                l0[i] = l0[i] + "_"
            for j in range(2):
                exec(f"self.lineEdit_{i+1}_{j+1}.setText(l0[{i}][{j}])")

    def setUpSignal(self):
        for i in range(4):
            for j in range(2):
                ___ = _Fake_Function(self, f"self.clicked_({i+1},{j+1})")
                ____ = _Fake_Function(self, f"self.unclicked({i+1},{j+1})")
                _ = _Fake_Function(
                    self, f"self.key_pressed({i+1},{j+1},event)", accept=False
                )
                exec(f"self.lineEdit_{i+1}_{j+1}.setReadOnly(True)")
                exec(f"self.lineEdit_{i+1}_{j+1}.focusInEvent=___")
                exec(f"self.lineEdit_{i+1}_{j+1}.focusOutEvent=____")
                exec(f"self.lineEdit_{i+1}_{j+1}.keyPressEvent=_")

    def key_pressed(self, i: int, j: int, event: QKeyEvent):
        self.logger.log(INFO, f"事件触发：{i} {j} {event.key()}")
        if event.key() in tuple(range(49, 58)):
            wid: QLineEdit = eval(f"self.lineEdit_{i}_{j}")
            wid.setText(str(event.key() - 48))
            self.next(i, j)
        elif event.key() == 16777219:
            wid: QLineEdit = eval(f"self.lineEdit_{i}_{j}")
            wid.setText("_")
            self.back(i, j)
        elif event.key() == 48:
            wid: QLineEdit = eval(f"self.lineEdit_{i}_{j}")
            wid.setText("0")
            self.next(i, j)

    def next(self, i: int, j: int):
        if j + 1 > 2:
            if i + 1 > 4:
                PyKeyboard.tap_key(self.kbd, VK_TAB)
                return 0
            i += 1
            j = 0
        j += 1
        self.logger.log(INFO, f"文本框前进：{i} {j}")
        wid: QLineEdit = eval(f"self.lineEdit_{i}_{j}")
        wid.setFocus()

    def back(self, i: int, j: int):
        if j - 1 < 1:
            if i - 1 < 1:
                PyKeyboard.press_key(self.kbd, VK_SHIFT)
                PyKeyboard.tap_key(self.kbd, VK_TAB)
                PyKeyboard.release_key(self.kbd, VK_SHIFT)
                return 0
            i -= 1
            j = 3
        j -= 1
        self.logger.log(INFO, f"文本框返回：{i} {j}")
        wid: QLineEdit = eval(f"self.lineEdit_{i}_{j}")
        wid.setFocus()

    def unclicked(self, i: int, j: int):
        __: QLineEdit = eval(f"self.lineEdit_{i}_{j}")
        __.setStyleSheet("background-color:none;border:none;color:black")

    def clicked_(self, i: int, j: int):
        __: QLineEdit = eval(f"self.lineEdit_{i}_{j}")
        __.setStyleSheet("background-color:#0078D4;color:white;border:none")


if __name__ == "__main__":
    ap = QApplication(list())
    ve = VersionEdit()
    ve.show()
    ap.exec()
