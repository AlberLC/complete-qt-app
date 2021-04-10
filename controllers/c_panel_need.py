import time
from datetime import date, timedelta
from threading import Thread, Condition

from sqlalchemy.sql import and_, func

from controllers.c_panel import CPanel
from exceptions.abort_exception import AbortException
from models import try_commit, try_flush, Cells, Certificate, Mark, Place, Incoterm, PanelType
from models.company import Company
from models.panel_need import PanelNeed
from models.panel_quotation import PanelQuotation
from my_qt.dialogs.message_boxes import inform_save_successful, warn
from utilities.various import EXACT_MATCH, IN_RANGE_MATCH, match_with_error, to_none


class CPanelNeed(CPanel):
    ERROR_RANGE_EFFICIENCY = 1
    ERROR_RANGE_PANEL_POWER = 5
    ERROR_RANGE_PRICE = 0.05

    FACTOR_NO_EXACTLY_MATCH = 0.75

    SCORE_COMPANY = 1
    SCORE_MARK = 2
    SCORE_TOTAL_POWER = 10
    SCORE_PRICE = 100
    SCORE_PANEL_TYPE = 200
    SCORE_CELLS = 90
    SCORE_PANEL_POWER = 410
    SCORE_EFFICIENCY = 80
    SCORE_TOLERANCE = 30
    SCORE_WARRANTY_PRODUCT = 30
    SCORE_WARRANTY_PERFORMANCE = 30
    SCORE_CERTIFICATES = 30
    SCORE_INCOTERM = 40
    SCORE_MADE_IN = 200
    SCORE_ORIGIN = 20
    SCORE_DESTINATION = 20

    SEARCH_WAIT_PERIOD = 1

    def __init__(self, c_master, gui, panel_need_id, current_item_data):
        super().__init__(c_master, gui, current_item_data)
        self.signal_search = self.gui.signal_search
        self.item = self.session.query(PanelNeed).filter_by(id=panel_need_id).one_or_none()
        self.can_search = False
        self.thread_can_run = True
        self.condition = Condition()
        self.thread = Thread(target=self.__thread_run)
        self.thread.daemon = True
        self.time_goal = time.time()

        self.thread.start()

    def changed(self):
        if self.can_search:
            self.time_goal = time.time() + self.SEARCH_WAIT_PERIOD
            with self.condition:
                self.condition.notify()

    def clicked_check_priorities(self):
        if self.gui.priorities:
            self.gui.set_priorities_visible(True)
        else:
            self.gui.set_priorities_visible(False)
        self.update_related_panel_quotations()

    def double_clicked_table_rel(self, panel_quotation_id):
        self.c_master.previous_data = self.gui.data
        self.c_master.setup_panel_quotation(panel_quotation_id)

    def exit(self):
        super().exit()
        self.thread_can_run = False
        with self.condition:
            self.condition.notify()

    def initialize_gui(self):
        super().initialize_gui()
        self.can_search = True
        self.update_related_panel_quotations()

    def load_initial_data(self, default=True):
        company_names = [company.name for company in self.session.query(Company).order_by(Company.name).all()]
        mark_names = [mark.name for mark in self.session.query(Mark).order_by(Mark.name).all()]
        panel_type_names = [panel_type.name for panel_type in
                            self.session.query(PanelType).order_by(PanelType.name).all()]
        cells_number = [cells.number for cells in self.session.query(Cells).order_by(Cells.number).all()]
        certificate_names = [certificate.name for certificate in
                             self.session.query(Certificate).order_by(Certificate.name).all()]
        incoterm_names = [incoterm.name for incoterm in self.session.query(Incoterm).order_by(Incoterm.name).all()]
        place_names = [place.name for place in self.session.query(Place).order_by(Place.name).all()]
        all_average = self.session.query(func.avg(PanelQuotation.price)).scalar()
        self.gui.load_initial_data(company_names,
                                   mark_names,
                                   panel_type_names,
                                   cells_number,
                                   certificate_names,
                                   incoterm_names,
                                   place_names,
                                   all_average if all_average else 0,
                                   default)

    def save(self, overwrite: bool):
        total_power = self.gui.total_power
        price = self.gui.price
        panel_power = self.gui.panel_power

        if not total_power or not price or not panel_power:
            warn(self.my_strings.title_error, self.my_strings.message_save_panel_need_error_required,
                 self.my_strings.button_accept)
            raise AbortException('Not saved: empty required fields')

        efficiency = self.gui.efficiency
        tolerance = self.gui.tolerance
        warranty_product = self.gui.warranty_product
        warranty_performance = self.gui.warranty_performance

        company = self.session.query(Company).filter_by(name=self.gui.company).one_or_none()

        mark = self.session.query(Mark).filter_by(name=self.gui.mark).one_or_none()
        if not mark and self.gui.mark:
            mark = Mark(None, self.gui.mark)
            self.session.add(mark)
            try_flush(self.session)

        incoterm = self.session.query(Incoterm).filter_by(name=self.gui.incoterm).one_or_none()
        if not incoterm and self.gui.incoterm:
            incoterm = Incoterm(None, self.gui.incoterm)
            self.session.add(incoterm)
            try_flush(self.session)

        made_in = self.session.query(Place).filter_by(name=self.gui.made_in).one_or_none()
        if not made_in and self.gui.made_in:
            made_in = Place(None, self.gui.made_in)
            self.session.add(made_in)
            try_flush(self.session)

        origin = self.session.query(Place).filter_by(name=self.gui.origin).one_or_none()
        if not origin and self.gui.origin:
            origin = Place(None, self.gui.origin)
            self.session.add(origin)
            try_flush(self.session)

        destination = self.session.query(Place).filter_by(name=self.gui.destination).one_or_none()
        if not destination and self.gui.destination:
            destination = Place(None, self.gui.destination)
            self.session.add(destination)
            try_flush(self.session)

        certificates = self.session.query(Certificate).filter(Certificate.name.in_(self.gui.checked_certificates)).all()

        panel_types = self.session.query(PanelType).filter(PanelType.name.in_(self.gui.checked_panel_types)).all()

        cells = self.session.query(Cells).filter(Cells.number.in_(self.gui.checked_cells)).all()

        data = [total_power, price, panel_power, efficiency, tolerance, warranty_product, warranty_performance, company,
                mark, incoterm, made_in, origin, destination, certificates, panel_types, cells]
        to_none(data)

        if not self.save_unique_check(data, overwrite):
            raise AbortException('Not saved: not unique')

        if overwrite:
            self.item.set_data(data)
        else:
            new_panel_need = PanelNeed(None, *data)
            self.session.add(new_panel_need)
            self.original_data = self.gui.data

        try_commit(self.session)
        inform_save_successful()

        if not overwrite:
            self.load_initial_data(default=False)
            self.gui.set_focus_nothing()

    def save_unique_check(self, data, overwrite):
        if overwrite:
            panel_needs = self.session.query(PanelNeed).filter_by(
                total_power=data[0], price=data[1], panel_power=data[2], efficiency=data[3], tolerance=data[4],
                warranty_product=data[5], warranty_performance=data[6], company=data[7], mark=data[8],
                incoterm=data[9], made_in=data[10], origin=data[11], destination=data[12]
            ).filter(PanelNeed.id != self.item.id).all()
        else:
            panel_needs = self.session.query(PanelNeed).filter_by(
                total_power=data[0], price=data[1], panel_power=data[2], efficiency=data[3], tolerance=data[4],
                warranty_product=data[5], warranty_performance=data[6], company=data[7], mark=data[8],
                incoterm=data[9], made_in=data[10], origin=data[11], destination=data[12]
            ).all()

        for panel_need in panel_needs:
            if (
                    set(panel_need.certificates) == set(data[13]) and
                    set(panel_need.panel_types) == set(data[14]) and
                    set(panel_need.cells) == set(data[15])
            ):
                warn(self.my_strings.title_error,
                     self.my_strings.message_save_error_need_not_unique,
                     self.my_strings.button_accept)
                return False

        return True

    def update_all_average(self):
        today = date.today()
        all_average = self.session.query(func.avg(PanelQuotation.price)).filter(
            and_(PanelQuotation.date_quotation >= today - timedelta(weeks=24),
                 PanelQuotation.date_quotation <= today
                 )).scalar()
        if all_average:
            self.gui.price_bar_chart_all_average = all_average
        else:
            self.gui.price_bar_chart_all_average = 0

    def update_current_type_average(self):
        today = date.today()
        current_type_average = self.session.query(func.avg(PanelQuotation.price)).join(
            PanelQuotation.panel_type).filter(
            and_(PanelType.name.in_(self.gui.checked_panel_types),
                 PanelQuotation.date_quotation >= today - timedelta(weeks=24),
                 PanelQuotation.date_quotation <= today
                 )).scalar()
        if current_type_average:
            self.gui.price_bar_chart_current_type_average = current_type_average
        else:
            self.gui.price_bar_chart_current_type_average = 0

    def update_current_power_average(self):
        today = date.today()
        current_power_average = self.session.query(func.avg(PanelQuotation.price)).filter(
            and_(PanelQuotation.panel_power == self.gui.panel_power,
                 PanelQuotation.date_quotation >= today - timedelta(weeks=24),
                 PanelQuotation.date_quotation <= today
                 )).scalar()
        if current_power_average:
            self.gui.price_bar_chart_current_power_average = current_power_average
        else:
            self.gui.price_bar_chart_current_power_average = 0

    def update_related_panel_quotations(self):
        class PrioritizedPanelQuotation:
            def __init__(self, panel_quotation):
                self.custom_priority = 0  # Chosen in GUI
                self.main_priority = 0  # Mark and Company are very important matchs
                self.priority = 0  # Rest
                self.in_date = True
                self.panel_quotation = panel_quotation  # Data

            def add_to_custom_priority(self, priority_text, factor_no_exactly_match=1):
                if priority_text == '-':
                    value = 0
                else:
                    value = abs(int(priority_text) - 15) * factor_no_exactly_match
                self.custom_priority += value

        all_panel_quotations = self.session.query(PanelQuotation).all()
        filtered_prioritized_panel_quotations = []
        for panel_quotation in all_panel_quotations:
            prioritized_panel_quotation = PrioritizedPanelQuotation(panel_quotation)

            # ----------------------------------------
            # ---------- General parameters ----------
            # ----------------------------------------
            if panel_quotation.company and str(panel_quotation.company) == self.gui.company:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_company)
                prioritized_panel_quotation.main_priority += self.SCORE_COMPANY

            if panel_quotation.mark and str(panel_quotation.mark) == self.gui.mark:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_mark)
                prioritized_panel_quotation.main_priority += self.SCORE_MARK

            if panel_quotation.total_power and panel_quotation.total_power == self.gui.total_power:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_total_power)
                prioritized_panel_quotation.priority += self.SCORE_TOTAL_POWER

            if panel_quotation.price:
                match = match_with_error(panel_quotation.price, self.gui.price, self.ERROR_RANGE_PRICE)
                if match == EXACT_MATCH:
                    if self.gui.priorities:
                        prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_price)
                    prioritized_panel_quotation.priority += self.SCORE_PRICE
                elif match == IN_RANGE_MATCH:
                    if self.gui.priorities:
                        prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_price,
                                                                           self.FACTOR_NO_EXACTLY_MATCH)
                    prioritized_panel_quotation.priority += self.SCORE_PRICE * self.FACTOR_NO_EXACTLY_MATCH

            today = date.today()
            if not today - timedelta(weeks=24) <= panel_quotation.date_quotation <= today:
                prioritized_panel_quotation.in_date = False

            # --------------------------------------
            # ---------- Panel parameters ----------
            # --------------------------------------
            if str(panel_quotation.panel_type) in self.gui.checked_panel_types:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_panel_type)
                prioritized_panel_quotation.priority += self.SCORE_PANEL_TYPE

            if str(panel_quotation.cells) in self.gui.checked_cells:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_cells)
                prioritized_panel_quotation.priority += self.SCORE_CELLS

            if panel_quotation.panel_power:
                match = match_with_error(panel_quotation.panel_power, self.gui.panel_power,
                                         self.ERROR_RANGE_PANEL_POWER)
                if match == EXACT_MATCH:
                    if self.gui.priorities:
                        prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_panel_power)
                    prioritized_panel_quotation.priority += self.SCORE_PANEL_POWER
                elif match == IN_RANGE_MATCH:
                    if self.gui.priorities:
                        prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_panel_power,
                                                                           self.FACTOR_NO_EXACTLY_MATCH)
                    prioritized_panel_quotation.priority += self.SCORE_PANEL_POWER * self.FACTOR_NO_EXACTLY_MATCH

            if panel_quotation.efficiency:
                match = match_with_error(panel_quotation.efficiency, self.gui.efficiency, self.ERROR_RANGE_EFFICIENCY)
                if match == EXACT_MATCH:
                    if self.gui.priorities:
                        prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_efficiency)
                    prioritized_panel_quotation.priority += self.SCORE_EFFICIENCY
                elif match == IN_RANGE_MATCH:
                    if self.gui.priorities:
                        prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_efficiency,
                                                                           self.FACTOR_NO_EXACTLY_MATCH)
                    prioritized_panel_quotation.priority += self.SCORE_EFFICIENCY * self.FACTOR_NO_EXACTLY_MATCH

            if panel_quotation.tolerance == self.gui.tolerance:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_tolerance)
                prioritized_panel_quotation.priority += self.SCORE_TOLERANCE

            if panel_quotation.warranty_product and panel_quotation.warranty_product == self.gui.warranty_product:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_warranty_product)
                prioritized_panel_quotation.priority += self.SCORE_WARRANTY_PRODUCT

            if panel_quotation.warranty_performance and panel_quotation.warranty_performance == self.gui.warranty_performance:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_warranty_performance)
                prioritized_panel_quotation.priority += self.SCORE_WARRANTY_PERFORMANCE

            certificates = [str(certificate) for certificate in panel_quotation.certificates]
            if certificates and set(certificates) == set(self.gui.checked_certificates):
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_certificates)
                prioritized_panel_quotation.priority += self.SCORE_CERTIFICATES

            # ---------------------------------------------
            # ---------- Geographical parameters ----------
            # ---------------------------------------------
            if panel_quotation.incoterm and str(panel_quotation.incoterm) == self.gui.incoterm:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_incoterm)
                prioritized_panel_quotation.priority += self.SCORE_INCOTERM

            if panel_quotation.made_in and str(panel_quotation.made_in) == self.gui.made_in:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_made_in)
                prioritized_panel_quotation.priority += self.SCORE_MADE_IN

            if panel_quotation.origin and str(panel_quotation.origin) == self.gui.origin:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_origin)
                prioritized_panel_quotation.priority += self.SCORE_ORIGIN

            if panel_quotation.destination and str(panel_quotation.destination) == self.gui.destination:
                if self.gui.priorities:
                    prioritized_panel_quotation.add_to_custom_priority(self.gui.priority_destination)
                prioritized_panel_quotation.priority += self.SCORE_DESTINATION

            filtered_prioritized_panel_quotations.append(prioritized_panel_quotation)

        sorted_prioritized_panel_quotations = sorted(filtered_prioritized_panel_quotations,
                                                     key=lambda fpq: (fpq.custom_priority,
                                                                      fpq.main_priority,
                                                                      fpq.priority,
                                                                      fpq.in_date),
                                                     reverse=True)

        self.gui.load_related_panel_quotations(sorted_prioritized_panel_quotations)

    def __thread_run(self):
        while self.thread_can_run:
            with self.condition:
                self.condition.wait()
            if not self.thread_can_run:
                return
            now = time.time()
            while now < self.time_goal:
                time.sleep(self.time_goal - now)
                if not self.thread_can_run:
                    return
                now = time.time()
            self.signal_search.emit()
