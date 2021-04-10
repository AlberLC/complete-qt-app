from abc import ABC, abstractmethod

from guis.g_need import GNeed


class GQuotation(GNeed, ABC):
    @abstractmethod
    def __init__(self, window):
        super().__init__(window)
        self.valid_user_color = 'default'

    @abstractmethod
    def connect_signals(self, controller):
        super().connect_signals(controller)

        self.w.comboUser.currentTextChanged.connect(self.validate_user)

    @property
    def date_quotation(self):
        return self.w.dateQuotation.date().toPython()

    @date_quotation.setter
    def date_quotation(self, date):
        self.w.dateQuotation.setDate(date)

    @property
    def date_validity(self):
        return self.w.dateValidity.date().toPython()

    @date_validity.setter
    def date_validity(self, date):
        self.w.dateValidity.setDate(date)

    @property
    def n_contacts(self):
        return self.w.spinNContacts.value()

    @n_contacts.setter
    def n_contacts(self, number):
        self.w.spinNContacts.setValue(number)

    @property
    def observations(self):
        return self.w.textObservations.toPlainText()

    @observations.setter
    def observations(self, text):
        self.w.textObservations.setText(text)

    @property
    def user(self):
        return self.w.comboUser.currentText()

    @user.setter
    def user(self, text):
        self.w.comboUser.setCurrentText(text)

    def validate_user(self):
        if not self.user:
            if self.valid_user_color != 'red':
                self.w.comboUser.color_red()
                self.valid_user_color = 'red'
        elif self.user not in self.w.comboUser.items:
            if self.valid_user_color != 'blue':
                self.w.comboUser.color_blue()
                self.valid_user_color = 'blue'
        elif self.valid_user_color != 'default':
            self.w.comboUser.color_default()
            self.valid_user_color = 'default'
