from PySide2 import QtCore, QtGui, QtWidgets

from my_qt.item_widgets import TextItemWidget, NumericItemWidget, DateItemWidget


class MenuTableWidget(QtWidgets.QTableWidget):
    def __init__(self, parent, my_strings):
        super().__init__(parent)
        self.my_strings = my_strings
        self.visible_row_count = self.rowCount()
        self.function_double_click = None
        self.function_delete = None
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+C'), self)
        self.action_delete = QtWidgets.QAction(self.my_strings.action_delete)
        self.action_copy_row = QtWidgets.QAction()
        self.action_copy_column = QtWidgets.QAction(self.my_strings.action_copy_column)
        self.menu = QtWidgets.QMenu()
        self.menu.addAction(self.action_copy_row)
        self.menu.addAction(self.action_copy_column)

        self.setMinimumSize(QtCore.QSize(0, 250))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        self.setFont(font)
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setObjectName('table')
        self.horizontalHeader().show()
        self.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().hide()
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setStyleSheet('alternate-background-color: rgb(242, 242, 242)')

    def connect_signals(self, function_double_click, function_delete):
        self.function_double_click = function_double_click
        self.function_delete = function_delete

        self.itemDoubleClicked.connect(lambda: self.function_double_click(self.currentItem().item_id))

        self.shortcut.activated.connect(self.copy_rows)

        if self.function_delete:
            self.menu.addSeparator()
            self.menu.addAction(self.action_delete)

    @property
    def data(self):
        data = []
        for row in range(self.rowCount()):
            row_data = []
            for column in range(self.columnCount()):
                row_data.append(self.item(row, column).text())
            data.append(row_data)
        return data

    def contextMenuEvent(self, event):
        if not self.selectedRanges():
            return

        if self.selectedRanges()[0].rowCount() == 1:
            self.action_copy_row.setText(self.my_strings.action_copy_row)
        else:
            self.action_copy_row.setText(self.my_strings.action_copy_rows)

        res = self.menu.exec_(event.globalPos())
        if res == self.action_copy_row:
            self.copy_rows()
        elif res == self.action_copy_column:
            self.copy_column()
        elif res == self.action_delete:
            self.function_delete(self.__get_selected_item_indices())

    def copy_column(self):
        column = self.column(self.currentItem())
        header_name = self.horizontalHeaderItem(column).text()
        item_texts = []
        for row in range(self.rowCount()):
            if self.isRowHidden(row):
                continue
            item_texts.append(self.item(row, column).text().replace('.', ','))

        text = header_name + '\n' + '\n'.join(item_texts)

        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.clear(mode=QtGui.QClipboard.Clipboard)
        clipboard.setText(text, mode=QtGui.QClipboard.Clipboard)

    def copy_rows(self):
        if not self.hasFocus():
            return

        header_names = []
        item_texts = []
        n_columns = self.columnCount()

        for column in range(n_columns):
            header_names.append(self.horizontalHeaderItem(column).text())

        sub_list = []
        for item in self.selectedItems():
            sub_list.append(item.text().replace('.', ','))
            if len(sub_list) == n_columns:
                item_texts.append('\t'.join(sub_list))
                sub_list = []

        text = '\t'.join(header_names) + '\n' + '\n'.join(item_texts)

        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.clear(mode=QtGui.QClipboard.Clipboard)
        clipboard.setText(text, mode=QtGui.QClipboard.Clipboard)

    def insertRow(self, row):
        super().insertRow(row)
        self.visible_row_count += 1

    def removeRow(self, row):
        super().removeRow(row)
        self.visible_row_count -= 1

    def setRowCount(self, rows):
        super().setRowCount(rows)
        self.visible_row_count = rows

    def show_all_rows(self):
        for i in range(self.rowCount()):
            self.showRow(i)
        self.visible_row_count = self.rowCount()

    def show_rows(self, indices):
        for i in range(self.rowCount()):
            if i in indices:
                self.showRow(i)
            else:
                self.hideRow(i)
        self.visible_row_count = len(indices)

    def __get_selected_item_indices(self):
        selected_rows = [index.row() for index in self.selectionModel().selectedRows()]
        item_ids = []

        for row in selected_rows:
            if not self.isRowHidden(row):
                item_ids.append(self.item(row, 0).item_id)

        return item_ids


# ---------------------------
# ---------- Needs ----------
# ---------------------------
class BatteryNeedTable(MenuTableWidget):
    pass


class BOSNeedTable(MenuTableWidget):
    pass


class InverterNeedTable(MenuTableWidget):
    pass


class PanelNeedTable(MenuTableWidget):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings)

        self.setColumnCount(16)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(15, item)

        self.horizontalHeaderItem(0).setText(self.my_strings.label_company)
        self.horizontalHeaderItem(1).setText(self.my_strings.label_mark)
        self.horizontalHeaderItem(2).setText(f'{self.my_strings.label_total_power} (kW)')
        self.horizontalHeaderItem(3).setText(f'{self.my_strings.label_price} (€/W)')
        self.horizontalHeaderItem(4).setText(self.my_strings.label_type)
        self.horizontalHeaderItem(5).setText(self.my_strings.label_cells)
        self.horizontalHeaderItem(6).setText(f'{self.my_strings.label_panel_power} (W)')
        self.horizontalHeaderItem(7).setText(self.my_strings.label_efficiency)
        self.horizontalHeaderItem(8).setText(self.my_strings.group_tolerance)
        self.horizontalHeaderItem(9).setText(self.my_strings.label_warranty_product)
        self.horizontalHeaderItem(10).setText(self.my_strings.label_warranty_performance)
        self.horizontalHeaderItem(11).setText(self.my_strings.label_certificates)
        self.horizontalHeaderItem(12).setText(self.my_strings.label_incoterm)
        self.horizontalHeaderItem(13).setText(self.my_strings.label_made_in)
        self.horizontalHeaderItem(14).setText(self.my_strings.label_origin)
        self.horizontalHeaderItem(15).setText(self.my_strings.label_destination)

        self.resizeColumnsToContents()

    def load_table_data(self, panel_needs):
        self.setRowCount(0)
        self.setRowCount(len(panel_needs))
        for i, panel_need in enumerate(panel_needs):
            self.setItem(i, 0, TextItemWidget(panel_need.company, panel_need.id))
            self.setItem(i, 1, TextItemWidget(panel_need.mark, panel_need.id))
            self.setItem(i, 2, NumericItemWidget(panel_need.total_power, panel_need.id))
            self.setItem(i, 3, NumericItemWidget(panel_need.price, panel_need.id))
            self.setItem(i, 4, TextItemWidget(panel_need.panel_types, panel_need.id))
            self.setItem(i, 5, TextItemWidget(panel_need.cells, panel_need.id))
            self.setItem(i, 6, NumericItemWidget(panel_need.panel_power, panel_need.id))
            self.setItem(i, 7, NumericItemWidget(panel_need.efficiency, panel_need.id))
            self.setItem(
                i,
                8,
                TextItemWidget(
                    self.my_strings.radio_positive if panel_need.tolerance else self.my_strings.radio_negative,
                    panel_need.id)
            )
            self.setItem(i, 9, NumericItemWidget(panel_need.warranty_product, panel_need.id))
            self.setItem(i, 10, NumericItemWidget(panel_need.warranty_performance, panel_need.id))
            self.setItem(i, 11, TextItemWidget(panel_need.certificates, panel_need.id))
            self.setItem(i, 12, TextItemWidget(panel_need.incoterm, panel_need.id))
            self.setItem(i, 13, TextItemWidget(panel_need.made_in, panel_need.id))
            self.setItem(i, 14, TextItemWidget(panel_need.origin, panel_need.id))
            self.setItem(i, 15, TextItemWidget(panel_need.destination, panel_need.id))


class StructureNeedTable(MenuTableWidget):
    pass


# --------------------------------
# ---------- Quotations ----------
# --------------------------------
class BatteryQuotationTable(MenuTableWidget):
    pass


class BOSQuotationTable(MenuTableWidget):
    pass


class InverterQuotationTable(MenuTableWidget):
    pass


class PanelQuotationTable(MenuTableWidget):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings)

        self.setColumnCount(21)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(20, item)

        self.horizontalHeaderItem(0).setText(self.my_strings.label_company)
        self.horizontalHeaderItem(1).setText(self.my_strings.label_mark)
        self.horizontalHeaderItem(2).setText(f'{self.my_strings.label_total_power} (kW)')
        self.horizontalHeaderItem(3).setText(f'{self.my_strings.label_price} (€/W)')
        self.horizontalHeaderItem(4).setText(self.my_strings.label_date_quotation)
        self.horizontalHeaderItem(5).setText(self.my_strings.label_date_validity)
        self.horizontalHeaderItem(6).setText(self.my_strings.label_n_contacts)
        self.horizontalHeaderItem(7).setText(self.my_strings.label_user)
        self.horizontalHeaderItem(8).setText(self.my_strings.label_observations)
        self.horizontalHeaderItem(9).setText(self.my_strings.label_type)
        self.horizontalHeaderItem(10).setText(self.my_strings.label_cells)
        self.horizontalHeaderItem(11).setText(f'{self.my_strings.label_panel_power} (W)')
        self.horizontalHeaderItem(12).setText(self.my_strings.label_efficiency)
        self.horizontalHeaderItem(13).setText(self.my_strings.group_tolerance)
        self.horizontalHeaderItem(14).setText(self.my_strings.label_warranty_product)
        self.horizontalHeaderItem(15).setText(self.my_strings.label_warranty_performance)
        self.horizontalHeaderItem(16).setText(self.my_strings.label_certificates)
        self.horizontalHeaderItem(17).setText(self.my_strings.label_incoterm)
        self.horizontalHeaderItem(18).setText(self.my_strings.label_made_in)
        self.horizontalHeaderItem(19).setText(self.my_strings.label_origin)
        self.horizontalHeaderItem(20).setText(self.my_strings.label_destination)

        self.resizeColumnsToContents()

    def load_table_data(self, panel_quotations):
        self.setRowCount(0)
        self.setRowCount(len(panel_quotations))
        for i, panel_quotation in enumerate(panel_quotations):
            self.setItem(i, 0, TextItemWidget(panel_quotation.company, panel_quotation.id))
            self.setItem(i, 1, TextItemWidget(panel_quotation.mark, panel_quotation.id))
            self.setItem(i, 2, NumericItemWidget(panel_quotation.total_power, panel_quotation.id))
            self.setItem(i, 3, NumericItemWidget(panel_quotation.price, panel_quotation.id))
            self.setItem(i, 4, DateItemWidget(panel_quotation.date_quotation, panel_quotation.id))
            self.setItem(i, 5, DateItemWidget(panel_quotation.date_validity, panel_quotation.id))
            self.setItem(i, 6, NumericItemWidget(panel_quotation.n_contacts, panel_quotation.id))
            self.setItem(i, 7, TextItemWidget(panel_quotation.user, panel_quotation.id))
            self.setItem(i, 8, TextItemWidget(panel_quotation.observations, panel_quotation.id))
            self.setItem(i, 9, TextItemWidget(panel_quotation.panel_type, panel_quotation.id))
            self.setItem(i, 10, NumericItemWidget(panel_quotation.cells, panel_quotation.id))
            self.setItem(i, 11, NumericItemWidget(panel_quotation.panel_power, panel_quotation.id))
            self.setItem(i, 12, NumericItemWidget(panel_quotation.efficiency, panel_quotation.id))
            self.setItem(
                i,
                13,
                TextItemWidget(
                    self.my_strings.radio_positive if panel_quotation.tolerance else self.my_strings.radio_negative,
                    panel_quotation.id)
            )
            self.setItem(i, 14, NumericItemWidget(panel_quotation.warranty_product, panel_quotation.id))
            self.setItem(i, 15, NumericItemWidget(panel_quotation.warranty_performance, panel_quotation.id))
            self.setItem(i, 16, TextItemWidget(panel_quotation.certificates, panel_quotation.id))
            self.setItem(i, 17, TextItemWidget(panel_quotation.incoterm, panel_quotation.id))
            self.setItem(i, 18, TextItemWidget(panel_quotation.made_in, panel_quotation.id))
            self.setItem(i, 19, TextItemWidget(panel_quotation.origin, panel_quotation.id))
            self.setItem(i, 20, TextItemWidget(panel_quotation.destination, panel_quotation.id))


class StructureQuotationTable(MenuTableWidget):
    pass


# ----------------------------------------
# ---------- Related quotations ----------
# ----------------------------------------
class RelatedPanelQuotationTable(PanelQuotationTable):
    def load_table_data(self, sorted_prioritized_panel_quotations):
        self.setRowCount(0)
        self.setRowCount(len(sorted_prioritized_panel_quotations))
        for i, sorted_prioritized_panel_quotation in enumerate(sorted_prioritized_panel_quotations):
            out_of_date = not sorted_prioritized_panel_quotation.in_date
            panel_quotation = sorted_prioritized_panel_quotation.panel_quotation
            self.setItem(i, 0, TextItemWidget(panel_quotation.company, panel_quotation.id, out_of_date))
            self.setItem(i, 1, TextItemWidget(panel_quotation.mark, panel_quotation.id, out_of_date))
            self.setItem(i, 2, NumericItemWidget(panel_quotation.total_power, panel_quotation.id, out_of_date))
            self.setItem(i, 3, NumericItemWidget(panel_quotation.price, panel_quotation.id, out_of_date))
            self.setItem(i, 4, DateItemWidget(panel_quotation.date_quotation, panel_quotation.id, out_of_date))
            self.setItem(i, 5, DateItemWidget(panel_quotation.date_validity, panel_quotation.id, out_of_date))
            self.setItem(i, 6, NumericItemWidget(panel_quotation.n_contacts, panel_quotation.id, out_of_date))
            self.setItem(i, 7, TextItemWidget(panel_quotation.user, panel_quotation.id, out_of_date))
            self.setItem(i, 8, TextItemWidget(panel_quotation.observations, panel_quotation.id, out_of_date))
            self.setItem(i, 9, TextItemWidget(panel_quotation.panel_type, panel_quotation.id, out_of_date))
            self.setItem(i, 10, NumericItemWidget(panel_quotation.cells, panel_quotation.id, out_of_date))
            self.setItem(i, 11, NumericItemWidget(panel_quotation.panel_power, panel_quotation.id, out_of_date))
            self.setItem(i, 12, NumericItemWidget(panel_quotation.efficiency, panel_quotation.id, out_of_date))
            self.setItem(
                i,
                13,
                TextItemWidget(
                    self.my_strings.radio_positive if panel_quotation.tolerance else self.my_strings.radio_negative,
                    panel_quotation.id,
                    out_of_date))
            self.setItem(i,
                         14,
                         NumericItemWidget(panel_quotation.warranty_product, panel_quotation.id, out_of_date))
            self.setItem(i,
                         15,
                         NumericItemWidget(panel_quotation.warranty_performance, panel_quotation.id, out_of_date))
            self.setItem(i, 16, TextItemWidget(panel_quotation.certificates, panel_quotation.id, out_of_date))
            self.setItem(i, 17, TextItemWidget(panel_quotation.incoterm, panel_quotation.id, out_of_date))
            self.setItem(i, 18, TextItemWidget(panel_quotation.made_in, panel_quotation.id, out_of_date))
            self.setItem(i, 19, TextItemWidget(panel_quotation.origin, panel_quotation.id, out_of_date))
            self.setItem(i, 20, TextItemWidget(panel_quotation.destination, panel_quotation.id, out_of_date))


# ---------------------------
# ---------- Staff ----------
# ---------------------------
class StaffTable(MenuTableWidget):
    def __init__(self, parent, my_strings):
        super().__init__(parent, my_strings)
        self.horizontalHeader().setStretchLastSection(False)

        self.setColumnCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.setHorizontalHeaderItem(7, item)

        self.horizontalHeaderItem(0).setText(self.my_strings.label_name)
        self.horizontalHeaderItem(1).setText(self.my_strings.label_position)
        self.horizontalHeaderItem(2).setText(self.my_strings.label_projects_type)
        self.horizontalHeaderItem(3).setText(self.my_strings.label_email)
        self.horizontalHeaderItem(4).setText(self.my_strings.label_phone)
        self.horizontalHeaderItem(5).setText(self.my_strings.label_linkedin)
        self.horizontalHeaderItem(6).setText(self.my_strings.label_language)
        self.horizontalHeaderItem(7).setText(self.my_strings.label_observations)

        self.resizeColumnsToContents()

    def load_table_data(self, employees):
        self.setRowCount(0)
        self.setRowCount(len(employees))
        for i, employee in enumerate(employees):
            self.setItem(i, 0, TextItemWidget(employee.name, employee.id))
            self.setItem(i, 1, TextItemWidget(employee.position, employee.id))
            self.setItem(i, 2, TextItemWidget(employee.projects_type, employee.id))
            self.setItem(i, 3, TextItemWidget(employee.email, employee.id))
            self.setItem(i, 4, TextItemWidget(employee.phone, employee.id))
            self.setItem(i, 5, TextItemWidget(employee.linkedin, employee.id))
            self.setItem(i, 6, TextItemWidget(employee.language, employee.id))
            self.setItem(i, 7, TextItemWidget(employee.observations, employee.id))
