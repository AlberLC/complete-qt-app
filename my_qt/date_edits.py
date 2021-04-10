from PySide2 import QtCore, QtGui, QtWidgets

from resources import url_cross
from utilities.various import get_minimum_date

class NoWheelDateEdit(QtWidgets.QDateEdit):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.setSpecialValueText('-')
        self.setDate(get_minimum_date())

        self.boton = QtWidgets.QPushButton()
        self.boton.setFlat(True)
        self.boton.setFixedSize(QtCore.QSize(20, 20))
        self.boton.setIconSize(QtCore.QSize(14, 14))
        self.boton.setIcon(QtGui.QIcon(url_cross))
        self.boton.clicked.connect(lambda: self.setDate(self.minimumDate()))

        layout = QtWidgets.QHBoxLayout(self)
        layout.addWidget(self.boton, 0, QtCore.Qt.AlignRight)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 23, 0)

    def wheelEvent(self, event):
        if self.hasFocus():
            return super().wheelEvent(event)
        else:
            event.ignore()
