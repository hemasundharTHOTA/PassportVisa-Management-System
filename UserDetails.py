from typing import List, Optional
from datetime import date


class UserDetails:
    def __init__(self, first_name: str, sur_name: str, dob: date, address: str, contact_no: str,
                 email: str, qualification: str, gender: str, apply_type: str,
                 hint_question: str, hint_answer: str, citizen_type: Optional[str] = "NA",
                 user_name: Optional[str] = "NA", password: Optional[str] = "NA"):
        self._first_name = first_name
        self._sur_name = sur_name
        self._dob = dob
        self._address = address
        self._contact_no = contact_no
        self._email = email
        self._qualification = qualification
        self._gender = gender
        self._apply_type = apply_type
        self._hint_question = hint_question
        self._hint_answer = hint_answer
        self._citizen_type = citizen_type
        self._user_name = user_name
        self._password = password

    # Getters and Setters for each attribute
    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, first_name: str):
        self._first_name = first_name

    def get_sur_name(self) -> str:
        return self._sur_name

    def set_sur_name(self, sur_name: str):
        self._sur_name = sur_name

    def get_dob(self) -> date:
        return self._dob

    def set_dob(self, dob: date):
        self._dob = dob

    def get_address(self) -> str:
        return self._address

    def set_address(self, address: str):
        self._address = address

    def get_contact_no(self) -> str:
        return self._contact_no

    def set_contact_no(self, contact_no: str):
        self._contact_no = contact_no

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str):
        self._email = email

    def get_qualification(self) -> str:
        return self._qualification

    def set_qualification(self, qualification: str):
        self._qualification = qualification

    def get_gender(self) -> str:
        return self._gender

    def set_gender(self, gender: str):
        self._gender = gender

    def get_apply_type(self) -> str:
        return self._apply_type

    def set_apply_type(self, apply_type: str):
        self._apply_type = apply_type

    def get_hint_question(self) -> str:
        return self._hint_question

    def set_hint_question(self, hint_question: str):
        self._hint_question = hint_question

    def get_hint_answer(self) -> str:
        return self._hint_answer

    def set_hint_answer(self, hint_answer: str):
        self._hint_answer = hint_answer

    def get_citizen_type(self) -> str:
        return self._citizen_type

    def set_citizen_type(self, citizen_type: str):
        self._citizen_type = citizen_type

    def get_user_name(self) -> str:
        return self._user_name

    def set_user_name(self, user_name: str):
        self._user_name = user_name

    def get_password(self) -> str:
        return self._password

    def set_password(self, password: str):
        self._password = password
