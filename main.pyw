import sys

from PySide2.QtWidgets import QApplication

from controllers.c_master import CMaster

if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('fusion')

    CMaster()

    sys.exit(app.exec_())
