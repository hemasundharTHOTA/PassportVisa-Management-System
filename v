from sqlalchemy import create_engine, Column, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Passport(Base):
    __tablename__ = 'Passport_Prt5'

    passport_id = Column('PassportId', String(50), primary_key=True)
    # Define other fields according to your Passport class here


class Visa(Base):
    __tablename__ = 'Visa_Prt5'

    visa_id = Column('VisaId', String(50), primary_key=True)
    user_name = Column('UserName', String(50))
    country = Column('Country', String(100))
    occupation = Column('Occupation', String(100))
    passport_id = Column('PassportId', String(50), ForeignKey('Passport_Prt5.PassportId'))
    expiry_date = Column('ExpiryDate', Date)
    issue_date = Column('IssueDate', Date)

    passport = relationship("Passport", back_populates="visas")

    def __init__(self, visa_id, user_name, country, occupation, passport, expiry_date, issue_date):
        self.visa_id = visa_id
        self.user_name = user_name
        self.country = country
        self.occupation = occupation
        self.passport = passport
        self.expiry_date = expiry_date
        self.issue_date = issue_date

    def __repr__(self):
        return (f"<Visa(visa_id={self.visa_id}, user_name={self.user_name}, country={self.country}, "
                f"occupation={self.occupation}, passport_id={self.passport_id}, "
                f"expiry_date={self.expiry_date}, issue_date={self.issue_date})>")


