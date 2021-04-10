from PySide2.QtWidgets import QMessageBox

import models
from my_qt.dialogs.message_boxes import question_delete_confirmation
from utilities.searchs import rows_indices_filtered


class CSearcher:
    def __init__(self, c_master, gui, mode):
        self.c_master = c_master
        self.gui = gui
        if mode == 'needs':
            PanelModelClass = models.panel_need.PanelNeed
        elif mode == 'quotations':
            PanelModelClass = models.panel_quotation.PanelQuotation
        else:
            raise Exception('Invalid mode code')
        self.session = self.c_master.Session()
        self.panels = self.session.query(PanelModelClass).all()
        self.inversors = []
        self.batterys = []
        self.structures = []
        self.boss = []

        self.load_data()

    def search(self, text):
        self.gui.paint_nothing()
        if text:
            self.gui.paint_loading()
            self.gui.group_panel.show_rows(rows_indices_filtered(self.panels, text, self.gui.my_strings))
            self.gui.group_inverter.show_rows(rows_indices_filtered(self.inversors, text, self.gui.my_strings))
            self.gui.group_battery.show_rows(rows_indices_filtered(self.batterys, text, self.gui.my_strings))
            self.gui.group_structure.show_rows(rows_indices_filtered(self.structures, text, self.gui.my_strings))
            self.gui.group_bos.show_rows(rows_indices_filtered(self.boss, text, self.gui.my_strings))
            if self.gui.is_empty():
                self.gui.paint_interrogation()
            else:
                self.gui.paint_tick()
        else:
            self.load_data()

    def delete_battery_need(self, need_ids):
        pass

    def delete_bos_need(self, need_ids):
        pass

    def delete_inverter_need(self, need_ids):
        pass

    def delete_panel_need(self, need_ids):
        self.__delete_item(list=self.panels,
                           ModelClass=models.panel_need.PanelNeed,
                           item_ids=need_ids)

    def delete_structure_need(self, need_ids):
        pass

    def delete_battery_quotation(self, quotation_ids):
        pass

    def delete_bos_quotation(self, quotation_ids):
        pass

    def delete_inverter_quotation(self, quotation_ids):
        pass

    def delete_panel_quotation(self, quotation_ids):
        self.__delete_item(list=self.panels,
                           ModelClass=models.panel_quotation.PanelQuotation,
                           item_ids=quotation_ids)

    def delete_structure_quotation(self, quotation_ids):
        pass

    def load_data(self):
        self.gui.group_panel.load_items(self.panels)
        self.gui.group_inverter.load_items(self.inversors)
        self.gui.group_battery.load_items(self.batterys)
        self.gui.group_structure.load_items(self.structures)
        self.gui.group_bos.load_items(self.boss)

    def __delete_item(self, list, ModelClass, item_ids):
        if len(item_ids) > 1 and question_delete_confirmation() == QMessageBox.RejectRole:
            return

        for item_id in item_ids:
            item = self.session.query(ModelClass).filter_by(id=item_id).one()
            self.session.delete(item)
            list.remove(item)
            self.gui.group_panel.remove_row(item_id)
        models.try_commit(self.session)

        self.search(self.gui.text_searcher)
