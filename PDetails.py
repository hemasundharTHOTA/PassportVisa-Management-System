from typing import List, Optional
from datetime import date


class PDetails:
    def __init__(self, passport_id: str, country: str, state: str, city: str, pin: str,
                 service_type: str, book_type: str, issue_date: date, expiry_date: date,
                 user_name: str, visas: List[str]):
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

    def get_passport_id(self) -> str:
        return self.passport_id

    def set_passport_id(self, passport_id: str):
        self.passport_id = passport_id

    def get_country(self) -> str:
        return self.country

    def set_country(self, country: str):
        self.country = country

    def get_state(self) -> str:
        return self.state

    def set_state(self, state: str):
        self.state = state

    def get_city(self) -> str:
        return self.city

    def set_city(self, city: str):
        self.city = city

    def get_pin(self) -> str:
        return self.pin

    def set_pin(self, pin: str):
        self.pin = pin

    def get_service_type(self) -> str:
        return self.service_type

    def set_service_type(self, service_type: str):
        self.service_type = service_type

    def get_book_type(self) -> str:
        return self.book_type

    def set_book_type(self, book_type: str):
        self.book_type = book_type

    def get_issue_date(self) -> date:
        return self.issue_date

    def set_issue_date(self, issue_date: date):
        self.issue_date = issue_date

    def get_expiry_date(self) -> date:
        return self.expiry_date

    def set_expiry_date(self, expiry_date: date):
        self.expiry_date = expiry_date

    def get_user_name(self) -> str:
        return self.user_name

    def set_user_name(self, user_name: str):
        self.user_name = user_name

    def get_visas(self) -> List[str]:
        return self.visas

    def set_visas(self, visas: List[str]):
        self.visas = visas
