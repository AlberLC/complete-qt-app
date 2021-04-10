from controllers.c_base import CBase


class CPanel(CBase):
    def __init__(self, c_master, gui, current_item_data):
        super().__init__(c_master, gui, current_item_data)

    def clicked_add_company(self):
        self.c_master.previous_data = self.gui.data
        self.c_master.setup_company()

    def initialize_gui(self):
        super().initialize_gui()
        self.update_all_average()

    def remove_certificate(self, index):
        # if index == -1:
        #     index = self.gui.certificates_list_widget.count() - 1
        if index != -1:
            self.gui.certificates_list_widget.takeItem(index)
            self.gui.certificates_list_widget.setCurrentRow(-1)
