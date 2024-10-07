from typing import List, Optional
from datetime import date

class Passport:
    def __init__(self, user_name: str, country: str, state: str, city: str, pin: str,
                 service_type: str, book_type: str, issue_date: date, expiry_date: date,
                 passport_id: str, visas: List[str]):
        self._user_name = user_name
        self._country = country
        self._state = state
        self._city = city
        self._pin = pin
        self._service_type = service_type
        self._book_type = book_type
        self._issue_date = issue_date
        self._expiry_date = expiry_date
        self._passport_id = passport_id
        self._visas = visas

    # Getters and Setters for each attribute
    def get_user_name(self) -> str:
        return self._user_name

    def set_user_name(self, user_name: str):
        self._user_name = user_name

    def get_country(self) -> str:
        return self._country

    def set_country(self, country: str):
        self._country = country

    def get_state(self) -> str:
        return self._state

    def set_state(self, state: str):
        self._state = state

    def get_city(self) -> str:
        return self._city

    def set_city(self, city: str):
        self._city = city

    def get_pin(self) -> str:
        return self._pin

    def set_pin(self, pin: str):
        self._pin = pin

    def get_service_type(self) -> str:
        return self._service_type

    def set_service_type(self, service_type: str):
        self._service_type = service_type

    def get_book_type(self) -> str:
        return self._book_type

    def set_book_type(self, book_type: str):
        self._book_type = book_type

    def get_issue_date(self) -> date:
        return self._issue_date

    def set_issue_date(self, issue_date: date):
        self._issue_date = issue_date

    def get_expiry_date(self) -> date:
        return self._expiry_date

    def set_expiry_date(self, expiry_date: date):
        self._expiry_date = expiry_date

    def get_passport_id(self) -> str:
        return self._passport_id

    def set_passport_id(self, passport_id: str):
        self._passport_id = passport_id

    def get_visas(self) -> List[str]:
        return self._visas

    def set_visas(self, visas: List[str]):
        self._visas = visas









