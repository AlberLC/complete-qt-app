from abc import ABC, abstractmethod

from PySide2 import QtCore, QtGui, QtWidgets

from my_qt import group_boxes
from resources import MyStrings, url_back, url_loading_mini, url_tick, url_interrogation


# noinspection PyPep8Naming
class GSearcher(ABC):
    @abstractmethod
    def __init__(self, window):
        self.w = window
        self.my_strings = MyStrings()

    # Edited: extended by inheritance
    def setup_gui(self):
        self.w.centralWidget = QtWidgets.QWidget(self.w)
        self.w.centralWidget.setObjectName('centralWidget')
        self.w.verticalLayout = QtWidgets.QVBoxLayout(self.w.centralWidget)
        self.w.verticalLayout.setObjectName('verticalLayout')
        self.w.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.w.horizontalLayout_3.setObjectName('horizontalLayout_3')
        self.w.buttonBack = QtWidgets.QPushButton(self.w.centralWidget)
        self.w.buttonBack.setMinimumSize(QtCore.QSize(50, 40))
        self.w.buttonBack.setMaximumSize(QtCore.QSize(50, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.w.buttonBack.setFont(font)
        self.w.buttonBack.setText('')
        self.w.buttonBack.setObjectName('buttonBack')
        self.w.horizontalLayout_3.addWidget(self.w.buttonBack)
        self.w.labelTitle = QtWidgets.QLabel(self.w.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.w.labelTitle.setFont(font)
        self.w.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.w.labelTitle.setObjectName('labelTitle')
        self.w.horizontalLayout_3.addWidget(self.w.labelTitle)
        spacerItem = QtWidgets.QSpacerItem(50, 40, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_3.addItem(spacerItem)
        self.w.verticalLayout.addLayout(self.w.horizontalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.w.verticalLayout.addItem(spacerItem1)
        self.w.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.w.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.w.buttonAddPanel = QtWidgets.QPushButton(self.w.centralWidget)
        self.w.buttonAddPanel.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.w.buttonAddPanel.setFont(font)
        self.w.buttonAddPanel.setObjectName('buttonAddPanel')
        self.w.horizontalLayout_2.addWidget(self.w.buttonAddPanel)
        self.w.buttonAddInverter = QtWidgets.QPushButton(self.w.centralWidget)
        self.w.buttonAddInverter.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.w.buttonAddInverter.setFont(font)
        self.w.buttonAddInverter.setObjectName('buttonAddInverter')
        self.w.horizontalLayout_2.addWidget(self.w.buttonAddInverter)
        self.w.buttonAddBattery = QtWidgets.QPushButton(self.w.centralWidget)
        self.w.buttonAddBattery.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.w.buttonAddBattery.setFont(font)
        self.w.buttonAddBattery.setObjectName('buttonAddBattery')
        self.w.horizontalLayout_2.addWidget(self.w.buttonAddBattery)
        self.w.buttonAddStructure = QtWidgets.QPushButton(self.w.centralWidget)
        self.w.buttonAddStructure.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.w.buttonAddStructure.setFont(font)
        self.w.buttonAddStructure.setObjectName('buttonAddStructure')
        self.w.horizontalLayout_2.addWidget(self.w.buttonAddStructure)
        self.w.buttonAddBOS = QtWidgets.QPushButton(self.w.centralWidget)
        self.w.buttonAddBOS.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.w.buttonAddBOS.setFont(font)
        self.w.buttonAddBOS.setObjectName('buttonAddBOS')
        self.w.horizontalLayout_2.addWidget(self.w.buttonAddBOS)
        self.w.verticalLayout.addLayout(self.w.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.w.verticalLayout.addItem(spacerItem2)
        self.w.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.w.horizontalLayout_7.setObjectName('horizontalLayout_7')
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_7.addItem(spacerItem3)
        self.w.groupSearcher = QtWidgets.QGroupBox(self.w.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupSearcher.setFont(font)
        self.w.groupSearcher.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupSearcher.setObjectName('groupSearcher')
        self.w.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.w.groupSearcher)
        self.w.horizontalLayout_5.setObjectName('horizontalLayout_5')
        self.w.lineSearcher = QtWidgets.QLineEdit(self.w.groupSearcher)
        self.w.lineSearcher.setMinimumSize(QtCore.QSize(350, 35))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setWeight(50)
        font.setBold(False)
        self.w.lineSearcher.setFont(font)
        self.w.lineSearcher.setText('')
        self.w.lineSearcher.setClearButtonEnabled(True)
        self.w.lineSearcher.setObjectName('lineSearcher')
        self.w.horizontalLayout_5.addWidget(self.w.lineSearcher)
        self.w.labelLoading = QtWidgets.QLabel(self.w.groupSearcher)
        self.w.labelLoading.setMinimumSize(QtCore.QSize(20, 20))
        self.w.labelLoading.setMaximumSize(QtCore.QSize(20, 20))
        self.w.labelLoading.setText('')
        self.w.labelLoading.setObjectName('labelLoading')
        self.w.horizontalLayout_5.addWidget(self.w.labelLoading)
        self.w.horizontalLayout_7.addWidget(self.w.groupSearcher)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_7.addItem(spacerItem4)
        self.w.horizontalLayout_7.setStretch(0, 1)
        self.w.horizontalLayout_7.setStretch(1, 3)
        self.w.horizontalLayout_7.setStretch(2, 1)
        self.w.verticalLayout.addLayout(self.w.horizontalLayout_7)
        self.w.scrollArea = QtWidgets.QScrollArea(self.w.centralWidget)
        self.w.scrollArea.setWidgetResizable(True)
        self.w.scrollArea.setObjectName('scrollArea')
        self.w.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.w.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1022, 1694))
        self.w.scrollAreaWidgetContents.setObjectName('scrollAreaWidgetContents')
        self.w.verticalLayout_3 = QtWidgets.QVBoxLayout(self.w.scrollAreaWidgetContents)
        self.w.verticalLayout_3.setSpacing(30)
        self.w.verticalLayout_3.setObjectName('verticalLayout_3')
        self.w.scrollArea.setWidget(self.w.scrollAreaWidgetContents)
        self.w.verticalLayout.addWidget(self.w.scrollArea)
        self.w.setCentralWidget(self.w.centralWidget)

        self.w.labelLoading.setVisible(False)

        self.w.buttonBack.setIcon(QtGui.QIcon(url_back))
        self.w.buttonBack.setIconSize(QtCore.QSize(32, 32))

        self.w.groupSearcher.setTitle(self.my_strings.group_searcher)

        self.w.buttonAddInverter.setDisabled(True)
        self.w.buttonAddBattery.setDisabled(True)
        self.w.buttonAddStructure.setDisabled(True)
        self.w.buttonAddBOS.setDisabled(True)

    def connect_signals(self, controller):
        self.w.buttonBack.clicked.connect(controller.c_master.go_back)

        self.w.lineSearcher.textChanged.connect(controller.search)

        self.group_panel.connect_signals(controller)
        self.group_inverter.connect_signals(controller)
        self.group_battery.connect_signals(controller)
        self.group_structure.connect_signals(controller)
        self.group_bos.connect_signals(controller)

    @property
    def group_panel(self):
        return self.w.groupPanel

    @property
    def group_inverter(self):
        return self.w.groupInverter

    @property
    def group_battery(self):
        return self.w.groupBattery

    @property
    def group_structure(self):
        return self.w.groupStructure

    @property
    def group_bos(self):
        return self.w.groupBOS

    @property
    def text_searcher(self):
        return self.w.lineSearcher.text()

    def paint_nothing(self):
        self.w.labelLoading.setVisible(False)
        self.w.labelLoading.setPixmap(None)

    def paint_interrogation(self):
        self.w.labelLoading.setVisible(True)
        self.w.labelLoading.setPixmap(QtGui.QPixmap(url_interrogation))

    def paint_loading(self):
        self.w.labelLoading.setVisible(True)
        movie = QtGui.QMovie(url_loading_mini)
        self.w.labelLoading.setMovie(movie)
        movie.start()

    def paint_tick(self):
        self.w.labelLoading.setVisible(True)
        self.w.labelLoading.setPixmap(QtGui.QPixmap(url_tick))

    def is_empty(self):
        if (
                self.group_panel.isVisible() or
                self.group_inverter.isVisible() or
                self.group_battery.isVisible() or
                self.group_structure.isVisible() or
                self.group_structure.isVisible()
        ):
            return False
        else:
            return True


class GNeeds(GSearcher):
    def __init__(self, window):
        super().__init__(window)
        super().setup_gui()
        self.setup_gui()

    def setup_gui(self):
        self.w.groupPanel = group_boxes.PanelNeedGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.groupInverter = group_boxes.InverterNeedGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.groupBattery = group_boxes.BatteryNeedGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.groupStructure = group_boxes.StructureNeedGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.groupBOS = group_boxes.BOSNeedGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.verticalLayout_3.addWidget(self.w.groupPanel)
        self.w.verticalLayout_3.addWidget(self.w.groupInverter)
        self.w.verticalLayout_3.addWidget(self.w.groupBattery)
        self.w.verticalLayout_3.addWidget(self.w.groupStructure)
        self.w.verticalLayout_3.addWidget(self.w.groupBOS)

        self.w.labelTitle.setText(self.my_strings.title_needs)

        self.w.buttonAddPanel.setText(self.my_strings.button_add_panel_n)
        self.w.buttonAddInverter.setText(self.my_strings.button_add_inverter_n)
        self.w.buttonAddBattery.setText(self.my_strings.button_add_batteries_n)
        self.w.buttonAddStructure.setText(self.my_strings.button_add_structure_n)
        self.w.buttonAddBOS.setText(self.my_strings.button_add_bos_n)

        # Coloring
        self.w.centralWidget.setStyleSheet('.QWidget{background-color: rgb(232, 242, 232)}')

    def connect_signals(self, controller):
        super().connect_signals(controller)

        self.w.buttonAddPanel.clicked.connect(controller.c_master.setup_panel_need)


class GQuotations(GSearcher):
    def __init__(self, window):
        super().__init__(window)
        super().setup_gui()
        self.setup_gui()

    def setup_gui(self):
        self.w.groupPanel = group_boxes.PanelQuotationGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.groupInverter = group_boxes.InverterQuotationGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.groupBattery = group_boxes.BatteryQuotationGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.groupStructure = group_boxes.StructureQuotationGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.groupBOS = group_boxes.BOSQuotationGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.verticalLayout_3.addWidget(self.w.groupPanel)
        self.w.verticalLayout_3.addWidget(self.w.groupInverter)
        self.w.verticalLayout_3.addWidget(self.w.groupBattery)
        self.w.verticalLayout_3.addWidget(self.w.groupStructure)
        self.w.verticalLayout_3.addWidget(self.w.groupBOS)

        self.w.labelTitle.setText(self.my_strings.title_quotations)

        self.w.buttonAddPanel.setText(self.my_strings.button_add_panel_q)
        self.w.buttonAddInverter.setText(self.my_strings.button_add_inverter_q)
        self.w.buttonAddBattery.setText(self.my_strings.button_add_batteries_q)
        self.w.buttonAddStructure.setText(self.my_strings.button_add_structure_q)
        self.w.buttonAddBOS.setText(self.my_strings.button_add_bos_q)

        # Coloring
        self.w.centralWidget.setStyleSheet('.QWidget{background-color: rgb(238, 240, 245)}')

    def connect_signals(self, controller):
        super().connect_signals(controller)

        self.w.buttonAddPanel.clicked.connect(controller.c_master.setup_panel_quotation)
