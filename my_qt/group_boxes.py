from PySide2 import QtCore, QtGui, QtWidgets

from my_qt.table_widgets import BatteryNeedTable, BOSNeedTable, InverterNeedTable, PanelNeedTable, \
    StructureNeedTable, BatteryQuotationTable, BOSQuotationTable, InverterQuotationTable, PanelQuotationTable, \
    StructureQuotationTable, RelatedPanelQuotationTable, StaffTable
from resources import url_plus


# noinspection PyPep8Naming
class BaseGroup(QtWidgets.QGroupBox):
    def __init__(self, parent, my_strings, title, TableClass):
        super().__init__(parent)
        self.my_strings = my_strings
        self.title = title
        self.table = TableClass(self, self.my_strings)
        self.label = QtWidgets.QLabel(self)

        self.setup_gui()

    def setup_gui(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(False)
        font.setBold(True)
        self.setFont(font)
        self.setObjectName('group')
        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(6, 6, 6, 6)
        self.vertical_layout.setObjectName('vertical_layout')
        self.vertical_layout.addWidget(self.table)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName('label')
        self.vertical_layout.addWidget(self.label)

        self.setTitle(self.title)
        self.label.setText(f'{self.my_strings.label_found}:')

    def load_items(self, items):
        if items:
            self.show()
            self.table.load_table_data(items)
            self.table.show_all_rows()
            self.table.resizeColumnsToContents()
            self.update_label_found()
        else:
            self.hide()

    def show_rows(self, indices):
        if indices:
            self.show()
            self.table.show_rows(indices)
            self.update_label_found()
        else:
            self.hide()

    def remove_row(self, item_id):
        for i in range(self.table.rowCount()):
            if item_id == self.table.item(i, 0).item_id:
                self.table.removeRow(i)
                break
        self.update_label_found()

    def update_label_found(self):
        self.label.setText(f'{self.my_strings.label_found}: {self.table.visible_row_count}')


class VisibleGroup(BaseGroup):
    def load_items(self, items):
        if items:
            self.table.show()
            self.table.load_table_data(items)
            self.table.show_all_rows()
            self.table.resizeColumnsToContents()
            self.update_label_found()
        else:
            self.table.hide()
            self.table.visible_row_count = 0
            self.update_label_found()


# ---------------------------
# ---------- Needs ----------
# ---------------------------
class BatteryNeedGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_batteries, BatteryNeedTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_battery_need,
                                   function_delete=controller.delete_battery_need)


class BOSNeedGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_bos, BOSNeedTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_bos_need,
                                   function_delete=controller.delete_bos_need)


class InverterNeedGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_inverters, InverterNeedTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_inverter_need,
                                   function_delete=controller.delete_inverter_need)


class PanelNeedGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_panels, PanelNeedTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_panel_need,
                                   function_delete=controller.delete_panel_need)


class StructureNeedGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_structures, StructureNeedTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_structure_need,
                                   function_delete=controller.delete_structure_need)


# --------------------------------
# ---------- Quotations ----------
# --------------------------------
class BatteryQuotationGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_batteries, BatteryQuotationTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_battery_quotation,
                                   function_delete=controller.delete_battery_quotation)


class BOSQuotationGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_bos, BOSQuotationTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_bos_quotation,
                                   function_delete=controller.delete_bos_quotation)


class InverterQuotationGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_inverters, InverterQuotationTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_inverter_quotation,
                                   function_delete=controller.delete_inverter_quotation)


class PanelQuotationGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_panels, PanelQuotationTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_panel_quotation,
                                   function_delete=controller.delete_panel_quotation)


class StructureQuotationGroup(BaseGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_structures, StructureQuotationTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.c_master.setup_structure_quotation,
                                   function_delete=controller.delete_structure_quotation)


# ----------------------------------------
# ---------- Related quotations ----------
# ----------------------------------------
class RelatedPanelQuotationGroup(VisibleGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_related_panel_quotations, RelatedPanelQuotationTable)

    def connect_signals(self, controller):
        self.table.connect_signals(function_double_click=controller.double_clicked_table_rel,
                                   function_delete=None)

    def load_items(self, items):
        if items:
            self.table.show()
            self.table.load_table_data(items)
            self.table.show_all_rows()
            self.table.resizeColumnsToContents()
            self.update_label_found()
        else:
            self.table.hide()
            self.table.visible_row_count = 0
            self.update_label_found()


# ---------------------------
# ---------- Staff ----------
# ---------------------------
class StaffGroup(VisibleGroup):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings, my_strings.group_staff, StaffTable)

    def setup_gui(self):
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setUnderline(False)
        font.setBold(True)
        self.setFont(font)
        self.setObjectName('group')
        self.vertical_layout = QtWidgets.QVBoxLayout(self)
        self.vertical_layout.setContentsMargins(6, 6, 6, 6)
        self.vertical_layout.setObjectName('vertical_layout')
        self.vertical_layout.addWidget(self.table)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName('horizontal_layout')
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setObjectName('label')
        self.horizontal_layout.addWidget(self.label)
        self.button_add_employee = QtWidgets.QPushButton(self)
        self.button_add_employee.setMinimumSize(QtCore.QSize(50, 30))
        self.button_add_employee.setMaximumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.button_add_employee.setFont(font)
        self.button_add_employee.setObjectName('button_add_employee')
        self.horizontal_layout.addWidget(self.button_add_employee)
        self.vertical_layout.addLayout(self.horizontal_layout)

        self.setTitle(self.title)
        self.label.setText(f'{self.my_strings.label_total}:')
        self.button_add_employee.setIcon(QtGui.QIcon(url_plus))
        self.button_add_employee.setIconSize(QtCore.QSize(12, 12))

    def connect_signals(self, controller):
        self.button_add_employee.clicked.connect(controller.clicked_add_employee)

        self.table.connect_signals(function_double_click=controller.clicked_add_employee,
                                   function_delete=controller.delete_employee)
