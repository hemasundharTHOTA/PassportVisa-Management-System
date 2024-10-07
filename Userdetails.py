from sqlalchemy import create_engine, Column, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class UserDetails(Base):
    __tablename__ = 'User_Details5'

    first_name = Column('FirstName', String(100))
    sur_name = Column('SurName', String(100))
    dob = Column('DOB', Date)
    address = Column('Address', String(255))
    contact_no = Column('ContactNo', String(20))
    email = Column('Email', String(100))
    qualification = Column('Qualification', String(100))
    gender = Column('Gender', String(10))
    apply_type = Column('ApplyType', String(50))
    hint_question = Column('HintQuesion', String(255))
    hint_answer = Column('HintAnswer', String(255))
    citizen_type = Column('CitizenType', String(50))
    user_name = Column('UserName', String(50), primary_key=True)
    password = Column('Password', String(100))

    def __init__(self, first_name, sur_name, dob, address, contact_no, email, qualification, gender, apply_type,
                 hint_question, hint_answer, citizen_type, user_name, password):
        self.first_name = first_name
        self.sur_name = sur_name
        self.dob = dob
        self.address = address
        self.contact_no = contact_no
        self.email = email
        self.qualification = qualification
        self.gender = gender
        self.apply_type = apply_type
        self.hint_question = hint_question
        self.hint_answer = hint_answer
        self.citizen_type = citizen_type
        self.user_name = user_name
        self.password = password

    def __repr__(self):
        return (f"<UserDetails(first_name={self.first_name}, sur_name={self.sur_name}, dob={self.dob}, "
                f"address={self.address}, contact_no={self.contact_no}, email={self.email}, "
                f"qualification={self.qualification}, gender={self.gender}, apply_type={self.apply_type}, "
                f"hint_question={self.hint_question}, hint_answer={self.hint_answer}, "
                f"citizen_type={self.citizen_type}, user_name={self.user_name}, password={self.password})>")

