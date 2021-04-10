from abc import ABC, abstractmethod


class GPriceBarChart(ABC):
    @abstractmethod
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def connect_signals(self, controller):
        self.w.spinPrice.valueChanged.connect(self.__update_price_bar_chart)
        self.w.spinPanelPower.valueChanged.connect(controller.update_current_power_average)

    @property
    def price_bar_chart(self):
        return self.w.priceBarChart

    @property
    def price_bar_chart_current(self):
        return self.price_bar_chart.current

    @price_bar_chart_current.setter
    def price_bar_chart_current(self, value):
        self.price_bar_chart.current = value

    @property
    def price_bar_chart_all_average(self):
        return self.price_bar_chart.all_average

    @price_bar_chart_all_average.setter
    def price_bar_chart_all_average(self, value):
        self.price_bar_chart.all_average = value

    @property
    def price_bar_chart_current_type_average(self):
        return self.price_bar_chart.current_type_average

    @price_bar_chart_current_type_average.setter
    def price_bar_chart_current_type_average(self, value):
        self.price_bar_chart.current_type_average = value

    @property
    def price_bar_chart_current_power_average(self):
        return self.price_bar_chart.current_power_average

    @price_bar_chart_current_power_average.setter
    def price_bar_chart_current_power_average(self, value):
        self.price_bar_chart.current_power_average = value

    def __update_price_bar_chart(self, value):
        self.price_bar_chart_current = value
