from abc import abstractmethod

from guis.g_base import GBase


class GNeed(GBase):
    @abstractmethod
    def __init__(self, window):
        super().__init__(window)

    @abstractmethod
    def connect_signals(self, controller):
        super().connect_signals(controller)
        self.w.buttonAddCompany.clicked.connect(controller.clicked_add_company)

        self.w.comboMark.currentTextChanged.connect(lambda: self.w.comboMark.validate_soft())
        self.w.comboIncoterm.currentTextChanged.connect(lambda: self.w.comboIncoterm.validate_soft())
        self.w.comboMadeIn.currentTextChanged.connect(lambda: self.w.comboMadeIn.validate_soft())
        self.w.comboOrigin.currentTextChanged.connect(lambda: self.w.comboOrigin.validate_soft())
        self.w.comboDestination.currentTextChanged.connect(lambda: self.w.comboDestination.validate_soft())

        self.w.spinTotalPower.valueChanged.connect(lambda: self.w.spinTotalPower.validate_hard())
        self.w.spinPrice.valueChanged.connect(lambda: self.w.spinPrice.validate_hard())
        self.w.spinPanelPower.valueChanged.connect(lambda: self.w.spinPanelPower.validate_hard())

    @property
    def checked_certificates(self):
        return self.w.buttonCertificates.checked_items

    @checked_certificates.setter
    def checked_certificates(self, items):
        self.w.buttonCertificates.checked_items = items

    @property
    def company(self):
        return self.w.comboCompany.currentText()

    @company.setter
    def company(self, text):
        self.w.comboCompany.setCurrentText(text)

    @property
    def incoterm(self):
        return self.w.comboIncoterm.currentText()

    @incoterm.setter
    def incoterm(self, text):
        self.w.comboIncoterm.setCurrentText(text)

    @property
    def made_in(self):
        return self.w.comboMadeIn.currentText()

    @made_in.setter
    def made_in(self, text):
        self.w.comboMadeIn.setCurrentText(text)

    @property
    def mark(self):
        return self.w.comboMark.currentText()

    @mark.setter
    def mark(self, text):
        self.w.comboMark.setCurrentText(text)

    @property
    def origin(self):
        return self.w.comboOrigin.currentText()

    @origin.setter
    def origin(self, text):
        self.w.comboOrigin.setCurrentText(text)

    @property
    def price(self):
        return self.w.spinPrice.value()

    @price.setter
    def price(self, number):
        self.w.spinPrice.setValue(number)

    @property
    def total_power(self):
        return self.w.spinTotalPower.value()

    @total_power.setter
    def total_power(self, number):
        self.w.spinTotalPower.setValue(number)

    @property
    def destination(self):
        return self.w.comboDestination.currentText()

    @destination.setter
    def destination(self, text):
        self.w.comboDestination.setCurrentText(text)
