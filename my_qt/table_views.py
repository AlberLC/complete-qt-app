from PySide2 import QtGui, QtWidgets


class TableView(QtWidgets.QTableView):
    def __init__(self, my_strings, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.my_strings = my_strings

        self.function_double_click = None
        self.function_delete = None
        self.shortcut = QtWidgets.QShortcut(QtGui.QKeySequence('Ctrl+C'), self)
        self.action_delete = QtWidgets.QAction(self.my_strings.action_delete)
        self.action_copy_row = QtWidgets.QAction()
        self.action_copy_column = QtWidgets.QAction(self.my_strings.action_copy_column)
        self.menu = QtWidgets.QMenu()
        self.menu.addAction(self.action_copy_row)
        self.menu.addAction(self.action_copy_column)
        self.menu.addSeparator()
        self.menu.addAction(self.action_delete)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        self.setFont(font)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.horizontalHeader().setFont(font)
        self.horizontalHeader().setHighlightSections(False)
        self.horizontalHeader().setStretchLastSection(True)
        self.verticalHeader().hide()
        self.setSortingEnabled(True)
        self.setAlternatingRowColors(True)
        self.setStyleSheet('alternate-background-color: rgb(242, 242, 242)')

    def connect_signals(self, controller):
        self.doubleClicked.connect(lambda: controller.double_clicked_cell(self.currentIndex()))
        self.function_delete = controller.delete_items

        self.shortcut.activated.connect(self.copy_rows)

    def contextMenuEvent(self, event):
        if not self.selectedIndexes():
            return

        if len(self.selectionModel().selectedRows()) == 1:
            self.action_copy_row.setText(self.my_strings.action_copy_row)
        else:
            self.action_copy_row.setText(self.my_strings.action_copy_rows)

        res = self.menu.exec_(event.globalPos())
        if res == self.action_copy_row:
            self.copy_rows()
        elif res == self.action_copy_column:
            self.copy_column()
        elif res == self.action_delete:
            self.function_delete(self.selectionModel().selectedRows())

    def copy_column(self):
        column = self.currentIndex().column()
        header_name = self.model().headers[column]
        item_texts = []
        for row in range(self.model().rowCount()):
            if self.isRowHidden(row):
                continue
            index = self.model().index(row, column)
            item_texts.append(str(self.model().data(index)).replace('.', ','))

        text = header_name + '\n' + '\n'.join(item_texts)

        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.clear(mode=QtGui.QClipboard.Clipboard)
        clipboard.setText(text, mode=QtGui.QClipboard.Clipboard)

    def copy_rows(self):
        if not self.hasFocus():
            return

        item_texts = []
        n_columns = self.model().columnCount()

        sub_list = []
        for index in self.selectionModel().selectedIndexes():
            sub_list.append(str(self.model().data(index)).replace('.', ','))
            if len(sub_list) == n_columns:
                item_texts.append('\t'.join(sub_list))
                sub_list = []

        text = '\t'.join(self.model().headers) + '\n' + '\n'.join(item_texts)

        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.clear(mode=QtGui.QClipboard.Clipboard)
        clipboard.setText(text, mode=QtGui.QClipboard.Clipboard)

    def setModel(self, model):
        super().setModel(model)
        # self.resizeColumnsToContents()
        self.setColumnWidth(0, 50)
        self.setColumnWidth(1, 250)
