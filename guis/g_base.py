from abc import ABC, abstractmethod

from resources import MyStrings


class GBase(ABC):
    @abstractmethod
    def __init__(self, window):
        self.w = window
        self.my_strings = MyStrings()

    @abstractmethod
    def connect_signals(self, controller):
        self.w.buttonBack.clicked.connect(controller.clicked_back)
        self.w.buttonNew.clicked.connect(lambda: controller.clicked_save(overwrite=False))
        self.w.buttonOverwrite.clicked.connect(lambda: controller.clicked_save(overwrite=True))

    def show_button_overwrite(self):
        self.w.buttonOverwrite.setVisible(True)

    def set_focus_nothing(self):
        self.w.setFocus()
