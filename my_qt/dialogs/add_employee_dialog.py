from PySide2 import QtCore, QtGui, QtWidgets

from my_qt.combo_boxes import SearchCombo
from resources import MyStrings, url_icon
from utilities.various import color_gray, color_red, color_default_line, color_red_line


class AddEmployeeDialog(QtWidgets.QDialog):
    def __init__(self, languages, company_name=None):
        super().__init__()
        self.my_strings = MyStrings()
        self.valid_name = True

        self.setWindowTitle(self.my_strings.title_employee(company_name))
        self.icono = QtGui.QIcon(url_icon)
        self.setWindowIcon(self.icono)
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        self.setFixedWidth(322)

        self.setup_gui()
        self.comboLanguage.items = languages
        self.validate_name()

    def sizeHint(self):
        return QtCore.QSize(322, 500)

    # Edited: SearchCombo
    def setup_gui(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setSpacing(30)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 15)
        self.verticalLayout.setObjectName('verticalLayout')
        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName('scrollArea')
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -20, 283, 619))
        self.scrollAreaWidgetContents.setObjectName('scrollAreaWidgetContents')
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName('verticalLayout_3')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setObjectName('verticalLayout_2')
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName('verticalLayout_12')
        self.labelName = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.labelName.setFont(font)
        self.labelName.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelName.setObjectName('labelName')
        self.verticalLayout_12.addWidget(self.labelName)
        self.lineName = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineName.setMinimumSize(QtCore.QSize(0, 30))
        self.lineName.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.lineName.setFont(font)
        self.lineName.setObjectName('lineName')
        self.verticalLayout_12.addWidget(self.lineName)
        self.verticalLayout_2.addLayout(self.verticalLayout_12)
        self.verticalLayout_17 = QtWidgets.QVBoxLayout()
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName('verticalLayout_17')
        self.labelPosition = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.labelPosition.setFont(font)
        self.labelPosition.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelPosition.setObjectName('labelPosition')
        self.verticalLayout_17.addWidget(self.labelPosition)
        self.linePosition = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.linePosition.setMinimumSize(QtCore.QSize(0, 30))
        self.linePosition.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.linePosition.setFont(font)
        self.linePosition.setObjectName('linePosition')
        self.verticalLayout_17.addWidget(self.linePosition)
        self.verticalLayout_2.addLayout(self.verticalLayout_17)
        self.verticalLayout_18 = QtWidgets.QVBoxLayout()
        self.verticalLayout_18.setSpacing(2)
        self.verticalLayout_18.setObjectName('verticalLayout_18')
        self.labelProjectType = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.labelProjectType.setFont(font)
        self.labelProjectType.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelProjectType.setObjectName('labelProjectType')
        self.verticalLayout_18.addWidget(self.labelProjectType)
        self.lineProjectType = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineProjectType.setMinimumSize(QtCore.QSize(0, 30))
        self.lineProjectType.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.lineProjectType.setFont(font)
        self.lineProjectType.setObjectName('lineProjectType')
        self.verticalLayout_18.addWidget(self.lineProjectType)
        self.verticalLayout_2.addLayout(self.verticalLayout_18)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setSpacing(2)
        self.verticalLayout_13.setObjectName('verticalLayout_13')
        self.labelEmail = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.labelEmail.setFont(font)
        self.labelEmail.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelEmail.setObjectName('labelEmail')
        self.verticalLayout_13.addWidget(self.labelEmail)
        self.lineEmail = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEmail.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEmail.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.lineEmail.setFont(font)
        self.lineEmail.setObjectName('lineEmail')
        self.verticalLayout_13.addWidget(self.lineEmail)
        self.verticalLayout_2.addLayout(self.verticalLayout_13)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setSpacing(2)
        self.verticalLayout_15.setObjectName('verticalLayout_15')
        self.labelPhone = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.labelPhone.setFont(font)
        self.labelPhone.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelPhone.setObjectName('labelPhone')
        self.verticalLayout_15.addWidget(self.labelPhone)
        self.linePhone = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.linePhone.setMinimumSize(QtCore.QSize(0, 30))
        self.linePhone.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.linePhone.setFont(font)
        self.linePhone.setText('')
        self.linePhone.setObjectName('linePhone')
        self.verticalLayout_15.addWidget(self.linePhone)
        self.verticalLayout_2.addLayout(self.verticalLayout_15)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setSpacing(2)
        self.verticalLayout_16.setObjectName('verticalLayout_16')
        self.labelLinkedin = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.labelLinkedin.setFont(font)
        self.labelLinkedin.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelLinkedin.setObjectName('labelLinkedin')
        self.verticalLayout_16.addWidget(self.labelLinkedin)
        self.lineLinkedin = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineLinkedin.setMinimumSize(QtCore.QSize(0, 30))
        self.lineLinkedin.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.lineLinkedin.setFont(font)
        self.lineLinkedin.setObjectName('lineLinkedin')
        self.verticalLayout_16.addWidget(self.lineLinkedin)
        self.verticalLayout_2.addLayout(self.verticalLayout_16)
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setSpacing(2)
        self.verticalLayout_19.setObjectName('verticalLayout_19')
        self.labelObservations = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.labelObservations.setFont(font)
        self.labelObservations.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelObservations.setObjectName('labelObservations')
        self.verticalLayout_19.addWidget(self.labelObservations)
        self.textObservations = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.textObservations.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textObservations.setFont(font)
        self.textObservations.setObjectName('textObservations')
        self.verticalLayout_19.addWidget(self.textObservations)
        self.verticalLayout_2.addLayout(self.verticalLayout_19)
        self.verticalLayout_33 = QtWidgets.QVBoxLayout()
        self.verticalLayout_33.setSpacing(2)
        self.verticalLayout_33.setObjectName('verticalLayout_33')
        self.labelLanguage = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(50)
        font.setBold(False)
        self.labelLanguage.setFont(font)
        self.labelLanguage.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.labelLanguage.setObjectName('labelLanguage')
        self.verticalLayout_33.addWidget(self.labelLanguage)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName('horizontalLayout_2')
        self.comboLanguage = SearchCombo(self.scrollAreaWidgetContents)
        self.comboLanguage.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.comboLanguage.setFont(font)
        self.comboLanguage.setObjectName('comboLanguage')
        self.horizontalLayout_2.addWidget(self.comboLanguage)
        spacerItem = QtWidgets.QSpacerItem(220, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_33.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout_33)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName('horizontalLayout')
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonAccept = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.buttonAccept.setFont(font)
        self.buttonAccept.setObjectName('buttonAccept')
        self.horizontalLayout.addWidget(self.buttonAccept)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.labelName.setText(f"{color_gray(self.my_strings.label_name)} {color_red('*')}")
        self.labelPosition.setText(color_gray(self.my_strings.label_position))
        self.labelProjectType.setText(color_gray(self.my_strings.label_projects_type))
        self.labelEmail.setText(color_gray(self.my_strings.label_email))
        self.labelPhone.setText(color_gray(self.my_strings.label_phone))
        self.labelLinkedin.setText(color_gray(self.my_strings.label_linkedin))
        self.labelLanguage.setText(color_gray(self.my_strings.label_language))
        self.labelObservations.setText(color_gray(self.my_strings.label_observations))

        self.buttonAccept.setText(self.my_strings.button_accept)

    def connect_signals(self, controller):
        self.buttonAccept.clicked.connect(controller.clicked_save_employee)

        self.lineName.textChanged.connect(self.validate_name)

        self.comboLanguage.currentTextChanged.connect(self.comboLanguage.validate_soft)

    @property
    def email(self):
        return self.lineEmail.text()

    @email.setter
    def email(self, text):
        self.lineEmail.setText(text)

    @property
    def name(self):
        return self.lineName.text()

    @name.setter
    def name(self, text):
        self.lineName.setText(text)

    @property
    def observations(self):
        return self.textObservations.toPlainText()

    @observations.setter
    def observations(self, text):
        self.textObservations.setText(text)

    @property
    def phone(self):
        return self.linePhone.text()

    @phone.setter
    def phone(self, text):
        self.linePhone.setText(text)

    @property
    def position(self):
        return self.linePosition.text()

    @position.setter
    def position(self, text):
        self.linePosition.setText(text)

    @property
    def projects_type(self):
        return self.lineProjectType.text()

    @projects_type.setter
    def projects_type(self, text):
        self.lineProjectType.setText(text)

    @property
    def language(self):
        return self.comboLanguage.currentText()

    @language.setter
    def language(self, text):
        self.comboLanguage.setCurrentText(text)

    @property
    def linkedin(self):
        return self.lineLinkedin.text()

    @linkedin.setter
    def linkedin(self, text):
        self.lineLinkedin.setText(text)

    def load_item_data(self, employee):
        self.name = employee.name
        self.position = employee.position
        self.projects_type = employee.projects_type
        self.email = employee.email
        self.phone = employee.phone
        self.linkedin = employee.linkedin
        self.language = employee.language
        self.observations = employee.observations

        self.validate_name()

    def validate_name(self):
        if not self.name:
            if self.valid_name:
                color_red_line(self.lineName)
                self.valid_name = False
        elif not self.valid_name:
            color_default_line(self.lineName)
            self.valid_name = True
