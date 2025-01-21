from PySide6 import QtGui, QtCore, QtWidgets
import _thread, traceback


class Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(
        self,
        parent: QtGui.QTextDocument = None,
    ):
        super().__init__(parent)
        self.finished1 = True
        self.finished2 = True

        self._ontype = None

    def highlightBlock(self, text: str):
        if self._ontype:
            self._ontype()
        try:
            for i in self._word_texts:
                self._word_text = i
                self._highlightBlock1(text)
            self._highlightBlock2(text)
        except Exception:
            print(traceback.format_exc(), file=__import__("sys").stderr)

    def _highlightBlock1(
        self,
        text: str,
    ) -> None:
        # print(len(text))
        if not self.finished1:
            return
        self.finished1 = False
        if not self._word_text:
            return
        myClassFormat = QtGui.QTextCharFormat()
        _ = QtGui.QFont()
        _.setBold(True)
        myClassFormat.setFont(_)
        pattern = self._word_text
        expression = pattern
        # print(expression)
        index: int = text.find(pattern)
        while index >= 0:
            # print(index, expression)
            QtWidgets.QApplication.processEvents()
            try:
                if (
                    index == 0
                    and (
                        text[index + len(self._word_text)] == " "
                        or len(text) == len(self._word_text)
                    )
                ) or (
                    text[index - 1] == " " and text[index + len(self._word_text)] == " "
                ):

                    self.setFormat(index, len(self._word_text), myClassFormat)
            except IndexError:
                # print(text[index - 1] == " ")
                if text[index - 1] == " " or index == 0:
                    self.setFormat(index, len(self._word_text), myClassFormat)
            index = text.find(pattern, index + len(self._word_text))
        self.finished1 = True

    def _highlightBlock2(self, text: str):
        if not self.finished2:
            return
        self.finished2 = False
        index: int = text.lower().find("rem")
        ____ = QtGui.QTextCharFormat()
        _____ = QtGui.QFont()
        _____.setItalic(True)
        ____.setFont(_____)
        while index >= 0:
            # print(index, expression)
            QtWidgets.QApplication.processEvents()
            try:
                if (index == 0 and (text[index + 3] == " " or len(text) == 3)) or (
                    text[index - 1] == " " and text[index + 3] == " "
                ):

                    self.setFormat(index, 3, ____)
            except IndexError:
                # print(text[index - 1] == " ")
                if text[index - 1] == " " or index == 0:
                    self.setFormat(index, 3, ____)
            index = text.lower().find("rem", index + 3)
        index = None
        for i in "0123456789":
            if text.find(i) >= 0:
                index = text.find(i)
        if index == None:
            self.finished2 = True
            return
        while index >= 0:
            __ = QtGui.QTextCharFormat()
            ___ = QtGui.QColor(0, 0, 255)
            __.setForeground(___)
            self.setFormat(index, 1, __)
            for i in "0123456789":
                if text.find(i, index + 1) >= 0:
                    index = text.find(i, index + 1)
                    break
                if i == "9":
                    index = -1
        self.finished2 = True

    def setText(self, *texts: str):
        self._word_texts = texts

    def setOnType(self, func: "function" = None):
        self._ontype = func


if __name__ == "__main__":
    print(Highlighter())
