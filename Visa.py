from typing import List, Optional
from datetime import date

from Project_PV.PassportVisa.models.pojo.Passport import Passport


class Visa:
    def __init__(self, visa_id: str, user_name: str, country: str, occupation: str,
                 passport: Optional[Passport], expiry_date: date, issue_date: date):
        self._visa_id = visa_id
        self._user_name = user_name
        self._country = country
        self._occupation = occupation
        self._passport = passport
        self._expiry_date = expiry_date
        self._issue_date = issue_date

    # Getters and Setters for each attribute
    def get_visa_id(self) -> str:
        return self._visa_id

    def set_visa_id(self, visa_id: str):
        self._visa_id = visa_id

    def get_user_name(self) -> str:
        return self._user_name

    def set_user_name(self, user_name: str):
        self._user_name = user_name

    def get_country(self) -> str:
        return self._country

    def set_country(self, country: str):
        self._country = country

    def get_occupation(self) -> str:
        return self._occupation

    def set_occupation(self, occupation: str):
        self._occupation = occupation

    def get_passport(self) -> Optional[Passport]:
        return self._passport

    def set_passport(self, passport: Optional[Passport]):
        self._passport = passport

    def get_expiry_date(self) -> date:
        return self._expiry_date

    def set_expiry_date(self, expiry_date: date):
        self._expiry_date = expiry_date

    def get_issue_date(self) -> date:
        return self._issue_date

    def set_issue_date(self, issue_date: date):
        self._issue_date = issue_date


class VisaCancelForm:
    def __init__(self, user_name: str, passport_number: str, visa_number: str, date_of_cancel: date):
        self._user_name = user_name
        self._passport_number = passport_number
        self._visa_number = visa_number
        self._date_of_cancel = date_of_cancel

    # Getters and Setters for each attribute
    def get_user_name(self) -> str:
        return self._user_name

    def set_user_name(self, user_name: str):
        self._user_name = user_name

    def get_passport_number(self) -> str:
        return self._passport_number

    def set_passport_number(self, passport_number: str):
        self._passport_number = passport_number

    def get_visa_number(self) -> str:
        return self._visa_number

    def set_visa_number(self, visa_number: str):
        self._visa_number = visa_number

    def get_date_of_cancel(self) -> date:
        return self._date_of_cancel

    def set_date_of_cancel(self, date_of_cancel: date):
        self._date_of_cancel = date_of_cancel


class VDetails:
    pass
