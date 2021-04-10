from PySide2.QtWidgets import QMessageBox

from controllers.c_employee import CEmployee
from exceptions.abort_exception import AbortException
from models import try_commit, Certificate
from models.company import Company
from models.employee import Employee
from models.panel_quotation import PanelQuotation
from my_qt.dialogs.message_boxes import inform_save_successful, question_delete_company_confirmation, \
    question_exit_without_saving, warn


class CDatabase(CEmployee):
    def __init__(self, c_master, gui, previous_button_clicked):
        super().__init__(c_master, gui)
        self.headers = []
        self.table_data = []
        self.last_button_clicked = None
        self.unsaved_changes = False
        self.selected_employee = None
        self.model_classes = {
            0: Certificate,
            3: Company,
            6: Employee
        }

        if previous_button_clicked:
            self.gui.click_button(previous_button_clicked)
            self.clicked_button()

    def changed_data(self, row, column, previous_value, value):
        if previous_value == value:
            return

        ModelClass = self.model_classes[self.gui.cheked_button_index]
        if self.gui.cheked_button_index == 3:
            item = self.session.query(ModelClass).filter_by(
                id=self.table_data[row][0]).one()
            item.name = value
        else:
            nullable_columns = ModelClass.get_not_nullable_columns()
            if column in nullable_columns:
                for row_data in self.table_data:
                    if row_data[column] == value:
                        warn(self.my_strings.title_error,
                             self.my_strings.message_save_error_not_unique.format(list(nullable_columns.values())),
                             self.my_strings.button_accept)
                        self.table_data[row][column] = previous_value
                        return
            self.table_data[row][column] = value
            id_ = int(self.table_data[row][0])
            item = self.session.query(ModelClass).filter_by(id=id_).one_or_none()
            if item:
                setattr(item, self.headers[column], value)
            else:
                new_item = ModelClass(int(self.table_data[row][0]), value)
                self.session.add(new_item)
        self.unsaved_changes = True
        self.gui.show_button_save()

    def clicked_add(self):
        if self.gui.cheked_button_index == 3:
            self.c_master.previous_data = self.last_button_clicked
            self.c_master.setup_company()
        elif self.gui.cheked_button_index == 0:
            if self.table_data:
                new_id = max(row[0] for row in self.table_data) + 1
            else:
                new_id = 1
            self.table_data.append([new_id, *(None,) * (len(self.headers) - 1)])
            self.gui.load_table_data(self.headers, self.table_data, self.changed_data)
            self.unsaved_changes = True
        elif self.gui.cheked_button_index == 6:
            self.clicked_add_employee()

    def clicked_button(self):
        button_index = self.gui.cheked_button_index
        if button_index == self.last_button_clicked:
            return
        self.last_button_clicked = button_index
        self.session.rollback()
        self.gui.hide_table()
        self.gui.hide_button_save()

        if button_index not in (0, 3, 6):
            return

        ModelClass = self.model_classes[self.gui.cheked_button_index]
        self.headers = ModelClass.get_headers()
        self.table_data = [item.data for item in
                           self.session.query(ModelClass).order_by(ModelClass.name).all()]
        self.gui.load_table_data(self.headers, self.table_data, self.changed_data)
        self.gui.show_table()

    def delete_items(self, indexes):
        ModelClass = self.model_classes[self.gui.cheked_button_index]
        item_ids = [int(self.table_data[index.row()][0]) for index in indexes]
        items = self.session.query(ModelClass).filter(ModelClass.id.in_(item_ids)).all()

        if self.gui.cheked_button_index == 3:
            company_names_with_panel_quotations = []
            for item in items:
                panel_quotations = self.session.query(PanelQuotation).filter_by(company=item).all()
                if panel_quotations:
                    company_names_with_panel_quotations.append(item.name)
            if company_names_with_panel_quotations and question_delete_company_confirmation(
                    company_names_with_panel_quotations) == QMessageBox.RejectRole:
                return
        for item in items:
            self.session.delete(item)
        self.unsaved_changes = True
        self.headers = ModelClass.get_headers()
        self.table_data = [item.data for item in
                           self.session.query(ModelClass).order_by(ModelClass.name).all()]
        self.gui.load_table_data(self.headers, self.table_data, self.changed_data)
        self.gui.show_button_save()

    def double_clicked_cell(self, index):
        if self.gui.cheked_button_index == 3:
            self.c_master.previous_data = self.last_button_clicked
            self.c_master.setup_company(self.table_data[index.row()][0])
        elif self.gui.cheked_button_index == 6:
            self.selected_employee = self.session.query(Employee).filter_by(id=self.table_data[index.row()][0]).one()
            self.clicked_add_employee(self.selected_employee.id)

    def exit(self):
        if self.unsaved_changes:
            if question_exit_without_saving() == QMessageBox.RejectRole:
                raise AbortException('No exit')
            self.session.rollback()

    def save(self):
        if self.gui.cheked_button_index == 0 and [i for i, row in enumerate(self.table_data) if None in row]:
            warn(self.my_strings.title_error,
                 self.my_strings.message_save_error_not_null.format(
                     list(self.model_classes[self.gui.cheked_button_index].get_not_nullable_columns().values())),
                 self.my_strings.button_accept)
            return
        try_commit(self.session)
        inform_save_successful()
        self.unsaved_changes = False
        self.gui.hide_button_save()

    def save_employee(self):
        data = self.get_data_employee()

        if self.selected_employee:
            self.selected_employee.set_data(data)
        else:
            new_employee = Employee(None, *data)
            self.session.add(new_employee)

        ModelClass = self.model_classes[self.gui.cheked_button_index]
        self.table_data = [item.data for item in
                           self.session.query(ModelClass).order_by(ModelClass.name).all()]
        self.gui.load_table_data(self.headers, self.table_data, self.changed_data)

        self.unsaved_changes = True
        self.gui.show_button_save()
