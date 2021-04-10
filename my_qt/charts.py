from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCharts import QtCharts

from my_qt.dialogs.message_boxes import inform_save_successful, warn_critical_save_error


class PriceBarChart(QtCharts.QChartView):
    def __init__(self, my_strings):
        super().__init__()
        self.my_strings = my_strings

        self.label_current_text = self.my_strings.label_current
        self.label_all_average_text = self.my_strings.label_all_average
        self.label_current_type_average_text = self.my_strings.label_current_type_average
        self.label_current_power_average_text = self.my_strings.label_current_power_average

        self._current = 0
        self._all_average = 0
        self._current_type_average = 0
        self._current_power_average = 0

        self.setChart(self.__create_price_bar_chart())
        self.setMinimumHeight(300)
        self.setMaximumSize(600, 400)

        self.action_copy_current = QtWidgets.QAction(self.my_strings.action_copy_current_price)
        self.action_copy_all_average = QtWidgets.QAction(self.my_strings.action_copy_all_average)
        self.action_copy_current_type_average = QtWidgets.QAction(self.my_strings.action_copy_current_type_average)
        self.action_copy_current_power_average = QtWidgets.QAction(self.my_strings.action_copy_current_power_average)
        self.action_copy_all = QtWidgets.QAction(self.my_strings.action_copy_all)
        self.action_save_image = QtWidgets.QAction(self.my_strings.action_save_image)
        self.menu = QtWidgets.QMenu()
        self.menu.addActions((self.action_copy_current,
                              self.action_copy_all_average,
                              self.action_copy_current_type_average,
                              self.action_copy_current_power_average,
                              self.action_copy_all))
        self.menu.addSeparator()
        self.menu.addAction(self.action_save_image)

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value
        self.line_series.replace(0, 0, value)
        self.line_series.replace(1, 1, value)
        self.update_axis_y_maximum()

    @property
    def all_average(self):
        return self._all_average

    @all_average.setter
    def all_average(self, value):
        self._all_average = value
        self.all_average_bar_set.replace(0, value)
        self.update_axis_y_maximum()

    @property
    def current_type_average(self):
        return self._current_type_average

    @current_type_average.setter
    def current_type_average(self, value):
        self._current_type_average = value
        self.current_type_average_bar_set.replace(0, value)
        self.update_axis_y_maximum()

    @property
    def current_power_average(self):
        return self._current_power_average

    @current_power_average.setter
    def current_power_average(self, value):
        self._current_power_average = value
        self.current_power_average_bar_set.replace(0, value)
        self.update_axis_y_maximum()

    def contextMenuEvent(self, event):
        res = self.menu.exec_(event.globalPos())
        if res == self.action_copy_current:
            text = f'{self.label_current_text}\n{self.current}'
        elif res == self.action_copy_all_average:
            text = f'{self.label_all_average_text}\n{self.all_average}'
        elif res == self.action_copy_current_type_average:
            text = f'{self.label_current_type_average_text}\n{self.current_type_average}'
        elif res == self.action_copy_current_power_average:
            text = f'{self.label_current_power_average_text}\n{self.current_power_average}'
        elif res == self.action_copy_all:
            headers = '\t'.join((self.label_current_text,
                                 self.label_all_average_text,
                                 self.label_current_type_average_text,
                                 self.label_current_power_average_text))
            data = '\t'.join(str(n).replace('.', ',') for n in (self.current,
                                                                self.all_average,
                                                                self.current_type_average,
                                                                self.current_power_average))
            text = f'{headers}\n{data}'
        else:
            if res == self.action_save_image:
                self.__save_chart_image()
            return

        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.clear(mode=QtGui.QClipboard.Clipboard)
        clipboard.setText(text, mode=QtGui.QClipboard.Clipboard)

    def update_axis_y_maximum(self):
        self.axis_y.setMax(max(self.current, self.all_average, self.current_type_average, self.current_power_average))

    def __create_price_bar_chart(self):
        font = QtGui.QFont()

        chart = QtCharts.QChart()
        chart.setTitle(f'{self.my_strings.title_chart} (€/W)')
        font.setPointSize(11)
        chart.setTitleFont(font)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.legend().setVisible(True)
        font.setPointSize(10)
        chart.legend().setFont(font)
        chart.legend().setAlignment(QtCore.Qt.AlignBottom)

        bar_series = QtCharts.QBarSeries()
        bar_series.setBarWidth(0.7)
        bar_series.setLabelsVisible(True)

        font.setPointSize(11)
        self.all_average_bar_set = QtCharts.QBarSet(self.label_all_average_text)
        self.all_average_bar_set.append(self.all_average)
        self.all_average_bar_set.setLabelFont(font)
        self.current_type_average_bar_set = QtCharts.QBarSet(self.label_current_type_average_text)
        self.current_type_average_bar_set.append(self.current_type_average)
        self.current_type_average_bar_set.setLabelFont(font)
        self.current_power_average_bar_set = QtCharts.QBarSet(self.label_current_power_average_text)
        self.current_power_average_bar_set.append(self.current_power_average)
        self.current_power_average_bar_set.setLabelFont(font)

        bar_series.append(self.all_average_bar_set)
        bar_series.append(self.current_type_average_bar_set)
        bar_series.append(self.current_power_average_bar_set)
        chart.addSeries(bar_series)

        self.line_series = QtCharts.QLineSeries()
        self.line_series.setName(self.label_current_text)
        self.line_series.append(0, self.current)
        self.line_series.append(1, self.current)
        pen = self.line_series.pen()
        pen.setColor(QtGui.QColor(255, 70, 70))  # 32, 159, 223
        pen.setWidth(5)
        self.line_series.setPen(pen)
        chart.addSeries(self.line_series)

        axis_x = QtCharts.QValueAxis()
        axis_x.hide()

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setGridLineVisible(False)
        # self.axis_y.setLabelsVisible(False)
        # self.axis_y.setLineVisible(False)

        chart.addAxis(axis_x, QtCore.Qt.AlignBottom)
        chart.addAxis(self.axis_y, QtCore.Qt.AlignLeft)

        self.line_series.attachAxis(axis_x)
        bar_series.attachAxis(self.axis_y)
        self.line_series.attachAxis(self.axis_y)

        self.update_axis_y_maximum()
        self.axis_y.setMin(0)

        return chart

    def __save_chart_image(self):
        name, extension = QtWidgets.QFileDialog.getSaveFileName(parent=self,
                                                                caption='Guardar como',
                                                                dir=self.my_strings.chart,
                                                                filter='JPEG (*.jpg);; PNG (*.png)',
                                                                options=QtWidgets.QFileDialog.Options())
        if name:
            if name[-3:] in ('jpg', 'png'):
                image = QtGui.QPixmap(self.grab())
                image.save(name, quality=100)
                inform_save_successful()
            else:
                warn_critical_save_error()
