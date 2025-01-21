from PySide6 import QtGui


class _Highlighter(QtGui.QSyntaxHighlighter):
    def __init__(self, parent: QtGui.QTextDocument = None):
        super().__init__(parent)

    def highlightBlock(text: str):
        pass

    _word_text: str
