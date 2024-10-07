from abc import ABC, abstractmethod
from typing import List
from datetime import date
from sqlalchemy import create_engine, Column, String, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Define the base class for SQLAlchemy models
Base = declarative_base()


# Define the models

class UserDetails(Base):
    __tablename__ = 'User_Details5'
    user_name = Column('UserName', String(50), primary_key=True)
    first_name = Column('FirstName', String(100))
    sur_name = Column('SurName', String(100))
    dob = Column('DOB', Date)
    address = Column('Address', String(255))
    contact_no = Column('ContactNo', String(15))
    email = Column('Email', String(100))
    qualification = Column('Qualification', String(100))
    gender = Column('Gender', String(10))
    apply_type = Column('ApplyType', String(50))
    hint_question = Column('HintQuestion', String(255))
    hint_answer = Column('HintAnswer', String(255))
    citizen_type = Column('CitizenType', String(50))
    password = Column('Password', String(100))


class Passport(Base):
    __tablename__ = 'Passport_Prt5'
    passport_id = Column('PassportId', String(50), primary_key=True)
    country = Column('Country', String(100))
    state = Column('State', String(100))
    city = Column('City', String(100))
    pin = Column('Pin', String(10))
    service_type = Column('ServiceType', String(50))
    book_type = Column('BookType', String(50))
    issue_date = Column('IssueDate', Date)
    expiry_date = Column('ExpiryDate', Date)
    user_name = Column('UserName', String(50), ForeignKey('User_Details5.UserName'))
    user = relationship('UserDetails')
    visas = relationship('Visa', back_populates='passport')


class Visa(Base):
    __tablename__ = 'Visa_Prt5'
    visa_id = Column('VisaId', String(50), primary_key=True)
    user_name = Column('UserName', String(50))
    country = Column('Country', String(100))
    occupation = Column('Occupation', String(100))
    passport_id = Column('PassportId', String(50), ForeignKey('Passport_Prt5.PassportId'))
    expiry_date = Column('ExpiryDate', Date)
    issue_date = Column('IssueDate', Date)
    passport = relationship('Passport', back_populates='visas')


# Define the interface

class IPassportVisa(ABC):

    @abstractmethod
    def get_by_user_name(self, user_name: str) -> UserDetails:
        pass

    @abstractmethod
    def is_contact_exist(self, mobile: str) -> str:
        pass

    @abstractmethod
    def is_email_exist(self, email: str) -> str:
        pass

    @abstractmethod
    def no_of_users(self) -> int:
        pass

    @abstractmethod
    def insert_user(self, user: UserDetails) -> UserDetails:
        pass

    @abstractmethod
    def get_contact_no(self, user_name: str) -> str:
        pass

    @abstractmethod
    def check_password(self, user_name: str, password: str) -> UserDetails:
        pass

    @abstractmethod
    def update_password(self, user_name: str, confirm_password: str) -> str:
        pass

    @abstractmethod
    def get_passport_by_user_name(self, user_name: str) -> Passport:
        pass

    @abstractmethod
    def save_passport(self, passport: Passport) -> str:
        pass

    @abstractmethod
    def get_no_of_passports(self) -> int:
        pass

    @abstractmethod
    def get_passport_id_by_user_name(self, user_name: str) -> str:
        pass

    @abstractmethod
    def get_p_details(self, user_name: str) -> 'PDetails':
        pass

    @abstractmethod
    def get_all_passports_by_username(self, user_name: str) -> List['PDetails']:
        pass

    @abstractmethod
    def get_visas_list_by_passport_id(self, passport_id: str) -> List['VDetails']:
        pass

    @abstractmethod
    def save_visa(self, passport_id: str, visa: Visa) -> str:
        pass

    @abstractmethod
    def get_v_details_by_visa_id(self, visa_id: str) -> 'VDetails':
        pass

    @abstractmethod
    def no_of_visas(self) -> int:
        pass

    @abstractmethod
    def get_passport_id_within_visa_issue_range(self, user_name: str, visa_issue_date: date) -> str:
        pass

    @abstractmethod
    def get_all_v_details_by_user_name(self, user_name: str) -> List['VDetails']:
        pass

    @abstractmethod
    def cancel_visa(self, visa_id: str, cancel_date: date) -> str:
        pass


# Implement the service class

class PassportVisaService(IPassportVisa):

    def __init__(self, session):
        self.session = session

    def get_by_user_name(self, user_name: str) -> UserDetails:
        return self.session.query(UserDetails).filter_by(user_name=user_name).first()

    def is_contact_exist(self, mobile: str) -> str:
        user = self.session.query(UserDetails).filter_by(contact_no=mobile).first()
        return "Exists" if user else "Not Exists"

    def is_email_exist(self, email: str) -> str:
        user = self.session.query(UserDetails).filter_by(email=email).first()
        return "Exists" if user else "Not Exists"

    def no_of_users(self) -> int:
        return self.session.query(UserDetails).count()

    def insert_user(self, user: UserDetails) -> UserDetails:
        self.session.add(user)
        self.session.commit()
        return user

    def get_contact_no(self, user_name: str) -> str:
        user = self.session.query(UserDetails).filter_by(user_name=user_name).first()
        return user.contact_no if user else None

    def check_password(self, user_name: str, password: str) -> UserDetails:
        return self.session.query(UserDetails).filter_by(user_name=user_name, password=password).first()

    def update_password(self, user_name: str, confirm_password: str) -> str:
        user = self.session.query(UserDetails).filter_by(user_name=user_name).first()
        if user:
            user.password = confirm_password
            self.session.commit()
            return "Password updated"
        return "User not found"

    def get_passport_by_user_name(self, user_name: str) -> Passport:
        return self.session.query(Passport).filter_by(user_name=user_name).first()

    def save_passport(self, passport: Passport) -> str:
        self.session.add(passport)
        self.session.commit()
        return "Passport saved"

    def get_no_of_passports(self) -> int:
        return self.session.query(Passport).count()

    def get_passport_id_by_user_name(self, user_name: str) -> str:
        passport = self.session.query(Passport).filter_by(user_name=user_name).first()
        return passport.passport_id if passport else None

    def get_p_details(self, user_name: str) -> 'PDetails':
        # You need to implement this method based on your requirements
        pass

    def get_all_passports_by_username(self, user_name: str) -> List['PDetails']:
        # You need to implement this method based on your requirements
        pass

    def get_visas_list_by_passport_id(self, passport_id: str) -> List['VDetails']:
        # You need to implement this method based on your requirements
        pass

    def save_visa(self, passport_id: str, visa: Visa) -> str:
        self.session.add(visa)
        self.session.commit()
        return "Visa saved"

    def get_v_details_by_visa_id(self, visa_id: str) -> 'VDetails':
        # You need to implement this method based on your requirements
        pass

    def no_of_visas(self) -> int:
        return self.session.query(Visa).count()

    def get_passport_id_within_visa_issue_range(self, user_name: str, visa_issue_date: date) -> str:
        # You need to implement this method based on your requirements
        pass

    def get_all_v_details_by_user_name(self, user_name: str) -> List['VDetails']:
        # You need to implement this method based on your requirements
        pass

    def cancel_visa(self, visa_id: str, cancel_date: date) -> str:
        visa = self.session.query(Visa).filter_by(visa_id=visa_id).first()
        if visa:
            visa.expiry_date = cancel_date
            self.session.commit()
            return "Visa cancelled"
        return "Visa not found"


# Setup SQLAlchemy engine and session
engine = create_engine('sqlite:///example.db')  # Use your database URL
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Example usage
service = PassportVisaService(session)
