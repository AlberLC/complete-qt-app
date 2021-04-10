from sqlalchemy import Table, Column, Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from models import Base
from utilities.various import normalize

rel_panel_need_certificate = Table(
    'rel_panel_need_certificate',
    Base.metadata,
    Column('panel_need_id', Integer, ForeignKey('panel_need.id'), primary_key=True),
    Column('certificate_id', Integer, ForeignKey('certificate.id'), primary_key=True)
)

rel_panel_need_panel_type = Table(
    'rel_panel_need_panel_type',
    Base.metadata,
    Column('panel_need_id', Integer, ForeignKey('panel_need.id'), primary_key=True),
    Column('panel_type_id', Integer, ForeignKey('panel_type.id'), primary_key=True)
)

rel_panel_need_cells = Table(
    'rel_panel_need_cells',
    Base.metadata,
    Column('panel_need_id', Integer, ForeignKey('panel_need.id'), primary_key=True),
    Column('cells_id', Integer, ForeignKey('cells.id'), primary_key=True)
)


class PanelNeed(Base):
    __tablename__ = 'panel_need'
    id = Column(Integer, primary_key=True, autoincrement=True)
    total_power = Column(Float, nullable=False)
    price = Column(Integer, nullable=False)

    panel_power = Column(Float, nullable=False)
    efficiency = Column(Float)
    tolerance = Column(Boolean)
    warranty_product = Column(Integer)
    warranty_performance = Column(Integer)

    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
    mark_id = Column(Integer, ForeignKey('mark.id'))
    incoterm_id = Column(Integer, ForeignKey('incoterm.id'))
    made_in_id = Column(Integer, ForeignKey('place.id'))
    origin_id = Column(Integer, ForeignKey('place.id'))
    destination_id = Column(Integer, ForeignKey('place.id'))

    company = relationship('Company')
    mark = relationship('Mark')
    incoterm = relationship('Incoterm')
    made_in = relationship('Place', foreign_keys=made_in_id)
    origin = relationship('Place', foreign_keys=origin_id)
    destination = relationship('Place', foreign_keys=destination_id)
    certificates = relationship('Certificate', secondary=rel_panel_need_certificate, backref='panel_needs')
    panel_types = relationship('PanelType', secondary=rel_panel_need_panel_type)
    cells = relationship('Cells', secondary=rel_panel_need_cells)

    def __init__(self, *args):
        self.id = args[0]
        self.set_data(args[1:])

    def get_keywords(self, my_strings):
        return {
            'need',
            'needs',
            'necesidad',
            'necesidades',
            *normalize(self.company).split(),
            *normalize(self.mark).split(),
            *sum([normalize(panel_type).split() for panel_type in self.panel_types], []),
            my_strings.radio_positive if self.tolerance else my_strings.radio_negative,
            *normalize(self.incoterm).split(),
            *normalize(self.made_in).split(),
            *normalize(self.origin).split(),
            *normalize(self.destination).split(),
            *sum([normalize(certificate).split() for certificate in self.certificates], [])
        }

    def set_data(self, data):
        self.total_power = data[0]
        self.price = data[1]

        self.panel_power = data[2]
        self.efficiency = data[3]
        self.tolerance = data[4]
        self.warranty_product = data[5]
        self.warranty_performance = data[6]

        self.company = data[7]
        self.mark = data[8]
        self.incoterm = data[9]
        self.made_in = data[10]
        self.origin = data[11]
        self.destination = data[12]
        self.certificates = data[13]
        self.panel_types = data[14]
        self.cells = data[15]
