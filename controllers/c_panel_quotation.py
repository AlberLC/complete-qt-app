from datetime import date, timedelta

from sqlalchemy.sql import and_, func

from controllers.c_panel import CPanel
from exceptions.abort_exception import AbortException
from models import try_commit, try_flush, Cells, Certificate, Mark, Place, Incoterm, PanelType, User
from models.company import Company
from models.panel_quotation import PanelQuotation
from my_qt.dialogs.message_boxes import inform_save_successful, warn
from resources import get_last_user, set_last_user
from utilities.various import to_none


class CPanelQuotation(CPanel):
    def __init__(self, c_master, gui, panel_quotation_id, current_item_data):
        super().__init__(c_master, gui, current_item_data)
        self.item = self.session.query(PanelQuotation).filter_by(id=panel_quotation_id).one_or_none()

    def changed_date(self):
        self.update_all_average()
        self.update_current_type_average()
        self.update_current_power_average()

    def clicked_save(self, overwrite: bool):
        super().clicked_save(overwrite)
        if not overwrite:
            self.update_all_average()
            self.update_current_type_average()
            self.update_current_power_average()

    def load_initial_data(self, default=True):
        company_names = [company.name for company in self.session.query(Company).order_by(Company.name).all()]
        mark_names = [mark.name for mark in self.session.query(Mark).order_by(Mark.name).all()]
        date_quotation = date.today()
        date_validity = date_quotation + timedelta(days=30)
        user_names = [user.name for user in self.session.query(User).order_by(User.name).all()]
        last_user = self.session.query(User).filter_by(name=get_last_user()).one_or_none()
        panel_type_names = [panel_type.name for panel_type in
                            self.session.query(PanelType).order_by(PanelType.name).all()]
        cells_number = [cells.number for cells in self.session.query(Cells).order_by(Cells.number).all()]
        certificate_names = [certificate.name for certificate in
                             self.session.query(Certificate).order_by(Certificate.name).all()]
        incoterm_names = [incoterm.name for incoterm in self.session.query(Incoterm).order_by(Incoterm.name).all()]
        place_names = [place.name for place in self.session.query(Place).order_by(Place.name).all()]
        self.gui.load_initial_data(company_names,
                                   mark_names,
                                   date_quotation,
                                   date_validity,
                                   user_names,
                                   last_user,
                                   panel_type_names,
                                   cells_number,
                                   certificate_names,
                                   incoterm_names,
                                   place_names,
                                   default)

    def save(self, overwrite: bool):
        company_name = self.gui.company
        total_power = self.gui.total_power
        price = self.gui.price
        user_name = self.gui.user
        panel_power = self.gui.panel_power

        if not company_name or not total_power or not price or not user_name or not panel_power:
            warn(self.my_strings.title_error, self.my_strings.message_save_panel_quotation_error_required,
                 self.my_strings.button_accept)
            raise AbortException('Not saved: empty required fields')

        date_quotation = self.gui.date_quotation
        date_validity = self.gui.date_validity
        observations = self.gui.observations
        n_contacts = self.gui.n_contacts
        efficiency = self.gui.efficiency
        tolerance = self.gui.tolerance
        warranty_product = self.gui.warranty_product
        warranty_performance = self.gui.warranty_performance

        company = self.session.query(Company).filter_by(name=company_name).one()

        mark = self.session.query(Mark).filter_by(name=self.gui.mark).one_or_none()
        if not mark and self.gui.mark:
            mark = Mark(None, self.gui.mark)
            self.session.add(mark)
            try_flush(self.session)

        user = self.session.query(User).filter_by(name=user_name).one_or_none()
        if not user and self.gui.user:
            user = User(None, self.gui.user)
            self.session.add(user)
            try_flush(self.session)

        panel_type = self.session.query(PanelType).filter_by(name=self.gui.panel_type).one_or_none()
        if not panel_type and self.gui.panel_type:
            panel_type = PanelType(None, self.gui.panel_type)
            self.session.add(panel_type)
            try_flush(self.session)

        cells = self.session.query(Cells).filter_by(number=self.gui.cells if self.gui.cells else None).one_or_none()
        if not cells and self.gui.cells:
            cells = Cells(None, self.gui.cells)
            self.session.add(cells)
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

        data = [total_power, price, date_quotation, date_validity, observations, n_contacts, panel_power, efficiency,
                tolerance, warranty_product, warranty_performance, company, mark, user, panel_type, cells, incoterm,
                made_in, origin, destination, certificates]
        to_none(data)

        if not self.save_unique_check(data, overwrite):
            raise AbortException('Not saved: not unique')

        if overwrite:
            self.item.set_data(data)
        else:
            new_panel_quotation = PanelQuotation(None, *data)
            self.session.add(new_panel_quotation)
            self.original_data = self.gui.data

        set_last_user(user.name)
        try_commit(self.session)
        inform_save_successful()

        if not overwrite:
            self.load_initial_data(default=False)
            self.gui.set_focus_nothing()

    def save_unique_check(self, data, overwrite):
        if overwrite:
            panel_quotations = self.session.query(PanelQuotation).filter_by(
                total_power=data[0], price=data[1], date_quotation=data[2], date_validity=data[3], observations=data[4],
                n_contacts=data[5], panel_power=data[6], efficiency=data[7], tolerance=data[8],
                warranty_product=data[9],
                warranty_performance=data[10], company=data[11], mark=data[12], user=data[13], panel_type=data[14],
                cells=data[15], incoterm=data[16], made_in=data[17], origin=data[18], destination=data[19]
            ).filter(PanelQuotation.id != self.item.id).all()
        else:
            panel_quotations = self.session.query(PanelQuotation).filter_by(
                total_power=data[0], price=data[1], date_quotation=data[2], date_validity=data[3], observations=data[4],
                n_contacts=data[5], panel_power=data[6], efficiency=data[7], tolerance=data[8],
                warranty_product=data[9],
                warranty_performance=data[10], company=data[11], mark=data[12], user=data[13], panel_type=data[14],
                cells=data[15], incoterm=data[16], made_in=data[17], origin=data[18], destination=data[19]
            ).all()

        for panel_quotation in panel_quotations:
            if set(panel_quotation.certificates) == set(data[20]):
                warn(self.my_strings.title_error,
                     self.my_strings.message_save_error_quotation_not_unique,
                     self.my_strings.button_accept)
                return False

        return True

    def update_all_average(self):
        all_average = self.session.query(func.avg(PanelQuotation.price)).filter(
            and_(PanelQuotation.date_quotation >= self.gui.date_quotation,
                 PanelQuotation.date_quotation <= self.gui.date_validity
                 )).scalar()
        if all_average:
            self.gui.price_bar_chart_all_average = all_average
        else:
            self.gui.price_bar_chart_all_average = 0

    def update_current_type_average(self):
        current_type_average = self.session.query(func.avg(PanelQuotation.price)).join(
            PanelQuotation.panel_type).filter(
            and_(PanelType.name == self.gui.panel_type,
                 PanelQuotation.date_quotation >= self.gui.date_quotation,
                 PanelQuotation.date_quotation <= self.gui.date_validity
                 )).scalar()
        if current_type_average:
            self.gui.price_bar_chart_current_type_average = current_type_average
        else:
            self.gui.price_bar_chart_current_type_average = 0

    def update_current_power_average(self):
        current_power_average = self.session.query(func.avg(PanelQuotation.price)).filter(
            and_(PanelQuotation.panel_power == self.gui.panel_power,
                 PanelQuotation.date_quotation >= self.gui.date_quotation,
                 PanelQuotation.date_quotation <= self.gui.date_validity
                 )).scalar()
        if current_power_average:
            self.gui.price_bar_chart_current_power_average = current_power_average
        else:
            self.gui.price_bar_chart_current_power_average = 0
