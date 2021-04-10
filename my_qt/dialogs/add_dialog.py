from PySide2 import QtCore, QtGui, QtWidgets

from my_qt.combo_boxes import SearchCombo
from my_qt.dialogs.message_boxes import name_empty_or_existent, question_add_new_item
from resources import MyStrings, url_icon


class AddDialog(QtWidgets.QDialog):
    CANCEL = 0
    ADD_EXISTENT = 1
    ADD_NEW = 2

    def __init__(self, items, current_items):
        super().__init__()
        self.my_strings = MyStrings()
        self.items = items
        self.current_items = current_items

        self.setWindowTitle(self.my_strings.title_add_certificate)
        self.icono = QtGui.QIcon(url_icon)
        self.setWindowIcon(self.icono)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.resize(300, 45)
        self.setMaximumHeight(45)

        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName('horizontalLayout')
        self.comboBox = SearchCombo(self, self.items)
        self.comboBox.setMinimumSize(QtCore.QSize(150, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName('comboBox')
        self.horizontalLayout.addWidget(self.comboBox)
        self.buttonAccept = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.buttonAccept.setFont(font)
        self.buttonAccept.setObjectName('buttonAccept')
        self.horizontalLayout.addWidget(self.buttonAccept)
        self.horizontalLayout.setStretch(0, 1)

        self.buttonAccept.setText(self.my_strings.button_accept)
        self.buttonAccept.clicked.connect(lambda: self.done())
        self.comboBox.option_clicked.connect(lambda: self.done())

    @property
    def text(self):
        return self.comboBox.currentText()

    def done(self, code=None):
        if code is not None:
            return super().done(code)
        if not name_empty_or_existent(self.text, self.current_items):
            if self.text not in self.items:
                if question_add_new_item() == QtWidgets.QMessageBox.AcceptRole:
                    return super().done(self.ADD_NEW)
            else:
                return super().done(self.ADD_EXISTENT)
        self.comboBox.setFocus()
        self.comboBox.lineEdit().setCursorPosition(len(self.comboBox.lineEdit().text()))
