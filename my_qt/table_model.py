import operator
from datetime import date

from PySide2 import QtCore


class BaseTableModel(QtCore.QAbstractTableModel):
    def __init__(self, parent, headers, table_data, function_data_changed):
        super().__init__(parent)
        self.my_strings = self.parent().my_strings
        self.headers = headers
        self.table_data = table_data
        self.function_data_changed = function_data_changed

    def connect_signals(self, controller):
        self.dataChanged.connect(controller.changed_data)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        row = index.row()
        column = index.column()
        if role in (QtCore.Qt.DisplayRole, QtCore.Qt.EditRole):
            cell_data = self.table_data[row][column]
            if cell_data is '' or (type(cell_data) in (int, float) and not cell_data):
                return '-'
            else:
                return str(cell_data) if cell_data else '-'
        elif role == QtCore.Qt.TextAlignmentRole:
            if column != 1:
                return QtCore.Qt.AlignCenter
            else:
                return QtCore.Qt.AlignVCenter

    def flags(self, index):
        if index.column() == 0:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
        else:
            return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        # if index.column() > 0:
        #     return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable
        # elif index.column() == 1:
        #     return QtCore.Qt.DecorationRole
        # else:
        #     return QtCore.Qt.ItemIsSelectable

    def rowCount(self, *args, **kwargs):
        return len(self.table_data)

    def columnCount(self, *args, **kwargs):
        return len(self.headers)

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self.headers[section]

    # def setData(self, index, value, role=QtCore.Qt.EditRole):
    #     self.table_data[index.row()][index.column()] = value
    #     print(self.table_data)
    #     return True
    # if index.isValid():
    #     selected_row = self.user_data[index.row()]
    #     selected_column = self.columns[index.column()]
    #     selected_row[selected_column] = value
    #     self.dataChanged.emit(index, index, (QtCore.Qt.DisplayRole, ))
    #     ok = databaseOperations.update_existing(selected_row['_id'], selected_row)
    #     if ok:
    #         return True
    # return False

    def sort(self, column, order=None):
        self.layoutAboutToBeChanged.emit()
        self.table_data.sort(key=operator.itemgetter(column), reverse=order == QtCore.Qt.SortOrder.DescendingOrder)
        self.layoutChanged.emit()

    # def insertRows(self):
    #     pass
    # row_count = len(self.user_data)
    # self.beginInsertRows(QtCore.QModelIndex(), row_count, row_count)
    # empty_data = { key: None for key in self.columns if not key=='_id'}
    # document_id = databaseOperations.insert_data(empty_data)
    # new_data = databaseOperations.get_single_data(document_id)
    # self.user_data.append(new_data)
    # row_count += 1
    # self.endInsertRows()
    # return True

    # def removeRows(self, position):
    #     pass
    # row_count = self.rowCount()
    # row_count -= 1
    # self.beginRemoveRows(QtCore.QModelIndex(), row_count, row_count)
    # row_id = position.row()
    # document_id = self.user_data[row_id]['_id']
    # databaseOperations.remove_data(document_id)
    # self.user_data.pop(row_id)
    # self.endRemoveRows()
    # return True


class CertificateTableModel(BaseTableModel):
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        previous_value = self.table_data[index.row()][index.column()]
        # self.table_data[index.row()][index.column()] = value
        self.function_data_changed(index.row(), index.column(), previous_value, value)
        return True


class CompanyTableModel(BaseTableModel):
    def __init__(self, parent, headers, table_data, function_data_changed):
        row_count = len(table_data)
        column_count = len(headers)
        for i in range(row_count):
            for j in range(column_count):
                if table_data[i][j] is None:
                    if j in (2, 3, 5, 6, 7, 8, 9, 19, 20, 21, 22, 23, 24, 25):
                        table_data[i][j] = ''
                    elif j in (12, 14, 15, 16, 17):
                        table_data[i][j] = 0
        super().__init__(parent, headers, table_data, function_data_changed)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        row = index.row()
        column = index.column()
        if role in (QtCore.Qt.DisplayRole, QtCore.Qt.EditRole):
            cell_data = self.table_data[row][column]
            if cell_data is '' or (type(cell_data) in (int, float) and not cell_data):
                return '-'
            if column in (4, 11):
                if cell_data != date(1752, 9, 14):
                    return str(self.table_data[row][column].strftime('%d/%m/%Y'))
                else:
                    return '-'
            elif column in (10, 13, 18):
                return self.my_strings.radio_yes if cell_data else self.my_strings.radio_no
            else:
                return str(cell_data) if cell_data else '-'
        elif role == QtCore.Qt.TextAlignmentRole:
            if column != 1:
                return QtCore.Qt.AlignCenter
            else:
                return QtCore.Qt.AlignVCenter

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable


class EmployeeTableModel(BaseTableModel):
    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable
