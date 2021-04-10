from datetime import date

from controllers.c_employee import CEmployee
from exceptions.abort_exception import AbortException
from models import try_commit, AssessmentService, BOSType, CompanyTier, CompanyType, ExtraService, \
    FinancialService, GeoZone, InstallConstructService, InsuranceService, InverterType, LogisticService, \
    OperMainService, PanelType, Place, ProjectDevService, ScopeRange, SolarSystem, StructureType, SystemDesignService, \
    User
from models import try_flush
from models.company import Company
from models.employee import Employee
from my_qt.dialogs.message_boxes import inform_save_successful, warn
from resources import get_last_user, set_last_user
from utilities.various import to_none


class CCompany(CEmployee):
    def __init__(self, c_master, gui, company_id):
        super().__init__(c_master, gui)
        if company_id:
            self.item = self.session.query(Company).filter_by(id=company_id).one()
        else:
            self.item = self.__new_company()
        self.dialog = None
        self.selected_employee = None
        self.staff_changed = False

    def exit(self):
        super().exit()
        self.session.rollback()
        # with self.c_master.engine.connect() as con:
        #     trans = con.begin()
        #     max_id = con.execute('SELECT MAX(id) from company').fetchall()[0][0]
        #     next_id = max_id + 1 if max_id is not None else 0
        #     con.execute(f'ALTER SEQUENCE company_id_seq RESTART WITH {next_id}')
        #     trans.commit()

    def load_initial_data(self, default=True):
        items = (
            [company_type.name for company_type in self.session.query(CompanyType).order_by(CompanyType.name).all()],
            [user.name for user in self.session.query(User).order_by(User.name).all()],
            [place.name for place in self.session.query(Place).order_by(Place.name).all()],
            [geo_zone.name for geo_zone in self.session.query(GeoZone).order_by(GeoZone.name).all()],
            [tier.name for tier in self.session.query(CompanyTier).order_by(CompanyTier.name).all()],
            [scope_range.name for scope_range in self.session.query(ScopeRange).order_by(ScopeRange.name).all()],

            [solar_system.name for solar_system in self.session.query(SolarSystem).order_by(SolarSystem.name).all()],
            [panel_type.name for panel_type in self.session.query(PanelType).order_by(PanelType.name).all()],
            [it.name for it in self.session.query(InverterType).order_by(InverterType.name).all()],
            [st.name for st in self.session.query(StructureType).order_by(StructureType.name).all()],
            [bos_type.name for bos_type in self.session.query(BOSType).order_by(BOSType.name).all()],

            [ass.name for ass in self.session.query(AssessmentService).order_by(AssessmentService.name).all()],
            [pjs.name for pjs in self.session.query(ProjectDevService).order_by(ProjectDevService.name).all()],
            [sds.name for sds in self.session.query(SystemDesignService).order_by(SystemDesignService.name).all()],
            [install_construct_service.name for install_construct_service in
             self.session.query(InstallConstructService).order_by(InstallConstructService.name).all()],
            [oms.name for oms in self.session.query(OperMainService).order_by(OperMainService.name).all()],
            [is_.name for is_ in self.session.query(InsuranceService).order_by(InsuranceService.name).all()],
            [fs.name for fs in self.session.query(FinancialService).order_by(FinancialService.name).all()],
            [ls.name for ls in self.session.query(LogisticService).order_by(LogisticService.name).all()],
            [extra_service.name for extra_service in
             self.session.query(ExtraService).order_by(ExtraService.name).all()]
        )
        last_user = self.session.query(User).filter_by(name=get_last_user()).one_or_none()
        loading_date = date.today()
        self.gui.load_initial_data(items, last_user, loading_date, default)

    def save(self, overwrite: bool):
        name = self.gui.name

        if not name:
            warn(self.my_strings.title_error, self.my_strings.message_save_error_required_name,
                 self.my_strings.button_accept)
            raise AbortException('No saved: empty required fields')

        comments = self.gui.comments
        source = self.gui.source
        loading_date = self.gui.date_loading
        address = self.gui.address
        email = self.gui.email
        phone = self.gui.phone
        web = self.gui.web
        id_document = self.gui.id_document
        solarnub_verification = self.gui.sn_verification
        verification_date = self.gui.date_verification

        formation_year = self.gui.formation_year
        rel_with_this_company = self.gui.rel_with_this_company
        annual_capacity = self.gui.annual_capacity
        reply_ratio = self.gui.reply_ratio
        n_contacts = self.gui.n_contacts
        n_replies = self.gui.n_replies
        signed_document = self.gui.signed_document

        user = self.session.query(User).filter_by(name=self.gui.user).one_or_none()
        if not user and self.gui.user:
            user = User(None, self.gui.user)
            self.session.add(user)
            try_flush(self.session)

        country = self.session.query(Place).filter_by(name=self.gui.country).one_or_none()
        if not country and self.gui.country:
            place = Place(None, self.gui.country)
            self.session.add(place)
            try_flush(self.session)

        province = self.session.query(Place).filter_by(name=self.gui.province).one_or_none()
        if not province and self.gui.province:
            place = Place(None, self.gui.province)
            self.session.add(place)
            try_flush(self.session)

        geo_zone = self.session.query(GeoZone).filter_by(name=self.gui.geo_zone).one_or_none()
        if not geo_zone and self.gui.geo_zone:
            geo_zone = GeoZone(None, self.gui.geo_zone)
            self.session.add(geo_zone)
            try_flush(self.session)

        verification_user = self.session.query(User).filter_by(name=self.gui.verification_user).one_or_none()
        if not verification_user and self.gui.verification_user:
            user = User(None, self.gui.verification_user)
            self.session.add(user)
            try_flush(self.session)

        tier = self.session.query(CompanyTier).filter_by(name=self.gui.tier).one_or_none()
        if not tier and self.gui.tier:
            tier = CompanyTier(None, self.gui.tier)
            self.session.add(tier)
            try_flush(self.session)

        scope_range = self.session.query(ScopeRange).filter_by(name=self.gui.scope_range).one_or_none()
        if not scope_range and self.gui.scope_range:
            scope_range = ScopeRange(None, self.gui.scope_range)
            self.session.add(scope_range)
            try_flush(self.session)

        types = self.session.query(CompanyType).filter(CompanyType.name.in_(self.gui.types)).all()
        solar_systems = self.session.query(SolarSystem).filter(SolarSystem.name.in_(self.gui.solar_systems)).all()
        panel_types = self.session.query(PanelType).filter(PanelType.name.in_(self.gui.panel_types)).all()
        inverter_types = self.session.query(InverterType).filter(InverterType.name.in_(self.gui.inverter_types)).all()
        structure_types = self.session.query(StructureType).filter(
            StructureType.name.in_(self.gui.structure_types)).all()
        bos_types = self.session.query(BOSType).filter(BOSType.name.in_(self.gui.bos_types)).all()
        assesment_services = self.session.query(AssessmentService).filter(
            AssessmentService.name.in_(self.gui.assessment_services)).all()
        project_dev_services = self.session.query(ProjectDevService).filter(
            ProjectDevService.name.in_(self.gui.project_dev_services)).all()
        system_design_services = self.session.query(SystemDesignService).filter(
            SystemDesignService.name.in_(self.gui.system_design_services)).all()
        install_construct_services = self.session.query(InstallConstructService).filter(
            InstallConstructService.name.in_(self.gui.install_construct_services)).all()
        oper_main_services = self.session.query(OperMainService).filter(
            OperMainService.name.in_(self.gui.oper_main_services)).all()
        insurance_services = self.session.query(InsuranceService).filter(
            InsuranceService.name.in_(self.gui.insurance_services)).all()
        financial_services = self.session.query(FinancialService).filter(
            FinancialService.name.in_(self.gui.financial_services)).all()
        logistic_services = self.session.query(LogisticService).filter(
            LogisticService.name.in_(self.gui.logistic_services)).all()
        extra_services = self.session.query(ExtraService).filter(
            ExtraService.name.in_(self.gui.extra_services)).all()

        data = [name, comments, source, loading_date, address, email, phone, web, id_document, solarnub_verification,
                verification_date, formation_year, rel_with_this_company, annual_capacity, reply_ratio, n_contacts,
                n_replies, signed_document, user, country, province, geo_zone, verification_user, tier, scope_range,
                types, panel_types, inverter_types, structure_types, bos_types, solar_systems, assesment_services,
                project_dev_services, system_design_services, install_construct_services, oper_main_services,
                insurance_services, financial_services, logistic_services, extra_services]
        to_none(data)

        if not self.save_unique_check(data, overwrite):
            raise AbortException('No saved: not unique')

        self.item.set_data(data)

        if user:
            set_last_user(user.name)
        try_commit(self.session)
        inform_save_successful()

        if not overwrite:
            self.item = self.__new_company()
            self.original_data = self.gui.data
            self.load_initial_data(default=False)
            self.gui.set_focus_nothing()

    def save_employee(self):
        data = self.get_data_employee()

        if self.selected_employee:
            self.selected_employee.set_data(data)
        else:
            new_employee = Employee(None, *data)
            self.item.staff.append(new_employee)
            try_flush(self.session)

        self.gui.load_staff(getattr(self.item, 'staff', ()))

    def save_unique_check(self, data, overwrite):
        if overwrite:
            company = self.session.query(Company).filter_by(name=data[0]).filter(
                Company.id != self.item.id).one_or_none()
        else:
            company = self.session.query(Company).filter_by(name=data[0]).one_or_none()
        if company:
            warn(self.my_strings.title_error,
                 self.my_strings.message_save_error_company_name_not_unique,
                 self.my_strings.button_accept)
            return False

        if data[7]:  # web
            if overwrite:
                web = self.session.query(Company).filter_by(web=data[7]).filter(
                    Company.id != self.item.id).one_or_none()
            else:
                web = self.session.query(Company).filter_by(web=data[7]).one_or_none()
            if web:
                warn(self.my_strings.title_error,
                     self.my_strings.message_save_error_company_web_not_unique,
                     self.my_strings.button_accept)
                return False

        return True

    def __new_company(self):
        new_company = Company(None)
        self.session.add(new_company)
        try_flush(self.session)
        return new_company
