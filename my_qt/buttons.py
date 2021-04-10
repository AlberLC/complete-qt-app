from PySide2 import QtGui, QtWidgets

from my_qt.menus import CheckableMenu
from utilities.various import clip_string_list


class CheckableMenuButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super().__init__(parent)
        # self.setStyleSheet('text-align: left; font-size: 11pt')
        font = QtGui.QFont()
        font.setPointSize(11)
        self._menu = CheckableMenu(self, font)

        self.setFont(font)
        self.setMenu(self._menu)

        self.menu().aboutToHide.connect(self.__checked_items)

    @property
    def checked_items(self):
        return self.menu().checked_items

    @checked_items.setter
    def checked_items(self, items):
        self.menu().checked_items = items
        self.__checked_items()

    @property
    def items(self):
        return self.menu().items

    @items.setter
    def items(self, items):
        self.menu().items = items

    def add_item(self, item):
        if item:
            self.menu().add_item(str(item))

    def mousePressEvent(self, event):
        if self.items:
            super().mousePressEvent(event)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.menu().setMinimumSize(self.width(), 0)

    def setText(self, text):
        if not text:
            text = '-'
        super().setText(text)

    def __checked_items(self):
        self.setText(clip_string_list(self.checked_items))
