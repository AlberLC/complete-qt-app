from resources import get_language_code, set_language_code


class CMenu:
    def __init__(self, c_master, gui):
        self.c_master = c_master
        self.gui = gui
        self.session = self.c_master.Session()

    def clicked_button_language(self, lang_code):
        if lang_code != get_language_code():
            set_language_code(lang_code)
            self.c_master.refresh_menu()
