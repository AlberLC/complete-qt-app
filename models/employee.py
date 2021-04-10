from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models import Base
from utilities.various import normalize


class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    position = Column(String)
    projects_type = Column(String)
    email = Column(Integer)
    phone = Column(Integer)
    linkedin = Column(Integer)
    observations = Column(String)

    language_id = Column(Integer, ForeignKey('language.id'))

    language = relationship('Language')

    @classmethod
    def get_headers(cls):
        return [header[:-3] if header.endswith('_id') else header for header in cls.__table__.columns.keys()]

    def __init__(self, *args):
        self.id = args[0]
        self.set_data(args[1:])

    @property
    def data(self):
        return [
            self.id,
            self.name,
            self.position,
            self.projects_type,
            self.email,
            self.phone,
            self.linkedin,
            self.observations,
            self.language.name if self.language else None
        ]

    def get_keywords(self, _):
        return {
            *normalize(self.name).split(),
            *normalize(self.position).split(),
            *normalize(self.projects_type).split(),
            *normalize(self.email).split(),
            *normalize(self.phone).split(),
            *normalize(self.linkedin).split(),
            *normalize(self.language).split(),
            *normalize(self.observations).split()
        }

    def set_data(self, data):
        self.name = data[0]
        self.position = data[1]
        self.projects_type = data[2]
        self.email = data[3]
        self.phone = data[4]
        self.linkedin = data[5]
        self.language = data[6]
        self.observations = data[7]
