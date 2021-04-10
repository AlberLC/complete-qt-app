from enum import Enum

from PySide2 import QtCore, QtGui, QtWidgets


class Color(Enum):
    DEFAULT = 0
    RED = 1


# noinspection PyPep8Naming,PyUnresolvedReferences
class __NoWheelSpinBox:
    def __init__(self, *args):
        self.color = Color.DEFAULT
        super().__init__(*args)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setCorrectionMode(QtWidgets.QSpinBox.CorrectToNearestValue)

    def color_default(self):
        if self.color != Color.DEFAULT:
            self.color = Color.DEFAULT
            self.lineEdit().setStyleSheet(None)

    def color_red(self):
        if self.color != Color.RED:
            self.color = Color.RED
            self.lineEdit().setStyleSheet('background-color: rgb(255, 200, 200)')

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Backspace:
            suffix = self.suffix()
            if suffix:
                edit = self.lineEdit()
                text = edit.text()
                if text.endswith(suffix) and text != self.specialValueText():
                    pos = edit.cursorPosition()
                    end = len(text) - len(suffix)
                    if pos > end:
                        edit.setCursorPosition(end)
        super().keyPressEvent(event)

    def setValue(self, value):
        if value is None:
            value = 0
        super().setValue(value)

    def validate_hard(self):
        if not self.value():
            self.color_red()
        else:
            self.color_default()

    def wheelEvent(self, event):
        if self.hasFocus():
            return super().wheelEvent(event)
        else:
            event.ignore()


class NoWheelSpinBox(__NoWheelSpinBox, QtWidgets.QSpinBox):
    pass


class NoWheelDoubleSpinBox(__NoWheelSpinBox, QtWidgets.QDoubleSpinBox):
    def __init__(self, *args):
        super().__init__(*args)
        # self.setLocale(QtCore.QLocale(QtCore.QLocale.English))

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Period, QtCore.Qt.Key_Comma):
            cursor_position = self.lineEdit().cursorPosition()
            text_before_period = self.lineEdit().text()[:cursor_position].replace(',', '').replace('.','')
            self.lineEdit().setText(f'{text_before_period},')
            # event = QtGui.QKeyEvent(QtCore.QEvent.KeyPress, QtCore.Qt.Key_Comma, QtCore.Qt.NoModifier, ',')
        super().keyPressEvent(event)
