import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from controllers.c_company import CCompany
from controllers.c_database import CDatabase
from controllers.c_menu import CMenu
from controllers.c_panel_need import CPanelNeed
from controllers.c_panel_quotation import CPanelQuotation
from controllers.c_searcher import CSearcher
from guis.g_company import GCompany
from guis.g_database import GDatabase
from guis.g_menu import GMenu
from guis.g_panel_need import GPanelNeed
from guis.g_panel_quotation import GPanelQuotation
from guis.g_searcher import GNeeds, GQuotations
from my_qt.windows.main_windows import Window


class CMaster:
    def __init__(self):
        self.engine = create_engine(os.getenv('DB_URL'))
        self.Session = sessionmaker(bind=self.engine)
        self.controller = None
        self.window = Window()
        self.windows_queue = []
        self.previous_data = None

        self.window.add_controller(self)
        self.setup_menu()

    # -------------------- TRANSITIONS --------------------
    # ---------- Level 1 ----------
    def setup_menu(self):
        self.close_bd_session()
        self.windows_queue.append((self.setup_menu, []))
        gui = GMenu(self.window)
        self.controller = CMenu(self, gui)
        gui.connect_signals(self.controller)

    def refresh_menu(self):
        del self.windows_queue[-1]
        self.setup_menu()

    # ---------- Level 2 ----------
    def setup_database(self, previous_data=None):
        self.close_bd_session()
        self.windows_queue.append((self.setup_database, []))
        gui = GDatabase(self.window)
        self.controller = CDatabase(self, gui, previous_data)
        gui.connect_signals(self.controller)

    def setup_needs(self):
        self.close_bd_session()
        self.windows_queue.append((self.setup_needs, []))
        gui = GNeeds(self.window)
        self.controller = CSearcher(self, gui, 'needs')
        gui.connect_signals(self.controller)

    def setup_quotations(self):
        self.close_bd_session()
        self.windows_queue.append((self.setup_quotations, []))
        gui = GQuotations(self.window)
        self.controller = CSearcher(self, gui, 'quotations')
        gui.connect_signals(self.controller)

    # ---------- Level 3 ----------
    def setup_battery_need(self, panel_need_id=None, previous_data=None):
        pass

    def setup_bos_need(self, panel_need_id=None, previous_data=None):
        pass

    def setup_company(self, company_id=None):
        self.close_bd_session()
        self.windows_queue.append((self.setup_company, [company_id]))
        gui = GCompany(self.window)
        self.controller = CCompany(self, gui, company_id)
        gui.connect_signals(self.controller)
        self.controller.initialize_gui()
        if company_id:
            gui.show_button_overwrite()

    def setup_inverter_need(self, panel_need_id=None, previous_data=None):
        pass

    def setup_panel_need(self, panel_need_id=None, previous_data=None):
        self.close_bd_session()
        self.windows_queue.append((self.setup_panel_need, [panel_need_id]))
        gui = GPanelNeed(self.window)
        self.controller = CPanelNeed(self, gui, panel_need_id, previous_data)
        gui.connect_signals(self.controller)
        self.controller.initialize_gui()
        if panel_need_id:
            gui.show_button_overwrite()

    def setup_structure_need(self, panel_need_id=None, previous_data=None):
        pass

    def setup_battery_quotation(self, panel_quotation_id=None, previous_data=None):
        pass

    def setup_bos_quotation(self, panel_quotation_id=None, previous_data=None):
        pass

    def setup_inverter_quotation(self, panel_quotation_id=None, previous_data=None):
        pass

    def setup_panel_quotation(self, panel_quotation_id=None, previous_data=None):
        self.close_bd_session()
        self.windows_queue.append((self.setup_panel_quotation, [panel_quotation_id]))
        gui = GPanelQuotation(self.window)
        self.controller = CPanelQuotation(self, gui, panel_quotation_id, previous_data)
        gui.connect_signals(self.controller)
        self.controller.initialize_gui()
        if panel_quotation_id:
            gui.show_button_overwrite()

    def setup_structure_quotation(self, panel_quotation_id=None, previous_data=None):
        pass

    # --------------------
    def go_back(self):
        del self.windows_queue[-1]
        function, arguments = self.windows_queue.pop()
        if self.previous_data and function in (self.setup_database, self.setup_panel_quotation, self.setup_panel_need):
            arguments.append(self.previous_data)
            self.previous_data = None
        function(*arguments)

    # -------------------- OTHER --------------------
    def close_bd_session(self):
        if getattr(self.controller, 'session', None):
            self.controller.session.close()

    # def clear_layout(self, layout):
    #     if layout is not None:
    #         while layout.count():
    #             child = layout.takeAt(0)
    #             if child.widget() is not None:
    #                 child.widget().deleteLater()
    #             elif child.layout() is not None:
    #                 self.clear_layout(child.layout())
