from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from my_qt.dialogs.message_boxes import warn_critical_save_error

Base = declarative_base()


def try_commit(session):
    try:
        session.commit()
    except Exception as e:
        session.rollback()
        warn_critical_save_error()
        raise e


def try_flush(session):
    try:
        session.flush()
    except Exception as e:
        session.rollback()
        warn_critical_save_error()
        raise e


class NameElement:
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    @classmethod
    def get_headers(cls):
        return [header[:-3] if header.endswith('_id') else header for header in cls.__table__.columns.keys()]

    @classmethod
    def get_not_nullable_columns(cls):
        columns = dict()
        for i, column in enumerate(cls.__table__.columns):
            if not column.nullable:
                columns[i] = column.name
        return columns

    @classmethod
    def get_unique_columns(cls):
        columns = dict()
        for i, column in enumerate(cls.__table__.columns):
            if column.unique:
                columns[i] = column.name
        return columns

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    @property
    def data(self):
        return [
            self.id,
            self.name
        ]


class AssessmentService(NameElement, Base):
    __tablename__ = 'assessment_service'


class BOSType(NameElement, Base):
    __tablename__ = 'bos_type'


class Cells(Base):
    __tablename__ = 'cells'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer, nullable=False, unique=True)

    def __init__(self, id, number):
        self.id = id
        self.number = number

    def __str__(self):
        return str(self.number)


class Certificate(NameElement, Base):
    __tablename__ = 'certificate'


class CompanyTier(NameElement, Base):
    __tablename__ = 'company_tier'


class CompanyType(NameElement, Base):
    __tablename__ = 'company_type'


class ExtraService(NameElement, Base):
    __tablename__ = 'extra_service'


class FinancialService(NameElement, Base):
    __tablename__ = 'financial_service'


class GeoZone(NameElement, Base):
    __tablename__ = 'geo_zone'


class Incoterm(NameElement, Base):
    __tablename__ = 'incoterm'


class InstallConstructService(NameElement, Base):
    __tablename__ = 'install_construct_service'


class InsuranceService(NameElement, Base):
    __tablename__ = 'insurance_service'


class InverterType(NameElement, Base):
    __tablename__ = 'inverter_type'


class Language(NameElement, Base):
    __tablename__ = 'language'


class LogisticService(NameElement, Base):
    __tablename__ = 'logistic_service'


class Mark(NameElement, Base):
    __tablename__ = 'mark'


class OperMainService(NameElement, Base):
    __tablename__ = 'oper_main_service'


class PanelType(NameElement, Base):
    __tablename__ = 'panel_type'


class Place(NameElement, Base):
    __tablename__ = 'place'


class ProjectDevService(NameElement, Base):
    __tablename__ = 'project_dev_service'


class ScopeRange(NameElement, Base):
    __tablename__ = 'scope_range'


class SolarSystem(NameElement, Base):
    __tablename__ = 'solar_system'


class StructureType(NameElement, Base):
    __tablename__ = 'structure_type'


class SystemDesignService(NameElement, Base):
    __tablename__ = 'system_design_service'


class User(NameElement, Base):
    __tablename__ = 'user'
