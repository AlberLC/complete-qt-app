from abc import ABC, abstractmethod

from PySide2.QtWidgets import QMessageBox
from sqlalchemy.exc import DataError

from exceptions.abort_exception import AbortException
from my_qt.dialogs.message_boxes import question_exit_without_saving, warn_critical_save_error
from resources import MyStrings


class CBase(ABC):
    @abstractmethod
    def __init__(self, c_master, gui, current_item_data=None):
        self.c_master = c_master
        self.gui = gui
        self.session = self.c_master.Session()
        self.my_strings = MyStrings()
        self.original_data = None
        self.current_item_data = current_item_data

    def clicked_back(self):
        try:
            self.exit()
        except AbortException:
            return
        self.c_master.go_back()

    def clicked_save(self, overwrite: bool = False):
        try:
            self.save(overwrite)
        except AbortException:
            return
        except DataError as e:
            self.session.rollback()
            warn_critical_save_error()
            raise e
        if overwrite:
            self.c_master.go_back()

    def exit(self):
        if self.gui.data != self.original_data:
            if question_exit_without_saving() == QMessageBox.RejectRole:
                raise AbortException('No exit')
            self.session.rollback()

    def initialize_gui(self):
        self.load_initial_data()
        self.original_data = self.gui.data

        if self.item:
            self.gui.load_item_data(self.item)
            self.original_data = self.gui.data

        if self.current_item_data:
            self.gui.load_item_data(self.current_item_data)
