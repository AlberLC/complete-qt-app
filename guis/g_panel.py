from abc import ABC, abstractmethod


class GPanel(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def connect_signals(self, controller):
        self.w.spinWarrantyProduct.valueChanged.connect(self._update_suffix_year)
        self.w.spinWarrantyPerformance.valueChanged.connect(self._update_suffix_year)

    @property
    def efficiency(self):
        return self.w.spinEfficiency.value()

    @efficiency.setter
    def efficiency(self, number):
        self.w.spinEfficiency.setValue(number)

    @property
    def panel_power(self):
        return self.w.spinPanelPower.value()

    @panel_power.setter
    def panel_power(self, number):
        self.w.spinPanelPower.setValue(number)

    @property
    def tolerance(self):
        return self.w.radioPositiveTolerance.isChecked()

    @tolerance.setter
    def tolerance(self, positive):
        if positive:
            self.w.radioPositiveTolerance.setChecked(True)
        else:
            self.w.radioNegativeTolerance.setChecked(True)

    @property
    def warranty_performance(self):
        return self.w.spinWarrantyPerformance.value()

    @warranty_performance.setter
    def warranty_performance(self, number):
        self.w.spinWarrantyPerformance.setValue(number)

    @property
    def warranty_product(self):
        return self.w.spinWarrantyProduct.value()

    @warranty_product.setter
    def warranty_product(self, number):
        self.w.spinWarrantyProduct.setValue(number)

    def _update_suffix_year(self):
        if self.warranty_product == 1:
            self.w.spinWarrantyProduct.setSuffix(f' {self.my_strings.suffix_year}')
        else:
            self.w.spinWarrantyProduct.setSuffix(f' {self.my_strings.suffix_years}')

        if self.warranty_performance == 1:
            self.w.spinWarrantyPerformance.setSuffix(f' {self.my_strings.suffix_year}')
        else:
            self.w.spinWarrantyPerformance.setSuffix(f' {self.my_strings.suffix_years}')
