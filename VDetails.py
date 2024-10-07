from typing import List, Optional
from datetime import date


class VDetails:
    def __init__(self, visa_id: str, user_name: str, country: str, occupation: str,
                 passport_id: str, expiry_date: date, issue_date: date):
        self._visa_id = visa_id
        self._user_name = user_name
        self._country = country
        self._occupation = occupation
        self._passport_id = passport_id
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

    def get_passport_id(self) -> str:
        return self._passport_id

    def set_passport_id(self, passport_id: str):
        self._passport_id = passport_id

    def get_expiry_date(self) -> date:
        return self._expiry_date

    def set_expiry_date(self, expiry_date: date):
        self._expiry_date = expiry_date

    def get_issue_date(self) -> date:
        return self._issue_date

    def set_issue_date(self, issue_date: date):
        self._issue_date = issue_date
