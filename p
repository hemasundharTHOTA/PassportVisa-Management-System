from sqlalchemy import Column, String, Date, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey

Base = declarative_base()


class Passport(Base):
    __tablename__ = 'Passport_Prt5'

    passport_id = Column(String, primary_key=True)
    country = Column(String)
    state = Column(String)
    city = Column(String)
    pin = Column(String)
    service_type = Column(String)
    book_type = Column(String)
    issue_date = Column(Date)
    expiry_date = Column(Date)
    user_name = Column(String)

    visas = relationship('Visa', back_populates='passport')

    def __init__(self, passport_id, country, state, city, pin, service_type, book_type, issue_date, expiry_date,
                 user_name, visas=[]):
        self.passport_id = passport_id
        self.country = country
        self.state = state
        self.city = city
        self.pin = pin
        self.service_type = service_type
        self.book_type = book_type
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.user_name = user_name
        self.visas = visas

    def __repr__(self):
        return f"<Passport(passport_id={self.passport_id}, country={self.country}, state={self.state}, city={self.city}, pin={self.pin}, service_type={self.service_type}, book_type={self.book_type}, issue_date={self.issue_date}, expiry_date={self.expiry_date}, user_name={self.user_name})>"


class Visa(Base):
    __tablename__ = 'Visa'

    id = Column(Integer, primary_key=True)
    passport_id = Column(String, ForeignKey('Passport_Prt5.passport_id'))
    passport = relationship('Passport', back_populates='visas')

    def __init__(self, id, passport_id):
        self.id = id
        self.passport_id = passport_id

    def __repr__(self):
        return f"<Visa(id={self.id}, passport_id={self.passport_id})>"



