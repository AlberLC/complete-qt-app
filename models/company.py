from sqlalchemy import Table, Column, Integer, Float, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship

from models import Base
from utilities.various import normalize

rel_company_company_type = Table(
    'rel_company_company_type',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('company_type_id', Integer, ForeignKey('company_type.id'), primary_key=True)
)

rel_company_panel_type = Table(
    'rel_company_panel_type',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('panel_type_id', Integer, ForeignKey('panel_type.id'), primary_key=True)
)

rel_company_inverter_type = Table(
    'rel_company_inverter_type',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('inverter_type_id', Integer, ForeignKey('inverter_type.id'), primary_key=True)
)

rel_company_structure_type = Table(
    'rel_company_structure_type',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('structure_type_id', Integer, ForeignKey('structure_type.id'), primary_key=True)
)

rel_company_bos_type = Table(
    'rel_company_bos_type',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('bos_type_id', Integer, ForeignKey('bos_type.id'), primary_key=True)
)

rel_company_solar_system = Table(
    'rel_company_solar_system',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('solar_system_id', Integer, ForeignKey('solar_system.id'), primary_key=True)
)

rel_company_assessment_service = Table(
    'rel_company_assessment_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('assessment_service_id', Integer, ForeignKey('assessment_service.id'), primary_key=True)
)

rel_company_project_dev_service = Table(
    'rel_company_project_dev_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('project_dev_service_id', Integer, ForeignKey('project_dev_service.id'), primary_key=True)
)

rel_company_system_design_service = Table(
    'rel_company_system_design_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('system_design_service_id', Integer, ForeignKey('system_design_service.id'), primary_key=True)
)

rel_company_install_construct_service = Table(
    'rel_company_install_construct_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('install_construct_service_id', Integer, ForeignKey('install_construct_service.id'), primary_key=True)
)

rel_company_oper_main_service = Table(
    'rel_company_oper_main_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('oper_main_service_id', Integer, ForeignKey('oper_main_service.id'), primary_key=True)
)

rel_company_insurance_service = Table(
    'rel_company_insurance_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('insurance_service_id', Integer, ForeignKey('insurance_service.id'), primary_key=True)
)

rel_company_financial_service = Table(
    'rel_company_financial_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('financial_service_id', Integer, ForeignKey('financial_service.id'), primary_key=True)
)

rel_company_logistic_service = Table(
    'rel_company_logistic_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('logistic_service_id', Integer, ForeignKey('logistic_service.id'), primary_key=True)
)

rel_company_extra_service = Table(
    'rel_company_extra_service',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('extra_service_id', Integer, ForeignKey('extra_service.id'), primary_key=True)
)

rel_company_employee = Table(
    'rel_company_employee',
    Base.metadata,
    Column('company_id', Integer, ForeignKey('company.id'), primary_key=True),
    Column('employee_id', Integer, ForeignKey('employee.id'), primary_key=True)
)


class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    comments = Column(String)
    source = Column(String)
    loading_date = Column(Date)
    address = Column(String)
    email = Column(String)
    phone = Column(String)
    web = Column(String)
    id_document = Column(String)
    sn_verification = Column(Boolean)
    verification_date = Column(Date)
    formation_year = Column(Integer)
    rel_with_this_company = Column(Boolean)
    annual_capacity = Column(Float)
    reply_ratio = Column(Float)
    n_contacts = Column(Integer)
    n_replies = Column(Integer)
    signed_document = Column(Boolean)

    user_id = Column(Integer, ForeignKey('user.id'))
    country_id = Column(Integer, ForeignKey('place.id'))
    province_id = Column(Integer, ForeignKey('place.id'))
    geo_zone_id = Column(Integer, ForeignKey('geo_zone.id'))
    verification_user_id = Column(Integer, ForeignKey('user.id'))
    tier_id = Column(Integer, ForeignKey('company_tier.id'))
    scope_range_id = Column(Integer, ForeignKey('scope_range.id'))

    user = relationship('User', foreign_keys=user_id)
    country = relationship('Place', foreign_keys=country_id)
    province = relationship('Place', foreign_keys=province_id)
    geo_zone = relationship('GeoZone')
    verification_user = relationship('User', foreign_keys=verification_user_id)
    tier = relationship('CompanyTier')
    scope_range = relationship('ScopeRange')

    types = relationship('CompanyType', secondary=rel_company_company_type)

    panel_types = relationship('PanelType', secondary=rel_company_panel_type)
    inverter_types = relationship('InverterType', secondary=rel_company_inverter_type)
    structure_types = relationship('StructureType', secondary=rel_company_structure_type)
    bos_types = relationship('BOSType', secondary=rel_company_bos_type)
    solar_systems = relationship('SolarSystem', secondary=rel_company_solar_system)

    assessment_services = relationship('AssessmentService', secondary=rel_company_assessment_service)
    project_dev_services = relationship('ProjectDevService', secondary=rel_company_project_dev_service)
    system_design_services = relationship('SystemDesignService', secondary=rel_company_system_design_service)
    install_construct_services = relationship('InstallConstructService',
                                              secondary=rel_company_install_construct_service)
    oper_main_services = relationship('OperMainService', secondary=rel_company_oper_main_service)
    insurance_services = relationship('InsuranceService', secondary=rel_company_insurance_service)
    financial_services = relationship('FinancialService', secondary=rel_company_financial_service)
    logistic_services = relationship('LogisticService', secondary=rel_company_logistic_service)
    extra_services = relationship('ExtraService', secondary=rel_company_extra_service)

    staff = relationship('Employee', secondary=rel_company_employee)

    panel_quotations = relationship('PanelQuotation', cascade='all,delete-orphan')

    @classmethod
    def get_headers(cls):
        return [header[:-3] if header.endswith('_id') else header for header in cls.__table__.columns.keys()]

    def __init__(self, id, data=None):
        self.id = id
        if data:
            self.set_data(data)

    def __str__(self):
        return self.name

    @property
    def data(self):
        return [
            self.id,
            self.name,
            self.comments,
            self.source,
            self.loading_date,
            self.address,
            self.email,
            self.phone,
            self.web,
            self.id_document,
            self.sn_verification,
            self.verification_date,
            self.formation_year,
            self.rel_with_this_company,
            self.annual_capacity,
            self.reply_ratio,
            self.n_contacts,
            self.n_replies,
            self.signed_document,
            self.user.name if self.user else None,
            self.country.name if self.country else None,
            self.province.name if self.province else None,
            self.geo_zone.name if self.geo_zone else None,
            self.verification_user.name if self.verification_user else None,
            self.tier.name if self.tier else None,
            self.scope_range.name if self.scope_range else None
        ]

    def get_keywords(self, my_strings):
        return {
            *normalize(self.name).split(),
            *sum([normalize(type).split() for type in self.types], []),
            *normalize(self.comments).split(),
            *normalize(self.source).split(),
            *normalize(self.user).split(),
            *normalize(self.country).split(),
            *normalize(self.province).split(),
            *normalize(self.geo_zone).split(),
            *normalize(self.address).split(),
            *normalize(self.email).split(),
            *normalize(self.phone).split(),
            *normalize(self.web).split(),
            *normalize(self.id_document).split(),
            my_strings.radio_yes if self.sn_verification else my_strings.radio_no,
            *normalize(self.verification_user).split(),
            *normalize(self.tier).split(),
            my_strings.radio_yes if self.rel_with_this_company else my_strings.radio_no,
            *normalize(self.scope_range).split(),
            my_strings.radio_yes if self.signed_document else my_strings.radio_no,

            *sum([normalize(panel_type).split() for panel_type in self.panel_types], []),
            *sum([normalize(inverter_type).split() for inverter_type in self.inverter_types], []),
            *sum([normalize(structure_type).split() for structure_type in self.structure_types], []),
            *sum([normalize(bos_type).split() for bos_type in self.bos_types], []),
            *sum([normalize(solar_system).split() for solar_system in self.solar_systems], []),

            *sum([normalize(assessment_service).split() for assessment_service in self.assessment_services], []),
            *sum([normalize(project_dev_service).split() for project_dev_service in self.project_dev_services], []),
            *sum([normalize(sds).split() for sds in self.system_design_services], []),
            *sum([normalize(ics).split() for ics in self.install_construct_services], []),
            *sum([normalize(oper_main_service).split() for oper_main_service in self.oper_main_services], []),
            *sum([normalize(insurance_service).split() for insurance_service in self.insurance_services], []),
            *sum([normalize(financial_service).split() for financial_service in self.financial_services], []),
            *sum([normalize(logistic_service).split() for logistic_service in self.logistic_services], []),
            *sum([normalize(extra_service).split() for extra_service in self.extra_services], [])
        }

    def set_data(self, data):
        self.name = data[0]
        self.comments = data[1]
        self.source = data[2]
        self.loading_date = data[3]
        self.address = data[4]
        self.email = data[5]
        self.phone = data[6]
        self.web = data[7]
        self.id_document = data[8]
        self.sn_verification = data[9]
        self.verification_date = data[10]
        self.formation_year = data[11]
        self.rel_with_this_company = data[12]
        self.annual_capacity = data[13]
        self.reply_ratio = data[14]
        self.n_contacts = data[15]
        self.n_replies = data[16]
        self.signed_document = data[17]

        self.user = data[18]
        self.country = data[19]
        self.province = data[20]
        self.geo_zone = data[21]
        self.verification_user = data[22]
        self.tier = data[23]
        self.scope_range = data[24]

        self.types = data[25]

        self.panel_types = data[26]
        self.inverter_types = data[27]
        self.structure_types = data[28]
        self.bos_types = data[29]
        self.solar_systems = data[30]

        self.assessment_services = data[31]
        self.project_dev_services = data[32]
        self.system_design_services = data[33]
        self.install_construct_services = data[34]
        self.oper_main_services = data[35]
        self.insurance_services = data[36]
        self.financial_services = data[37]
        self.logistic_services = data[38]
        self.extra_services = data[39]
        # self.staff = data[40]
