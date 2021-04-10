from PySide2 import QtWidgets, QtGui, QtCore

from exceptions.abort_exception import AbortException
from resources import MyStrings, url_icon


class Window(QtWidgets.QMainWindow):
    signal_search = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.icon = QtGui.QIcon(url_icon)
        self.c_master = None
        self.language = MyStrings()
        self.setWindowTitle(self.language.title_sn)
        self.setWindowIcon(self.icon)
        self.show()

    def sizeHint(self):
        return QtCore.QSize(910, 625)

    def add_controller(self, controller):
        self.c_master = controller

    def closeEvent(self, event):
        if hasattr(self.c_master.controller, 'exit'):
            try:
                self.c_master.controller.exit()
            except AbortException:
                event.ignore()

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == QtCore.Qt.Key_Backspace:
            try:
                self.buttonBack.click()
            except:
                pass
