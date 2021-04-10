from enum import Enum

from PySide2 import QtCore, QtGui, QtWidgets

from utilities.searchs import filtered_items
from utilities.various import sort_items


# class Worker(QtCore.QRunnable):
#     def __init__(self, items, text, s):
#         super().__init__()
#         self.items = items
#         self.text = text
#         self.s = s
#
#     def run(self):
#         names = filtered_items(self.items, self.text)
#         # self.s.completer.model().setStringList(names)

class Color(Enum):
    DEFAULT = 0
    BLUE = 1
    RED = 2


class SearchCombo(QtWidgets.QComboBox):
    option_clicked = QtCore.Signal()

    def __init__(self, parent, items=[]):
        super().__init__(parent)
        self.setEditable(True)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self._items = []
        font = QtGui.QFont()
        font.setPointSize(11)
        self.completer = QtWidgets.QCompleter([])
        self.completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.completer.setCompletionMode(QtWidgets.QCompleter.UnfilteredPopupCompletion)
        self.completer.popup().setFont(font)
        self.setCompleter(self.completer)

        self.items = items
        self.color = Color.DEFAULT
        self.__is_item_highlighted = False

        self.lineEdit().textEdited.connect(self.__set_completer_items)
        self.currentIndexChanged.connect(self.__set_cursor_start)
        self.activated.connect(self.__filter_activation)
        self.highlighted.connect(self.__set_item_highlighted)

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, items):
        text = self.lineEdit().text()
        self.clear()
        self._items = sort_items(items)
        self.addItems(self.items)
        self.lineEdit().setText(text)

    def color_blue(self):
        if self.color != Color.BLUE:
            self.color = Color.BLUE
            self.lineEdit().setStyleSheet('background-color: rgb(210, 240, 255)')
            self.setStyleSheet('font-size: 12pt')

    def color_default(self):
        if self.color != Color.DEFAULT:
            self.color = Color.DEFAULT
            self.lineEdit().setStyleSheet(None)

    def color_red(self):
        if self.color != Color.RED:
            self.color = Color.RED
            self.lineEdit().setStyleSheet('background-color: rgb(255, 200, 200)')
            self.setStyleSheet('font-size: 12pt')

    def focusOutEvent(self, event):
        super().focusOutEvent(event)
        self.__set_cursor_start()

    def setCurrentText(self, item):
        super().setCurrentText(str(item) if item else '')
        self.__set_cursor_start()

    def validate_hard(self, ignore_empty=False):
        if (self.currentText() or not ignore_empty) and self.currentText() not in self.items:
            self.color_red()
        else:
            self.color_default()

    def validate_soft(self):
        if self.currentText() and self.currentText() not in self.items:
            self.color_blue()
        else:
            self.color_default()

    def wheelEvent(self, event):
        if self.hasFocus():
            return super().wheelEvent(event)
        else:
            event.ignore()

    def __complete_place_completer(self, items):
        current_made_in = self.window().comboMadeIn.currentText()
        current_origin = self.window().comboOrigin.currentText()
        current_destination = self.window().comboDestination.currentText()
        if self.objectName() == 'comboMadeIn':
            if current_origin:
                items.append(current_origin)
            if current_destination:
                items.append(current_destination)
        elif self.objectName() == 'comboOrigin':
            if current_made_in:
                items.append(current_made_in)
            if current_destination:
                items.append(current_destination)
        else:
            if current_made_in:
                items.append(current_made_in)
            if current_origin:
                items.append(current_origin)
        return items

    def __filter_activation(self):
        if self.__is_item_highlighted:
            self.option_clicked.emit()
            self.__is_item_highlighted = False

    def __set_completer_items(self):
        items = self.items.copy()
        if self.objectName() in ('comboMadeIn', 'comboOrigin', 'comboDestination'):
            items = self.__complete_place_completer(items)
        items = filtered_items(items, self.currentText())
        self.completer.model().setStringList(items)

    def __set_cursor_start(self):
        self.lineEdit().setCursorPosition(0)

    def __set_item_highlighted(self):
        self.__is_item_highlighted = True
