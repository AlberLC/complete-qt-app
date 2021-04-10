from abc import ABC, abstractmethod

from PySide2.QtWidgets import QMessageBox

from controllers.c_base import CBase
from exceptions.abort_exception import AbortException
from models import try_flush, Language
from models.employee import Employee
from my_qt.dialogs.add_employee_dialog import AddEmployeeDialog
from my_qt.dialogs.message_boxes import question_delete_confirmation, warn
from utilities.various import to_none


class CEmployee(CBase, ABC):
    def clicked_add_employee(self, employee_id=None):
        language_names = [language.name for language in self.session.query(Language).all()]
        company_name = getattr(self.gui, 'name', None)
        self.dialog = AddEmployeeDialog(language_names, company_name)
        if employee_id:
            self.selected_employee = self.session.query(Employee).filter_by(id=employee_id).one()
            self.dialog.load_item_data(self.selected_employee)
        else:
            self.selected_employee = None
        self.dialog.connect_signals(self)
        self.dialog.exec_()

    def clicked_save_employee(self):
        try:
            self.save_employee()
        except AbortException:
            return
        self.dialog.accept()
        self.staff_changed = True

    def delete_employee(self, employee_ids):
        if len(employee_ids) > 1 and question_delete_confirmation() == QMessageBox.RejectRole:
            return
        for employee_id in employee_ids:
            employee = self.session.query(Employee).filter_by(id=employee_id).one()
            self.item.staff.remove(employee)
            self.session.delete(employee)
            self.gui.group_staff.remove_row(employee_id)
        self.staff_changed = True

    def get_data_employee(self):
        name = self.dialog.name

        if not name:
            warn(self.my_strings.title_error, self.my_strings.message_save_error_required_name,
                 self.my_strings.button_accept)
            raise AbortException('No saved: empty required fields')

        position = self.dialog.position
        projects_type = self.dialog.projects_type
        email = self.dialog.email
        phone = self.dialog.phone
        linkedin = self.dialog.linkedin
        observations = self.dialog.observations

        language = self.session.query(Language).filter_by(name=self.dialog.language).one_or_none()
        if not language and self.dialog.language:
            language = Language(None, self.dialog.language)
            self.session.add(language)
            try_flush(self.session)

        data = [name, position, projects_type, email, phone, linkedin, language, observations]
        to_none(data)

        if not self.save_employee_unique_check(data):
            raise AbortException('No saved: not unique')

        return data

    @abstractmethod
    def save_employee(self):
        pass

    def save_employee_unique_check(self, data):
        employees = self.session.query(Employee).filter_by(
            name=data[0],
            position=data[1],
            projects_type=data[2],
            email=data[3],
            phone=data[4],
            linkedin=data[5],
            language=data[6],
            observations=data[7]
        ).all()

        if employees:
            warn(self.my_strings.title_error,
                 self.my_strings.message_save_error_employee_not_unique,
                 self.my_strings.button_accept)
            return False

        return True
