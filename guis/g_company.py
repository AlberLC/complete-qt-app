from collections import namedtuple

from PySide2 import QtCore, QtGui, QtWidgets

from guis.g_base import GBase
from my_qt.buttons import CheckableMenuButton
from my_qt.combo_boxes import SearchCombo
from my_qt.date_edits import NoWheelDateEdit
from my_qt.group_boxes import StaffGroup
from my_qt.spin_boxes import NoWheelSpinBox, NoWheelDoubleSpinBox
from resources import url_back, url_save
from utilities.various import color_gray, color_red, color_default_line, color_red_line


class GCompany(GBase):
    def __init__(self, window):
        super().__init__(window)
        self.valid_name = True

        self.setup_gui()

    # Edited: SearchCombo, CheckableMenuButton, NoWheelSpinBox, NoWheelDoubleSpinBox, NoWheelDateEdit, StaffGroup(+delete below)
    def setup_gui(self):
        self.w.centralWidget = QtWidgets.QWidget(self.w)
        self.w.centralWidget.setObjectName('centralWidget')
        self.w.verticalLayout_2 = QtWidgets.QVBoxLayout(self.w.centralWidget)
        self.w.verticalLayout_2.setObjectName('verticalLayout_2')
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
        self.w.verticalLayout_2.addLayout(self.w.horizontalLayout_3)
        self.w.scrollArea = QtWidgets.QScrollArea(self.w.centralWidget)
        self.w.scrollArea.setWidgetResizable(True)
        self.w.scrollArea.setObjectName('scrollArea')
        self.w.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.w.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -1154, 1174, 2031))
        self.w.scrollAreaWidgetContents.setObjectName('scrollAreaWidgetContents')
        self.w.verticalLayout = QtWidgets.QVBoxLayout(self.w.scrollAreaWidgetContents)
        self.w.verticalLayout.setSpacing(20)
        self.w.verticalLayout.setObjectName('verticalLayout')
        self.w.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.w.horizontalLayout_4.setObjectName('horizontalLayout_4')
        spacerItem1 = QtWidgets.QSpacerItem(50, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_4.addItem(spacerItem1)
        self.w.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_3.setObjectName('verticalLayout_3')
        self.w.groupGeneral = QtWidgets.QGroupBox(self.w.scrollAreaWidgetContents)
        self.w.groupGeneral.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupGeneral.setFont(font)
        self.w.groupGeneral.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupGeneral.setObjectName('groupGeneral')
        self.w.verticalLayout_4 = QtWidgets.QVBoxLayout(self.w.groupGeneral)
        self.w.verticalLayout_4.setSpacing(20)
        self.w.verticalLayout_4.setObjectName('verticalLayout_4')
        self.w.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_12.setSpacing(2)
        self.w.verticalLayout_12.setObjectName('verticalLayout_12')
        self.w.labelName = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelName.setFont(font)
        self.w.labelName.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelName.setObjectName('labelName')
        self.w.verticalLayout_12.addWidget(self.w.labelName)
        self.w.lineName = QtWidgets.QLineEdit(self.w.groupGeneral)
        self.w.lineName.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.lineName.setFont(font)
        self.w.lineName.setObjectName('lineName')
        self.w.verticalLayout_12.addWidget(self.w.lineName)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_12)
        self.w.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_33.setSpacing(2)
        self.w.verticalLayout_33.setObjectName('verticalLayout_33')
        self.w.labelCompanyType = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelCompanyType.setFont(font)
        self.w.labelCompanyType.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelCompanyType.setObjectName('labelCompanyType')
        self.w.verticalLayout_33.addWidget(self.w.labelCompanyType)
        self.w.buttonCompanyType = CheckableMenuButton(self.w.groupGeneral)
        self.w.buttonCompanyType.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonCompanyType.setFont(font)
        self.w.buttonCompanyType.setText('')
        self.w.buttonCompanyType.setObjectName('buttonCompanyType')
        self.w.verticalLayout_33.addWidget(self.w.buttonCompanyType)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_33)
        self.w.verticalLayout_28 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_28.setSpacing(2)
        self.w.verticalLayout_28.setObjectName('verticalLayout_28')
        self.w.labelComments = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelComments.setFont(font)
        self.w.labelComments.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelComments.setObjectName('labelComments')
        self.w.verticalLayout_28.addWidget(self.w.labelComments)
        self.w.textComments = QtWidgets.QTextEdit(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.textComments.setFont(font)
        self.w.textComments.setObjectName('textComments')
        self.w.verticalLayout_28.addWidget(self.w.textComments)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_28)
        self.w.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_13.setSpacing(2)
        self.w.verticalLayout_13.setObjectName('verticalLayout_13')
        self.w.labelSource = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelSource.setFont(font)
        self.w.labelSource.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelSource.setObjectName('labelSource')
        self.w.verticalLayout_13.addWidget(self.w.labelSource)
        self.w.lineSource = QtWidgets.QLineEdit(self.w.groupGeneral)
        self.w.lineSource.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.lineSource.setFont(font)
        self.w.lineSource.setObjectName('lineSource')
        self.w.verticalLayout_13.addWidget(self.w.lineSource)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_13)
        self.w.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_14.setSpacing(2)
        self.w.verticalLayout_14.setObjectName('verticalLayout_14')
        self.w.labelUser = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelUser.setFont(font)
        self.w.labelUser.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelUser.setObjectName('labelUser')
        self.w.verticalLayout_14.addWidget(self.w.labelUser)
        self.w.comboUser = SearchCombo(self.w.groupGeneral)
        self.w.comboUser.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.comboUser.setFont(font)
        self.w.comboUser.setObjectName('comboUser')
        self.w.verticalLayout_14.addWidget(self.w.comboUser)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_14)
        self.w.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_15.setSpacing(2)
        self.w.verticalLayout_15.setObjectName('verticalLayout_15')
        self.w.labelDateLoading = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelDateLoading.setFont(font)
        self.w.labelDateLoading.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelDateLoading.setObjectName('labelDateLoading')
        self.w.verticalLayout_15.addWidget(self.w.labelDateLoading)
        self.w.dateLoading = NoWheelDateEdit(self.w.groupGeneral)
        self.w.dateLoading.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.dateLoading.setFont(font)
        self.w.dateLoading.setCalendarPopup(True)
        self.w.dateLoading.setObjectName('dateLoading')
        self.w.verticalLayout_15.addWidget(self.w.dateLoading)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_15)
        self.w.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_16.setSpacing(2)
        self.w.verticalLayout_16.setObjectName('verticalLayout_16')
        self.w.labelCountry = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelCountry.setFont(font)
        self.w.labelCountry.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelCountry.setObjectName('labelCountry')
        self.w.verticalLayout_16.addWidget(self.w.labelCountry)
        self.w.comboCountry = SearchCombo(self.w.groupGeneral)
        self.w.comboCountry.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.comboCountry.setFont(font)
        self.w.comboCountry.setObjectName('comboCountry')
        self.w.verticalLayout_16.addWidget(self.w.comboCountry)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_16)
        self.w.verticalLayout_27 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_27.setSpacing(2)
        self.w.verticalLayout_27.setObjectName('verticalLayout_27')
        self.w.labelProvince = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelProvince.setFont(font)
        self.w.labelProvince.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelProvince.setObjectName('labelProvince')
        self.w.verticalLayout_27.addWidget(self.w.labelProvince)
        self.w.comboProvince = SearchCombo(self.w.groupGeneral)
        self.w.comboProvince.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.comboProvince.setFont(font)
        self.w.comboProvince.setObjectName('comboProvince')
        self.w.verticalLayout_27.addWidget(self.w.comboProvince)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_27)
        self.w.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_17.setSpacing(2)
        self.w.verticalLayout_17.setObjectName('verticalLayout_17')
        self.w.labelGeoZone = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelGeoZone.setFont(font)
        self.w.labelGeoZone.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelGeoZone.setObjectName('labelGeoZone')
        self.w.verticalLayout_17.addWidget(self.w.labelGeoZone)
        self.w.comboGeoZone = SearchCombo(self.w.groupGeneral)
        self.w.comboGeoZone.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.comboGeoZone.setFont(font)
        self.w.comboGeoZone.setObjectName('comboGeoZone')
        self.w.verticalLayout_17.addWidget(self.w.comboGeoZone)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_17)
        self.w.verticalLayout_23 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_23.setSpacing(2)
        self.w.verticalLayout_23.setObjectName('verticalLayout_23')
        self.w.labelAddress = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelAddress.setFont(font)
        self.w.labelAddress.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelAddress.setObjectName('labelAddress')
        self.w.verticalLayout_23.addWidget(self.w.labelAddress)
        self.w.lineAddress = QtWidgets.QLineEdit(self.w.groupGeneral)
        self.w.lineAddress.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.lineAddress.setFont(font)
        self.w.lineAddress.setObjectName('lineAddress')
        self.w.verticalLayout_23.addWidget(self.w.lineAddress)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_23)
        self.w.verticalLayout_24 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_24.setSpacing(2)
        self.w.verticalLayout_24.setObjectName('verticalLayout_24')
        self.w.labelEmail = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelEmail.setFont(font)
        self.w.labelEmail.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelEmail.setObjectName('labelEmail')
        self.w.verticalLayout_24.addWidget(self.w.labelEmail)
        self.w.lineEmail = QtWidgets.QLineEdit(self.w.groupGeneral)
        self.w.lineEmail.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.lineEmail.setFont(font)
        self.w.lineEmail.setObjectName('lineEmail')
        self.w.verticalLayout_24.addWidget(self.w.lineEmail)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_24)
        self.w.verticalLayout_54 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_54.setSpacing(2)
        self.w.verticalLayout_54.setObjectName('verticalLayout_54')
        self.w.labelPhone = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelPhone.setFont(font)
        self.w.labelPhone.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelPhone.setObjectName('labelPhone')
        self.w.verticalLayout_54.addWidget(self.w.labelPhone)
        self.w.linePhone = QtWidgets.QLineEdit(self.w.groupGeneral)
        self.w.linePhone.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.linePhone.setFont(font)
        self.w.linePhone.setObjectName('linePhone')
        self.w.verticalLayout_54.addWidget(self.w.linePhone)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_54)
        self.w.verticalLayout_25 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_25.setSpacing(2)
        self.w.verticalLayout_25.setObjectName('verticalLayout_25')
        self.w.labelWeb = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelWeb.setFont(font)
        self.w.labelWeb.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelWeb.setObjectName('labelWeb')
        self.w.verticalLayout_25.addWidget(self.w.labelWeb)
        self.w.lineWeb = QtWidgets.QLineEdit(self.w.groupGeneral)
        self.w.lineWeb.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.lineWeb.setFont(font)
        self.w.lineWeb.setObjectName('lineWeb')
        self.w.verticalLayout_25.addWidget(self.w.lineWeb)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_25)
        self.w.verticalLayout_26 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_26.setSpacing(2)
        self.w.verticalLayout_26.setObjectName('verticalLayout_26')
        self.w.labelIDDocument = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelIDDocument.setFont(font)
        self.w.labelIDDocument.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelIDDocument.setObjectName('labelIDDocument')
        self.w.verticalLayout_26.addWidget(self.w.labelIDDocument)
        self.w.lineIDDocument = QtWidgets.QLineEdit(self.w.groupGeneral)
        self.w.lineIDDocument.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.lineIDDocument.setFont(font)
        self.w.lineIDDocument.setObjectName('lineIDDocument')
        self.w.verticalLayout_26.addWidget(self.w.lineIDDocument)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_26)
        self.w.groupSolarnubVerification = QtWidgets.QGroupBox(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.groupSolarnubVerification.setFont(font)
        self.w.groupSolarnubVerification.setObjectName('groupSolarnubVerification')
        self.w.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.w.groupSolarnubVerification)
        self.w.horizontalLayout_5.setObjectName('horizontalLayout_5')
        self.w.radioYesSolarnubVerification = QtWidgets.QRadioButton(self.w.groupSolarnubVerification)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.radioYesSolarnubVerification.setFont(font)
        self.w.radioYesSolarnubVerification.setChecked(True)
        self.w.radioYesSolarnubVerification.setObjectName('radioYesSolarnubVerification')
        self.w.horizontalLayout_5.addWidget(self.w.radioYesSolarnubVerification)
        self.w.radioNoSolarnubVerification = QtWidgets.QRadioButton(self.w.groupSolarnubVerification)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.radioNoSolarnubVerification.setFont(font)
        self.w.radioNoSolarnubVerification.setObjectName('radioNoSolarnubVerification')
        self.w.horizontalLayout_5.addWidget(self.w.radioNoSolarnubVerification)
        self.w.verticalLayout_4.addWidget(self.w.groupSolarnubVerification)
        self.w.verticalLayout_30 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_30.setSpacing(2)
        self.w.verticalLayout_30.setObjectName('verticalLayout_30')
        self.w.labelDateVerification = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelDateVerification.setFont(font)
        self.w.labelDateVerification.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelDateVerification.setObjectName('labelDateVerification')
        self.w.verticalLayout_30.addWidget(self.w.labelDateVerification)
        self.w.dateVerification = NoWheelDateEdit(self.w.groupGeneral)
        self.w.dateVerification.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.dateVerification.setFont(font)
        self.w.dateVerification.setCalendarPopup(True)
        self.w.dateVerification.setObjectName('dateVerification')
        self.w.verticalLayout_30.addWidget(self.w.dateVerification)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_30)
        self.w.verticalLayout_34 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_34.setSpacing(2)
        self.w.verticalLayout_34.setObjectName('verticalLayout_34')
        self.w.labelVerificationUser = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelVerificationUser.setFont(font)
        self.w.labelVerificationUser.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelVerificationUser.setObjectName('labelVerificationUser')
        self.w.verticalLayout_34.addWidget(self.w.labelVerificationUser)
        self.w.comboVerificationUser = SearchCombo(self.w.groupGeneral)
        self.w.comboVerificationUser.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.comboVerificationUser.setFont(font)
        self.w.comboVerificationUser.setObjectName('comboVerificationUser')
        self.w.verticalLayout_34.addWidget(self.w.comboVerificationUser)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_34)
        self.w.verticalLayout_35 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_35.setSpacing(2)
        self.w.verticalLayout_35.setObjectName('verticalLayout_35')
        self.w.labelTier = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelTier.setFont(font)
        self.w.labelTier.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelTier.setObjectName('labelTier')
        self.w.verticalLayout_35.addWidget(self.w.labelTier)
        self.w.comboTier = SearchCombo(self.w.groupGeneral)
        self.w.comboTier.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.comboTier.setFont(font)
        self.w.comboTier.setObjectName('comboTier')
        self.w.verticalLayout_35.addWidget(self.w.comboTier)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_35)
        self.w.verticalLayout_36 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_36.setSpacing(2)
        self.w.verticalLayout_36.setObjectName('verticalLayout_36')
        self.w.labelFormationYear = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelFormationYear.setFont(font)
        self.w.labelFormationYear.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelFormationYear.setObjectName('labelFormationYear')
        self.w.verticalLayout_36.addWidget(self.w.labelFormationYear)
        self.w.spinFormationYear = NoWheelSpinBox(self.w.groupGeneral)
        self.w.spinFormationYear.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.spinFormationYear.setFont(font)
        self.w.spinFormationYear.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.w.spinFormationYear.setMaximum(999999999)
        self.w.spinFormationYear.setObjectName('spinFormationYear')
        self.w.verticalLayout_36.addWidget(self.w.spinFormationYear)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_36)
        self.w.groupRelWithThisCompany = QtWidgets.QGroupBox(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.groupRelWithThisCompany.setFont(font)
        self.w.groupRelWithThisCompany.setObjectName('groupRelWithThisCompany')
        self.w.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.w.groupRelWithThisCompany)
        self.w.horizontalLayout_7.setObjectName('horizontalLayout_7')
        self.w.radioYesRelWithThisCompany = QtWidgets.QRadioButton(self.w.groupRelWithThisCompany)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.radioYesRelWithThisCompany.setFont(font)
        self.w.radioYesRelWithThisCompany.setChecked(True)
        self.w.radioYesRelWithThisCompany.setObjectName('radioYesRelWithThisCompany')
        self.w.horizontalLayout_7.addWidget(self.w.radioYesRelWithThisCompany)
        self.w.radioNoRelWithThisCompany = QtWidgets.QRadioButton(self.w.groupRelWithThisCompany)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.radioNoRelWithThisCompany.setFont(font)
        self.w.radioNoRelWithThisCompany.setObjectName('radioNoRelWithThisCompany')
        self.w.horizontalLayout_7.addWidget(self.w.radioNoRelWithThisCompany)
        self.w.verticalLayout_4.addWidget(self.w.groupRelWithThisCompany)
        self.w.verticalLayout_41 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_41.setSpacing(2)
        self.w.verticalLayout_41.setObjectName('verticalLayout_41')
        self.w.labelAnnualCapacity = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelAnnualCapacity.setFont(font)
        self.w.labelAnnualCapacity.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelAnnualCapacity.setObjectName('labelAnnualCapacity')
        self.w.verticalLayout_41.addWidget(self.w.labelAnnualCapacity)
        self.w.spinAnnualCapacity = NoWheelDoubleSpinBox(self.w.groupGeneral)
        self.w.spinAnnualCapacity.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.spinAnnualCapacity.setFont(font)
        self.w.spinAnnualCapacity.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.w.spinAnnualCapacity.setDecimals(2)
        self.w.spinAnnualCapacity.setMaximum(9999999999.0)
        self.w.spinAnnualCapacity.setObjectName('spinAnnualCapacity')
        self.w.verticalLayout_41.addWidget(self.w.spinAnnualCapacity)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_41)
        self.w.verticalLayout_38 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_38.setSpacing(2)
        self.w.verticalLayout_38.setObjectName('verticalLayout_38')
        self.w.labelScopeRange = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelScopeRange.setFont(font)
        self.w.labelScopeRange.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelScopeRange.setObjectName('labelScopeRange')
        self.w.verticalLayout_38.addWidget(self.w.labelScopeRange)
        self.w.comboScopeRange = SearchCombo(self.w.groupGeneral)
        self.w.comboScopeRange.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.comboScopeRange.setFont(font)
        self.w.comboScopeRange.setObjectName('comboScopeRange')
        self.w.verticalLayout_38.addWidget(self.w.comboScopeRange)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_38)
        self.w.verticalLayout_31 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_31.setSpacing(2)
        self.w.verticalLayout_31.setObjectName('verticalLayout_31')
        self.w.labelReplyRatio = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelReplyRatio.setFont(font)
        self.w.labelReplyRatio.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelReplyRatio.setObjectName('labelReplyRatio')
        self.w.verticalLayout_31.addWidget(self.w.labelReplyRatio)
        self.w.spinReplyRatio = NoWheelDoubleSpinBox(self.w.groupGeneral)
        self.w.spinReplyRatio.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.spinReplyRatio.setFont(font)
        self.w.spinReplyRatio.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.w.spinReplyRatio.setDecimals(2)
        self.w.spinReplyRatio.setMaximum(100.0)
        self.w.spinReplyRatio.setObjectName('spinReplyRatio')
        self.w.verticalLayout_31.addWidget(self.w.spinReplyRatio)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_31)
        self.w.verticalLayout_39 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_39.setSpacing(2)
        self.w.verticalLayout_39.setObjectName('verticalLayout_39')
        self.w.labelNContacts = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelNContacts.setFont(font)
        self.w.labelNContacts.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelNContacts.setObjectName('labelNContacts')
        self.w.verticalLayout_39.addWidget(self.w.labelNContacts)
        self.w.spinNContacts = NoWheelSpinBox(self.w.groupGeneral)
        self.w.spinNContacts.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.spinNContacts.setFont(font)
        self.w.spinNContacts.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.w.spinNContacts.setMaximum(999999999)
        self.w.spinNContacts.setObjectName('spinNContacts')
        self.w.verticalLayout_39.addWidget(self.w.spinNContacts)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_39)
        self.w.verticalLayout_40 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_40.setSpacing(2)
        self.w.verticalLayout_40.setObjectName('verticalLayout_40')
        self.w.labelNReplies = QtWidgets.QLabel(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelNReplies.setFont(font)
        self.w.labelNReplies.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelNReplies.setObjectName('labelNReplies')
        self.w.verticalLayout_40.addWidget(self.w.labelNReplies)
        self.w.spinNReplies = NoWheelSpinBox(self.w.groupGeneral)
        self.w.spinNReplies.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.spinNReplies.setFont(font)
        self.w.spinNReplies.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.w.spinNReplies.setMaximum(999999999)
        self.w.spinNReplies.setObjectName('spinNReplies')
        self.w.verticalLayout_40.addWidget(self.w.spinNReplies)
        self.w.verticalLayout_4.addLayout(self.w.verticalLayout_40)
        self.w.groupSignedDocument = QtWidgets.QGroupBox(self.w.groupGeneral)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.groupSignedDocument.setFont(font)
        self.w.groupSignedDocument.setObjectName('groupSignedDocument')
        self.w.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.w.groupSignedDocument)
        self.w.horizontalLayout_8.setObjectName('horizontalLayout_8')
        self.w.radioYesSignedDocument = QtWidgets.QRadioButton(self.w.groupSignedDocument)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.radioYesSignedDocument.setFont(font)
        self.w.radioYesSignedDocument.setChecked(True)
        self.w.radioYesSignedDocument.setObjectName('radioYesSignedDocument')
        self.w.horizontalLayout_8.addWidget(self.w.radioYesSignedDocument)
        self.w.radioNoSignedDocument = QtWidgets.QRadioButton(self.w.groupSignedDocument)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.w.radioNoSignedDocument.setFont(font)
        self.w.radioNoSignedDocument.setObjectName('radioNoSignedDocument')
        self.w.horizontalLayout_8.addWidget(self.w.radioNoSignedDocument)
        self.w.verticalLayout_4.addWidget(self.w.groupSignedDocument)
        self.w.verticalLayout_3.addWidget(self.w.groupGeneral)
        self.w.horizontalLayout_4.addLayout(self.w.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(50, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_4.addItem(spacerItem2)
        self.w.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_5.setObjectName('verticalLayout_5')
        self.w.groupProducts = QtWidgets.QGroupBox(self.w.scrollAreaWidgetContents)
        self.w.groupProducts.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupProducts.setFont(font)
        self.w.groupProducts.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupProducts.setObjectName('groupProducts')
        self.w.verticalLayout_9 = QtWidgets.QVBoxLayout(self.w.groupProducts)
        self.w.verticalLayout_9.setSpacing(40)
        self.w.verticalLayout_9.setContentsMargins(40, 25, 40, 20)
        self.w.verticalLayout_9.setObjectName('verticalLayout_9')
        self.w.groupSolarComponents = QtWidgets.QGroupBox(self.w.groupProducts)
        self.w.groupSolarComponents.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupSolarComponents.setFont(font)
        self.w.groupSolarComponents.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupSolarComponents.setObjectName('groupSolarComponents')
        self.w.verticalLayout_6 = QtWidgets.QVBoxLayout(self.w.groupSolarComponents)
        self.w.verticalLayout_6.setSpacing(20)
        self.w.verticalLayout_6.setObjectName('verticalLayout_6')
        self.w.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_19.setSpacing(2)
        self.w.verticalLayout_19.setObjectName('verticalLayout_19')
        self.w.labelPanelTypes = QtWidgets.QLabel(self.w.groupSolarComponents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelPanelTypes.setFont(font)
        self.w.labelPanelTypes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelPanelTypes.setObjectName('labelPanelTypes')
        self.w.verticalLayout_19.addWidget(self.w.labelPanelTypes)
        self.w.buttonPanelTypes = CheckableMenuButton(self.w.groupSolarComponents)
        self.w.buttonPanelTypes.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonPanelTypes.setFont(font)
        self.w.buttonPanelTypes.setText('')
        self.w.buttonPanelTypes.setObjectName('buttonPanelTypes')
        self.w.verticalLayout_19.addWidget(self.w.buttonPanelTypes)
        self.w.verticalLayout_6.addLayout(self.w.verticalLayout_19)
        self.w.verticalLayout_21 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_21.setSpacing(2)
        self.w.verticalLayout_21.setObjectName('verticalLayout_21')
        self.w.labelInverterTypes = QtWidgets.QLabel(self.w.groupSolarComponents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelInverterTypes.setFont(font)
        self.w.labelInverterTypes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelInverterTypes.setObjectName('labelInverterTypes')
        self.w.verticalLayout_21.addWidget(self.w.labelInverterTypes)
        self.w.buttonInverterTypes = CheckableMenuButton(self.w.groupSolarComponents)
        self.w.buttonInverterTypes.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonInverterTypes.setFont(font)
        self.w.buttonInverterTypes.setText('')
        self.w.buttonInverterTypes.setObjectName('buttonInverterTypes')
        self.w.verticalLayout_21.addWidget(self.w.buttonInverterTypes)
        self.w.verticalLayout_6.addLayout(self.w.verticalLayout_21)
        self.w.verticalLayout_22 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_22.setSpacing(2)
        self.w.verticalLayout_22.setObjectName('verticalLayout_22')
        self.w.labelStructureTypes = QtWidgets.QLabel(self.w.groupSolarComponents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelStructureTypes.setFont(font)
        self.w.labelStructureTypes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelStructureTypes.setObjectName('labelStructureTypes')
        self.w.verticalLayout_22.addWidget(self.w.labelStructureTypes)
        self.w.buttonStructureTypes = CheckableMenuButton(self.w.groupSolarComponents)
        self.w.buttonStructureTypes.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonStructureTypes.setFont(font)
        self.w.buttonStructureTypes.setText('')
        self.w.buttonStructureTypes.setObjectName('buttonStructureTypes')
        self.w.verticalLayout_22.addWidget(self.w.buttonStructureTypes)
        self.w.verticalLayout_6.addLayout(self.w.verticalLayout_22)
        self.w.verticalLayout_29 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_29.setSpacing(2)
        self.w.verticalLayout_29.setObjectName('verticalLayout_29')
        self.w.labelBOSTypes = QtWidgets.QLabel(self.w.groupSolarComponents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelBOSTypes.setFont(font)
        self.w.labelBOSTypes.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelBOSTypes.setObjectName('labelBOSTypes')
        self.w.verticalLayout_29.addWidget(self.w.labelBOSTypes)
        self.w.buttonBOSTypes = CheckableMenuButton(self.w.groupSolarComponents)
        self.w.buttonBOSTypes.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonBOSTypes.setFont(font)
        self.w.buttonBOSTypes.setText('')
        self.w.buttonBOSTypes.setObjectName('buttonBOSTypes')
        self.w.verticalLayout_29.addWidget(self.w.buttonBOSTypes)
        self.w.verticalLayout_6.addLayout(self.w.verticalLayout_29)
        self.w.verticalLayout_9.addWidget(self.w.groupSolarComponents)
        self.w.groupSystemsApps = QtWidgets.QGroupBox(self.w.groupProducts)
        self.w.groupSystemsApps.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupSystemsApps.setFont(font)
        self.w.groupSystemsApps.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupSystemsApps.setObjectName('groupSystemsApps')
        self.w.verticalLayout_7 = QtWidgets.QVBoxLayout(self.w.groupSystemsApps)
        self.w.verticalLayout_7.setSpacing(20)
        self.w.verticalLayout_7.setObjectName('verticalLayout_7')
        self.w.verticalLayout_32 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_32.setSpacing(2)
        self.w.verticalLayout_32.setObjectName('verticalLayout_32')
        self.w.labelSolarSystems = QtWidgets.QLabel(self.w.groupSystemsApps)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelSolarSystems.setFont(font)
        self.w.labelSolarSystems.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelSolarSystems.setObjectName('labelSolarSystems')
        self.w.verticalLayout_32.addWidget(self.w.labelSolarSystems)
        self.w.buttonSolarSystems = CheckableMenuButton(self.w.groupSystemsApps)
        self.w.buttonSolarSystems.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonSolarSystems.setFont(font)
        self.w.buttonSolarSystems.setText('')
        self.w.buttonSolarSystems.setObjectName('buttonSolarSystems')
        self.w.verticalLayout_32.addWidget(self.w.buttonSolarSystems)
        self.w.verticalLayout_7.addLayout(self.w.verticalLayout_32)
        self.w.verticalLayout_9.addWidget(self.w.groupSystemsApps)
        self.w.verticalLayout_5.addWidget(self.w.groupProducts)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.w.verticalLayout_5.addItem(spacerItem3)
        self.w.horizontalLayout_4.addLayout(self.w.verticalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(29, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_4.addItem(spacerItem4)
        self.w.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_10.setObjectName('verticalLayout_10')
        self.w.groupServices = QtWidgets.QGroupBox(self.w.scrollAreaWidgetContents)
        self.w.groupServices.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupServices.setFont(font)
        self.w.groupServices.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupServices.setObjectName('groupServices')
        self.w.verticalLayout_37 = QtWidgets.QVBoxLayout(self.w.groupServices)
        self.w.verticalLayout_37.setSpacing(40)
        self.w.verticalLayout_37.setContentsMargins(40, 25, 40, 20)
        self.w.verticalLayout_37.setObjectName('verticalLayout_37')
        self.w.groupConsultingServices = QtWidgets.QGroupBox(self.w.groupServices)
        self.w.groupConsultingServices.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupConsultingServices.setFont(font)
        self.w.groupConsultingServices.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupConsultingServices.setObjectName('groupConsultingServices')
        self.w.verticalLayout_42 = QtWidgets.QVBoxLayout(self.w.groupConsultingServices)
        self.w.verticalLayout_42.setSpacing(20)
        self.w.verticalLayout_42.setObjectName('verticalLayout_42')
        self.w.verticalLayout_43 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_43.setSpacing(2)
        self.w.verticalLayout_43.setObjectName('verticalLayout_43')
        self.w.labelAssessmentServices = QtWidgets.QLabel(self.w.groupConsultingServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelAssessmentServices.setFont(font)
        self.w.labelAssessmentServices.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelAssessmentServices.setObjectName('labelAssessmentServices')
        self.w.verticalLayout_43.addWidget(self.w.labelAssessmentServices)
        self.w.buttonAssessmentServices = CheckableMenuButton(self.w.groupConsultingServices)
        self.w.buttonAssessmentServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonAssessmentServices.setFont(font)
        self.w.buttonAssessmentServices.setText('')
        self.w.buttonAssessmentServices.setObjectName('buttonAssessmentServices')
        self.w.verticalLayout_43.addWidget(self.w.buttonAssessmentServices)
        self.w.verticalLayout_42.addLayout(self.w.verticalLayout_43)
        self.w.verticalLayout_37.addWidget(self.w.groupConsultingServices)
        self.w.groupBuildingOperatingServices = QtWidgets.QGroupBox(self.w.groupServices)
        self.w.groupBuildingOperatingServices.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupBuildingOperatingServices.setFont(font)
        self.w.groupBuildingOperatingServices.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupBuildingOperatingServices.setObjectName('groupBuildingOperatingServices')
        self.w.verticalLayout_44 = QtWidgets.QVBoxLayout(self.w.groupBuildingOperatingServices)
        self.w.verticalLayout_44.setSpacing(20)
        self.w.verticalLayout_44.setObjectName('verticalLayout_44')
        self.w.verticalLayout_45 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_45.setSpacing(2)
        self.w.verticalLayout_45.setObjectName('verticalLayout_45')
        self.w.labelProjectDevServices = QtWidgets.QLabel(self.w.groupBuildingOperatingServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelProjectDevServices.setFont(font)
        self.w.labelProjectDevServices.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelProjectDevServices.setObjectName('labelProjectDevServices')
        self.w.verticalLayout_45.addWidget(self.w.labelProjectDevServices)
        self.w.buttonProjectDevServices = CheckableMenuButton(self.w.groupBuildingOperatingServices)
        self.w.buttonProjectDevServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonProjectDevServices.setFont(font)
        self.w.buttonProjectDevServices.setText('')
        self.w.buttonProjectDevServices.setObjectName('buttonProjectDevServices')
        self.w.verticalLayout_45.addWidget(self.w.buttonProjectDevServices)
        self.w.verticalLayout_44.addLayout(self.w.verticalLayout_45)
        self.w.verticalLayout_46 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_46.setSpacing(2)
        self.w.verticalLayout_46.setObjectName('verticalLayout_46')
        self.w.labelSystemDesignServices = QtWidgets.QLabel(self.w.groupBuildingOperatingServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelSystemDesignServices.setFont(font)
        self.w.labelSystemDesignServices.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelSystemDesignServices.setObjectName('labelSystemDesignServices')
        self.w.verticalLayout_46.addWidget(self.w.labelSystemDesignServices)
        self.w.buttonSystemDesignServices = CheckableMenuButton(self.w.groupBuildingOperatingServices)
        self.w.buttonSystemDesignServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonSystemDesignServices.setFont(font)
        self.w.buttonSystemDesignServices.setText('')
        self.w.buttonSystemDesignServices.setObjectName('buttonSystemDesignServices')
        self.w.verticalLayout_46.addWidget(self.w.buttonSystemDesignServices)
        self.w.verticalLayout_44.addLayout(self.w.verticalLayout_46)
        self.w.verticalLayout_47 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_47.setSpacing(2)
        self.w.verticalLayout_47.setObjectName('verticalLayout_47')
        self.w.labelInstallConstructServices = QtWidgets.QLabel(self.w.groupBuildingOperatingServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelInstallConstructServices.setFont(font)
        self.w.labelInstallConstructServices.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelInstallConstructServices.setObjectName('labelInstallConstructServices')
        self.w.verticalLayout_47.addWidget(self.w.labelInstallConstructServices)
        self.w.buttonInstallConstructServices = CheckableMenuButton(self.w.groupBuildingOperatingServices)
        self.w.buttonInstallConstructServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonInstallConstructServices.setFont(font)
        self.w.buttonInstallConstructServices.setText('')
        self.w.buttonInstallConstructServices.setObjectName('buttonInstallConstructServices')
        self.w.verticalLayout_47.addWidget(self.w.buttonInstallConstructServices)
        self.w.verticalLayout_44.addLayout(self.w.verticalLayout_47)
        self.w.verticalLayout_48 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_48.setSpacing(2)
        self.w.verticalLayout_48.setObjectName('verticalLayout_48')
        self.w.labelOperMainServices = QtWidgets.QLabel(self.w.groupBuildingOperatingServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelOperMainServices.setFont(font)
        self.w.labelOperMainServices.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelOperMainServices.setObjectName('labelOperMainServices')
        self.w.verticalLayout_48.addWidget(self.w.labelOperMainServices)
        self.w.buttonOperMainServices = CheckableMenuButton(self.w.groupBuildingOperatingServices)
        self.w.buttonOperMainServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonOperMainServices.setFont(font)
        self.w.buttonOperMainServices.setText('')
        self.w.buttonOperMainServices.setObjectName('buttonOperMainServices')
        self.w.verticalLayout_48.addWidget(self.w.buttonOperMainServices)
        self.w.verticalLayout_44.addLayout(self.w.verticalLayout_48)
        self.w.verticalLayout_37.addWidget(self.w.groupBuildingOperatingServices)
        self.w.groupAuxiliaryServices = QtWidgets.QGroupBox(self.w.groupServices)
        self.w.groupAuxiliaryServices.setMinimumSize(QtCore.QSize(250, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.w.groupAuxiliaryServices.setFont(font)
        self.w.groupAuxiliaryServices.setAlignment(QtCore.Qt.AlignCenter)
        self.w.groupAuxiliaryServices.setObjectName('groupAuxiliaryServices')
        self.w.verticalLayout_49 = QtWidgets.QVBoxLayout(self.w.groupAuxiliaryServices)
        self.w.verticalLayout_49.setSpacing(20)
        self.w.verticalLayout_49.setObjectName('verticalLayout_49')
        self.w.verticalLayout_50 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_50.setSpacing(2)
        self.w.verticalLayout_50.setObjectName('verticalLayout_50')
        self.w.labelInsuranceServices = QtWidgets.QLabel(self.w.groupAuxiliaryServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelInsuranceServices.setFont(font)
        self.w.labelInsuranceServices.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelInsuranceServices.setObjectName('labelInsuranceServices')
        self.w.verticalLayout_50.addWidget(self.w.labelInsuranceServices)
        self.w.buttonInsuranceServices = CheckableMenuButton(self.w.groupAuxiliaryServices)
        self.w.buttonInsuranceServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonInsuranceServices.setFont(font)
        self.w.buttonInsuranceServices.setText('')
        self.w.buttonInsuranceServices.setObjectName('buttonInsuranceServices')
        self.w.verticalLayout_50.addWidget(self.w.buttonInsuranceServices)
        self.w.verticalLayout_49.addLayout(self.w.verticalLayout_50)
        self.w.verticalLayout_51 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_51.setSpacing(2)
        self.w.verticalLayout_51.setObjectName('verticalLayout_51')
        self.w.labelFinancialServices = QtWidgets.QLabel(self.w.groupAuxiliaryServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelFinancialServices.setFont(font)
        self.w.labelFinancialServices.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelFinancialServices.setObjectName('labelFinancialServices')
        self.w.verticalLayout_51.addWidget(self.w.labelFinancialServices)
        self.w.buttonFinancialServices = CheckableMenuButton(self.w.groupAuxiliaryServices)
        self.w.buttonFinancialServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonFinancialServices.setFont(font)
        self.w.buttonFinancialServices.setText('')
        self.w.buttonFinancialServices.setObjectName('buttonFinancialServices')
        self.w.verticalLayout_51.addWidget(self.w.buttonFinancialServices)
        self.w.verticalLayout_49.addLayout(self.w.verticalLayout_51)
        self.w.verticalLayout_52 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_52.setSpacing(2)
        self.w.verticalLayout_52.setObjectName('verticalLayout_52')
        self.w.labelLogisticServices = QtWidgets.QLabel(self.w.groupAuxiliaryServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelLogisticServices.setFont(font)
        self.w.labelLogisticServices.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelLogisticServices.setObjectName('labelLogisticServices')
        self.w.verticalLayout_52.addWidget(self.w.labelLogisticServices)
        self.w.buttonLogisticServices = CheckableMenuButton(self.w.groupAuxiliaryServices)
        self.w.buttonLogisticServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonLogisticServices.setFont(font)
        self.w.buttonLogisticServices.setText('')
        self.w.buttonLogisticServices.setObjectName('buttonLogisticServices')
        self.w.verticalLayout_52.addWidget(self.w.buttonLogisticServices)
        self.w.verticalLayout_49.addLayout(self.w.verticalLayout_52)
        self.w.verticalLayout_53 = QtWidgets.QVBoxLayout()
        self.w.verticalLayout_53.setSpacing(2)
        self.w.verticalLayout_53.setObjectName('verticalLayout_53')
        self.w.labelExtraServices = QtWidgets.QLabel(self.w.groupAuxiliaryServices)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.w.labelExtraServices.setFont(font)
        self.w.labelExtraServices.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.w.labelExtraServices.setObjectName('labelExtraServices')
        self.w.verticalLayout_53.addWidget(self.w.labelExtraServices)
        self.w.buttonExtraServices = CheckableMenuButton(self.w.groupAuxiliaryServices)
        self.w.buttonExtraServices.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.w.buttonExtraServices.setFont(font)
        self.w.buttonExtraServices.setText('')
        self.w.buttonExtraServices.setObjectName('buttonExtraServices')
        self.w.verticalLayout_53.addWidget(self.w.buttonExtraServices)
        self.w.verticalLayout_49.addLayout(self.w.verticalLayout_53)
        self.w.verticalLayout_37.addWidget(self.w.groupAuxiliaryServices)
        self.w.verticalLayout_10.addWidget(self.w.groupServices)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.w.verticalLayout_10.addItem(spacerItem5)
        self.w.horizontalLayout_4.addLayout(self.w.verticalLayout_10)
        spacerItem6 = QtWidgets.QSpacerItem(29, 50, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_4.addItem(spacerItem6)
        self.w.verticalLayout.addLayout(self.w.horizontalLayout_4)
        self.w.groupStaff = StaffGroup(self.w.scrollAreaWidgetContents, self.my_strings)
        self.w.verticalLayout.addWidget(self.w.groupStaff)
        self.w.scrollArea.setWidget(self.w.scrollAreaWidgetContents)
        self.w.verticalLayout_2.addWidget(self.w.scrollArea)
        self.w.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.w.horizontalLayout_13.setSpacing(30)
        self.w.horizontalLayout_13.setObjectName('horizontalLayout_13')
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_13.addItem(spacerItem7)
        self.w.buttonNew = QtWidgets.QToolButton(self.w.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w.buttonNew.sizePolicy().hasHeightForWidth())
        self.w.buttonNew.setSizePolicy(sizePolicy)
        self.w.buttonNew.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.w.buttonNew.setFont(font)
        self.w.buttonNew.setIconSize(QtCore.QSize(40, 40))
        self.w.buttonNew.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.w.buttonNew.setObjectName('buttonNew')
        self.w.horizontalLayout_13.addWidget(self.w.buttonNew)
        self.w.buttonOverwrite = QtWidgets.QToolButton(self.w.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w.buttonOverwrite.sizePolicy().hasHeightForWidth())
        self.w.buttonOverwrite.setSizePolicy(sizePolicy)
        self.w.buttonOverwrite.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.w.buttonOverwrite.setFont(font)
        self.w.buttonOverwrite.setIconSize(QtCore.QSize(40, 40))
        self.w.buttonOverwrite.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.w.buttonOverwrite.setObjectName('buttonOverwrite')
        self.w.horizontalLayout_13.addWidget(self.w.buttonOverwrite)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.w.horizontalLayout_13.addItem(spacerItem8)
        self.w.verticalLayout_2.addLayout(self.w.horizontalLayout_13)
        spacerItem9 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.w.verticalLayout_2.addItem(spacerItem9)
        self.w.setCentralWidget(self.w.centralWidget)

        self.w.labelTitle.setText(self.my_strings.label_company)
        self.w.labelName.setText(f"{color_gray(self.my_strings.label_name)} {color_red('*')}")
        self.w.labelCompanyType.setText(color_gray(self.my_strings.label_type))
        self.w.labelComments.setText(color_gray(self.my_strings.label_comments))
        self.w.labelSource.setText(color_gray(self.my_strings.label_source))
        self.w.labelUser.setText(color_gray(self.my_strings.label_loader))
        self.w.labelDateLoading.setText(color_gray(self.my_strings.label_date_loading))
        self.w.labelCountry.setText(color_gray(self.my_strings.label_country))
        self.w.labelProvince.setText(color_gray(self.my_strings.label_province))
        self.w.labelGeoZone.setText(color_gray(self.my_strings.label_geo_zone))
        self.w.labelAddress.setText(color_gray(self.my_strings.label_address))
        self.w.labelEmail.setText(color_gray(self.my_strings.label_email))
        self.w.labelPhone.setText(color_gray(self.my_strings.label_phone))
        self.w.labelWeb.setText(color_gray(self.my_strings.label_web))
        self.w.labelIDDocument.setText(color_gray(self.my_strings.label_id_document))
        self.w.labelDateVerification.setText(color_gray(self.my_strings.label_date_verification))
        self.w.labelVerificationUser.setText(color_gray(self.my_strings.label_verification_user))
        self.w.labelTier.setText(color_gray(self.my_strings.label_tier))
        self.w.labelFormationYear.setText(color_gray(self.my_strings.label_formation_year))
        self.w.labelAnnualCapacity.setText(color_gray(self.my_strings.label_annual_capacity))
        self.w.labelScopeRange.setText(color_gray(self.my_strings.label_scope_range))
        self.w.labelReplyRatio.setText(color_gray(self.my_strings.label_reply_ratio))
        self.w.labelNContacts.setText(color_gray(self.my_strings.label_n_contacts))
        self.w.labelNReplies.setText(color_gray(self.my_strings.label_n_replies))
        self.w.labelSolarSystems.setText(color_gray(self.my_strings.label_solar_systems))
        self.w.labelPanelTypes.setText(color_gray(self.my_strings.label_panel_types))
        self.w.labelInverterTypes.setText(color_gray(self.my_strings.label_inverter_types))
        self.w.labelStructureTypes.setText(color_gray(self.my_strings.label_structure_types))
        self.w.labelBOSTypes.setText(color_gray(self.my_strings.label_bos_types))
        self.w.labelAssessmentServices.setText(color_gray(self.my_strings.label_assessment_services))
        self.w.labelProjectDevServices.setText(color_gray(self.my_strings.label_project_dev_services))
        self.w.labelSystemDesignServices.setText(color_gray(self.my_strings.label_system_design_services))
        self.w.labelInstallConstructServices.setText(color_gray(self.my_strings.label_install_construct_services))
        self.w.labelOperMainServices.setText(color_gray(self.my_strings.label_oper_main_services))
        self.w.labelInsuranceServices.setText(color_gray(self.my_strings.label_insurance_services))
        self.w.labelFinancialServices.setText(color_gray(self.my_strings.label_financial_services))
        self.w.labelLogisticServices.setText(color_gray(self.my_strings.label_logistic_services))
        self.w.labelExtraServices.setText(color_gray(self.my_strings.label_extra_services))

        self.w.buttonBack.setIcon(QtGui.QIcon(url_back))
        self.w.buttonBack.setIconSize(QtCore.QSize(32, 32))
        self.w.buttonNew.setIcon(QtGui.QIcon(url_save))
        self.w.buttonNew.setIconSize(QtCore.QSize(40, 40))
        self.w.buttonNew.setText(self.my_strings.button_new)
        self.w.buttonOverwrite.setIcon(QtGui.QIcon(url_save))
        self.w.buttonOverwrite.setIconSize(QtCore.QSize(40, 40))
        self.w.buttonOverwrite.setText(self.my_strings.button_overwrite)
        self.w.buttonOverwrite.setVisible(False)

        self.w.radioYesSolarnubVerification.setText(self.my_strings.radio_yes)
        self.w.radioNoSolarnubVerification.setText(self.my_strings.radio_no)
        self.w.radioYesRelWithThisCompany.setText(self.my_strings.radio_yes)
        self.w.radioNoRelWithThisCompany.setText(self.my_strings.radio_no)
        self.w.radioYesSignedDocument.setText(self.my_strings.radio_yes)
        self.w.radioNoSignedDocument.setText(self.my_strings.radio_no)

        self.w.spinAnnualCapacity.setSuffix(' MW')
        self.w.spinReplyRatio.setSuffix(' %')

        self.w.comboUser.currentTextChanged.connect(lambda: self.w.comboUser.validate_soft())
        self.w.comboCountry.currentTextChanged.connect(lambda: self.w.comboCountry.validate_soft())
        self.w.comboProvince.currentTextChanged.connect(lambda: self.w.comboProvince.validate_soft())
        self.w.comboGeoZone.currentTextChanged.connect(lambda: self.w.comboGeoZone.validate_soft())
        self.w.comboVerificationUser.currentTextChanged.connect(lambda: self.w.comboVerificationUser.validate_soft())
        self.w.comboTier.currentTextChanged.connect(lambda: self.w.comboTier.validate_soft())
        self.w.comboScopeRange.currentTextChanged.connect(lambda: self.w.comboScopeRange.validate_soft())

        self.w.groupGeneral.setTitle(self.my_strings.group_general)
        self.w.groupSolarnubVerification.setTitle(self.my_strings.group_sn_verification)
        self.w.groupSolarnubVerification.setStyleSheet('QGroupBox:title {color: #555555}')
        self.w.groupRelWithThisCompany.setTitle(self.my_strings.group_rel_with_this_company)
        self.w.groupRelWithThisCompany.setStyleSheet('QGroupBox:title {color: #555555}')
        self.w.groupSignedDocument.setTitle(self.my_strings.group_signed_document)
        self.w.groupSignedDocument.setStyleSheet('QGroupBox:title {color: #555555}')
        self.w.groupProducts.setTitle(self.my_strings.group_products)
        self.w.groupSystemsApps.setTitle(self.my_strings.group_systems_apps)
        self.w.groupSolarComponents.setTitle(self.my_strings.group_solar_components)
        self.w.groupServices.setTitle(self.my_strings.group_services)
        self.w.groupConsultingServices.setTitle(self.my_strings.group_consulting_services)
        self.w.groupBuildingOperatingServices.setTitle(self.my_strings.group_building_operating_services)
        self.w.groupAuxiliaryServices.setTitle(self.my_strings.group_auxiliary_services)
        self.w.groupStaff.setTitle(self.my_strings.group_staff)

    def connect_signals(self, controller):
        super().connect_signals(controller)
        self.w.lineName.textChanged.connect(self.validate_name)

        self.w.groupStaff.connect_signals(controller)

    @property
    def address(self):
        return self.w.lineAddress.text()

    @address.setter
    def address(self, text):
        self.w.lineAddress.setText(text)

    @property
    def annual_capacity(self):
        return self.w.spinAnnualCapacity.value()

    @annual_capacity.setter
    def annual_capacity(self, number):
        self.w.spinAnnualCapacity.setValue(number)

    @property
    def assessment_services(self):
        return self.w.buttonAssessmentServices.checked_items

    @assessment_services.setter
    def assessment_services(self, items):
        self.w.buttonAssessmentServices.checked_items = items

    @property
    def bos_types(self):
        return self.w.buttonBOSTypes.checked_items

    @bos_types.setter
    def bos_types(self, items):
        self.w.buttonBOSTypes.checked_items = items

    @property
    def comments(self):
        return self.w.textComments.toPlainText()

    @comments.setter
    def comments(self, text):
        self.w.textComments.setText(text)

    @property
    def country(self):
        return self.w.comboCountry.currentText()

    @country.setter
    def country(self, text):
        self.w.comboCountry.setCurrentText(text)

    @property
    def data(self):
        Data = namedtuple('Data',
                          ('name', 'types', 'comments', 'source', 'user', 'date_loading', 'country', 'province',
                           'geo_zone', 'address', 'email', 'phone', 'web', 'id_document', 'solarnub_verification',
                           'date_verification', 'verification_user', 'tier', 'formation_year', 'rel_with_this_company',
                           'annual_capacity', 'scope_range', 'reply_ratio', 'n_contacts', 'n_replies',
                           'signed_document', 'panel_types', 'inverter_types', 'structure_types', 'bos_types',
                           'solar_systems', 'assessment_services', 'project_dev_services', 'system_design_services',
                           'install_construct_services', 'oper_main_services', 'insurance_services',
                           'financial_services', 'logistic_services', 'extra_services', 'staff')
                          )
        return Data(
            self.name,
            self.types,
            self.comments,
            self.source,
            self.user,
            self.date_loading,
            self.country,
            self.province,
            self.geo_zone,
            self.address,
            self.email,
            self.phone,
            self.web,
            self.id_document,
            self.sn_verification,
            self.date_verification,
            self.verification_user,
            self.tier,
            self.formation_year,
            self.rel_with_this_company,
            self.annual_capacity,
            self.scope_range,
            self.reply_ratio,
            self.n_contacts,
            self.n_replies,
            self.signed_document,

            self.panel_types,
            self.inverter_types,
            self.structure_types,
            self.bos_types,
            self.solar_systems,

            self.assessment_services,
            self.project_dev_services,
            self.system_design_services,
            self.install_construct_services,
            self.oper_main_services,
            self.insurance_services,
            self.financial_services,
            self.logistic_services,
            self.extra_services,

            self.group_staff.table.data
        )

    @property
    def date_loading(self):
        return self.w.dateLoading.date().toPython()

    @date_loading.setter
    def date_loading(self, date):
        self.w.dateLoading.setDate(date)

    @property
    def date_verification(self):
        return self.w.dateVerification.date().toPython()

    @date_verification.setter
    def date_verification(self, date):
        self.w.dateVerification.setDate(date)

    @property
    def email(self):
        return self.w.lineEmail.text()

    @email.setter
    def email(self, text):
        self.w.lineEmail.setText(text)

    @property
    def extra_services(self):
        return self.w.buttonExtraServices.checked_items

    @extra_services.setter
    def extra_services(self, items):
        self.w.buttonExtraServices.checked_items = items

    @property
    def financial_services(self):
        return self.w.buttonFinancialServices.checked_items

    @financial_services.setter
    def financial_services(self, items):
        self.w.buttonFinancialServices.checked_items = items

    @property
    def formation_year(self):
        return self.w.spinFormationYear.value()

    @formation_year.setter
    def formation_year(self, number):
        self.w.spinFormationYear.setValue(number)

    @property
    def geo_zone(self):
        return self.w.comboGeoZone.currentText()

    @geo_zone.setter
    def geo_zone(self, text):
        self.w.comboGeoZone.setCurrentText(text)

    @property
    def group_staff(self):
        return self.w.groupStaff

    @property
    def id_document(self):
        return self.w.lineIDDocument.text()

    @id_document.setter
    def id_document(self, text):
        self.w.lineIDDocument.setText(text)

    @property
    def install_construct_services(self):
        return self.w.buttonInstallConstructServices.checked_items

    @install_construct_services.setter
    def install_construct_services(self, items):
        self.w.buttonInstallConstructServices.checked_items = items

    @property
    def insurance_services(self):
        return self.w.buttonInsuranceServices.checked_items

    @insurance_services.setter
    def insurance_services(self, items):
        self.w.buttonInsuranceServices.checked_items = items

    @property
    def inverter_types(self):
        return self.w.buttonInverterTypes.checked_items

    @inverter_types.setter
    def inverter_types(self, items):
        self.w.buttonInverterTypes.checked_items = items

    @property
    def logistic_services(self):
        return self.w.buttonLogisticServices.checked_items

    @logistic_services.setter
    def logistic_services(self, items):
        self.w.buttonLogisticServices.checked_items = items

    @property
    def n_contacts(self):
        return self.w.spinNContacts.value()

    @n_contacts.setter
    def n_contacts(self, number):
        self.w.spinNContacts.setValue(number)

    @property
    def n_replies(self):
        return self.w.spinNReplies.value()

    @n_replies.setter
    def n_replies(self, number):
        self.w.spinNReplies.setValue(number)

    @property
    def name(self):
        return self.w.lineName.text()

    @name.setter
    def name(self, text):
        self.w.lineName.setText(text)

    @property
    def oper_main_services(self):
        return self.w.buttonOperMainServices.checked_items

    @oper_main_services.setter
    def oper_main_services(self, items):
        self.w.buttonOperMainServices.checked_items = items

    @property
    def panel_types(self):
        return self.w.buttonPanelTypes.checked_items

    @panel_types.setter
    def panel_types(self, items):
        self.w.buttonPanelTypes.checked_items = items

    @property
    def phone(self):
        return self.w.linePhone.text()

    @phone.setter
    def phone(self, text):
        self.w.linePhone.setText(text)

    @property
    def project_dev_services(self):
        return self.w.buttonProjectDevServices.checked_items

    @project_dev_services.setter
    def project_dev_services(self, items):
        self.w.buttonProjectDevServices.checked_items = items

    @property
    def province(self):
        return self.w.comboProvince.currentText()

    @province.setter
    def province(self, text):
        self.w.comboProvince.setCurrentText(text)

    @property
    def rel_with_this_company(self):
        return self.w.radioYesRelWithThisCompany.isChecked()

    @rel_with_this_company.setter
    def rel_with_this_company(self, yes):
        if yes:
            self.w.radioYesRelWithThisCompany.setChecked(True)
        else:
            self.w.radioNoRelWithThisCompany.setChecked(True)

    @property
    def reply_ratio(self):
        return self.w.spinReplyRatio.value()

    @reply_ratio.setter
    def reply_ratio(self, number):
        self.w.spinReplyRatio.setValue(number)

    @property
    def scope_range(self):
        return self.w.comboScopeRange.currentText()

    @scope_range.setter
    def scope_range(self, text):
        self.w.comboScopeRange.setCurrentText(text)

    @property
    def signed_document(self):
        return self.w.radioYesSignedDocument.isChecked()

    @signed_document.setter
    def signed_document(self, yes):
        if yes:
            self.w.radioYesSignedDocument.setChecked(True)
        else:
            self.w.radioNoSignedDocument.setChecked(True)

    @property
    def solar_systems(self):
        return self.w.buttonSolarSystems.checked_items

    @solar_systems.setter
    def solar_systems(self, items):
        self.w.buttonSolarSystems.checked_items = items

    @property
    def sn_verification(self):
        return self.w.radioYesSolarnubVerification.isChecked()

    @sn_verification.setter
    def sn_verification(self, yes):
        if yes:
            self.w.radioYesSolarnubVerification.setChecked(True)
        else:
            self.w.radioNoSolarnubVerification.setChecked(True)

    @property
    def source(self):
        return self.w.lineSource.text()

    @source.setter
    def source(self, text):
        self.w.lineSource.setText(text)

    @property
    def structure_types(self):
        return self.w.buttonStructureTypes.checked_items

    @structure_types.setter
    def structure_types(self, items):
        self.w.buttonStructureTypes.checked_items = items

    @property
    def system_design_services(self):
        return self.w.buttonSystemDesignServices.checked_items

    @system_design_services.setter
    def system_design_services(self, items):
        self.w.buttonSystemDesignServices.checked_items = items

    @property
    def tier(self):
        return self.w.comboTier.currentText()

    @tier.setter
    def tier(self, text):
        self.w.comboTier.setCurrentText(text)

    @property
    def types(self):
        return self.w.buttonCompanyType.checked_items

    @types.setter
    def types(self, items):
        self.w.buttonCompanyType.checked_items = items

    @property
    def user(self):
        return self.w.comboUser.currentText()

    @user.setter
    def user(self, text):
        self.w.comboUser.setCurrentText(text)

    @property
    def verification_user(self):
        return self.w.comboVerificationUser.currentText()

    @verification_user.setter
    def verification_user(self, text):
        self.w.comboVerificationUser.setCurrentText(text)

    @property
    def web(self):
        return self.w.lineWeb.text()

    @web.setter
    def web(self, text):
        self.w.lineWeb.setText(text)

    def load_initial_data(self, items, last_user, loading_date, default):
        self.w.buttonCompanyType.items = items[0]
        self.w.comboUser.items = items[1]
        self.w.comboCountry.items = items[2]
        self.w.comboProvince.items = items[2]
        self.w.comboGeoZone.items = items[3]
        self.w.comboVerificationUser.items = items[1]
        self.w.comboTier.items = items[4]
        self.w.comboScopeRange.items = items[5]

        self.w.buttonSolarSystems.items = items[6]
        self.w.buttonPanelTypes.items = items[7]
        self.w.buttonInverterTypes.items = items[8]
        self.w.buttonStructureTypes.items = items[9]
        self.w.buttonBOSTypes.items = items[10]

        self.w.buttonAssessmentServices.items = items[11]
        self.w.buttonProjectDevServices.items = items[12]
        self.w.buttonSystemDesignServices.items = items[13]
        self.w.buttonInstallConstructServices.items = items[14]
        self.w.buttonOperMainServices.items = items[15]
        self.w.buttonInsuranceServices.items = items[16]
        self.w.buttonFinancialServices.items = items[17]
        self.w.buttonLogisticServices.items = items[18]
        self.w.buttonExtraServices.items = items[19]

        if default:
            self.user = last_user
            self.date_loading = loading_date
            self.sn_verification = False
            self.rel_with_this_company = False
            self.signed_document = False

            self.validate_name()
        else:
            self.w.comboUser.validate_soft()
            self.w.comboCountry.validate_soft()
            self.w.comboProvince.validate_soft()
            self.w.comboGeoZone.validate_soft()
            self.w.comboVerificationUser.validate_soft()
            self.w.comboTier.validate_soft()
            self.w.comboScopeRange.validate_soft()

    def load_item_data(self, company):
        self.name = company.name
        self.types = company.types
        self.comments = company.comments
        self.source = company.source
        self.user = company.user
        self.date_loading = company.loading_date
        self.country = company.country
        self.province = company.province
        self.geo_zone = company.geo_zone
        self.address = company.address
        self.email = company.email
        self.phone = company.phone
        self.web = company.web
        self.id_document = company.id_document
        self.sn_verification = company.sn_verification
        self.date_verification = company.verification_date
        self.verification_user = company.verification_user
        self.tier = company.tier
        self.formation_year = company.formation_year
        self.rel_with_this_company = company.rel_with_this_company
        self.annual_capacity = company.annual_capacity
        self.scope_range = company.scope_range
        self.reply_ratio = company.reply_ratio
        self.n_contacts = company.n_contacts
        self.n_replies = company.n_replies
        self.signed_document = company.signed_document

        self.panel_types = company.panel_types
        self.inverter_types = company.inverter_types
        self.structure_types = company.structure_types
        self.bos_types = company.bos_types
        self.solar_systems = company.solar_systems

        self.assessment_services = company.assessment_services
        self.project_dev_services = company.project_dev_services
        self.system_design_services = company.system_design_services
        self.install_construct_services = company.install_construct_services
        self.oper_main_services = company.oper_main_services
        self.insurance_services = company.insurance_services
        self.financial_services = company.financial_services
        self.logistic_services = company.logistic_services
        self.extra_services = company.extra_services

        self.load_staff(company.staff)

    def load_staff(self, staff):
        self.w.groupStaff.load_items(staff)

    def validate_name(self):
        if not self.name:
            if self.valid_name:
                color_red_line(self.w.lineName)
                self.valid_name = False
        elif not self.valid_name:
            color_default_line(self.w.lineName)
            self.valid_name = True
