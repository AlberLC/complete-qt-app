from datetime import date

from PySide2 import QtCore, QtGui, QtWidgets

from models import Cells
from utilities.various import get_minimum_date


class TextItemWidget(QtWidgets.QTableWidgetItem):
    def __init__(self, obj, item_id, red=False):
        if isinstance(obj, list):
            text = ' - '.join(map(str, obj))
        elif isinstance(obj, date):
            text = obj.strftime('%d/%m/%Y')
        elif type(obj) in (int, float):
            text = str(obj).replace('.', ',')
        else:
            text = str(obj).replace('\n', ' ')
        text = '-' if not text or text == 'None' else text
        super().__init__(text)
        self.item_id = item_id

        self.setTextAlignment(QtCore.Qt.AlignCenter)
        if red:
            self.setBackgroundColor(QtGui.QColor(255, 200, 200))


class NumericItemWidget(TextItemWidget):
    def __init__(self, obj, item_id, red=False):
        if isinstance(obj, Cells):
            obj = getattr(obj, 'number', None)
        super().__init__(obj, item_id, red)
        self.number = obj if obj else 0

    def __lt__(self, other):
        return self.number < other.number


class DateItemWidget(TextItemWidget):
    def __init__(self, date, item_id, red=False):
        super().__init__(date, item_id, red)
        self.date = date if date else get_minimum_date()

    def __lt__(self, other):
        return self.date < other.date
