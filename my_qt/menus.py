from PySide2 import QtCore, QtWidgets

from utilities.various import sort_items


class CheckableMenu(QtWidgets.QMenu):
    def __init__(self, parent, font=None):
        super().__init__(parent)
        self.installEventFilter(self)
        if font:
            self.setFont(font)

    @property
    def checked_items(self):
        return [action.text() for action in self.actions() if action.isChecked()]

    @checked_items.setter
    def checked_items(self, items):
        for item in items:
            if item:
                for action in self.actions():
                    if str(item) == action.text():
                        action.setChecked(True)
                        break

    @property
    def items(self):
        return [action.text() for action in self.actions()]

    @items.setter
    def items(self, items):
        items = sort_items(items)
        for item in items:
            self.add_item(item)

    def add_item(self, item):
        if item:
            action = QtWidgets.QAction(str(item), self)
            action.setCheckable(True)
            super().addAction(action)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.MouseButtonRelease:
            if isinstance(obj, QtWidgets.QMenu) and obj.activeAction() and not obj.activeAction().menu():
                obj.activeAction().trigger()
                return True
        return super().eventFilter(obj, event)

    def keyPressEvent(self, event):
        if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            action = self.activeAction()
            if not action:
                return False
            if action.isChecked():
                check = False
            else:
                check = True
            self.activeAction().setChecked(check)
            return True
        elif event.key() == QtCore.Qt.Key_Backspace:
            self.close()
        return super().keyPressEvent(event)
