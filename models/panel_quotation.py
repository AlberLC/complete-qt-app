from sqlalchemy import Table, Column, String, Integer, Float, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from models import Base
from utilities.various import normalize

rel_panel_quotation_certificate = Table(
    'rel_panel_quotation_certificate',
    Base.metadata,
    Column('panel_quotation_id', Integer, ForeignKey('panel_quotation.id'), primary_key=True),
    Column('certificate_id', Integer, ForeignKey('certificate.id'), primary_key=True)
)


class PanelQuotation(Base):
    __tablename__ = 'panel_quotation'
    id = Column(Integer, primary_key=True, autoincrement=True)
    total_power = Column(Float, nullable=False)
    price = Column(Integer, nullable=False)
    date_quotation = Column(Date)
    date_validity = Column(Date)
    observations = Column(String)
    n_contacts = Column(Integer)

    panel_power = Column(Float, nullable=False)
    efficiency = Column(Float)
    tolerance = Column(Boolean)
    warranty_product = Column(Integer)
    warranty_performance = Column(Integer)

    company_id = Column(Integer, ForeignKey('company.id'), nullable=False)
    mark_id = Column(Integer, ForeignKey('mark.id'))
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    panel_type_id = Column(Integer, ForeignKey('panel_type.id'))
    cells_id = Column(Integer, ForeignKey('cells.id'))
    incoterm_id = Column(Integer, ForeignKey('incoterm.id'))
    made_in_id = Column(Integer, ForeignKey('place.id'))
    origin_id = Column(Integer, ForeignKey('place.id'))
    destination_id = Column(Integer, ForeignKey('place.id'))

    company = relationship('Company', back_populates='panel_quotations')
    mark = relationship('Mark')
    user = relationship('User')
    panel_type = relationship('PanelType')
    cells = relationship('Cells')
    incoterm = relationship('Incoterm')
    made_in = relationship('Place', foreign_keys=made_in_id)
    origin = relationship('Place', foreign_keys=origin_id)
    destination = relationship('Place', foreign_keys=destination_id)
    certificates = relationship('Certificate', secondary=rel_panel_quotation_certificate, backref='panel_quotations')

    def __init__(self, *args):
        self.id = args[0]
        self.set_data(args[1:])

    def get_keywords(self, my_strings):
        return {
            'panel',
            'panels',
            'paneles',
            *normalize(self.company).split(),
            *normalize(self.mark).split(),
            *normalize(self.observations).split(),
            *normalize(self.user).split(),
            *normalize(self.panel_type).split(),
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
        self.date_quotation = data[2]
        self.date_validity = data[3]
        self.observations = data[4]

        self.n_contacts = data[5]
        self.panel_power = data[6]
        self.efficiency = data[7]
        self.tolerance = data[8]
        self.warranty_product = data[9]
        self.warranty_performance = data[10]

        self.company = data[11]
        self.mark = data[12]
        self.user = data[13]
        self.panel_type = data[14]
        self.cells = data[15]
        self.incoterm = data[16]
        self.made_in = data[17]
        self.origin = data[18]
        self.destination = data[19]
        self.certificates = data[20]
