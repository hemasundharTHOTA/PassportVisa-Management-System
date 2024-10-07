# File: ProjectPV/PassportVisa/services/passport_visa_service.py

from typing import Optional
from Project_PV.PassportVisa.models.pojo import UserDetails, Passport, VDetails
from Project_PV.PassportVisa.models.dao import PassportDAO, VisaDAO

class PassportVisaService:
    def __init__(self):
        self.passport_dao = PassportDAO()
        self.visa_dao = VisaDAO()

    def get_user_by_id(self, user_id: str) -> Optional[UserDetails]:
        return self.passport_dao.find_user_by_id(user_id)

    def get_contact_no(self, user_name: str) -> str:
        user = self.get_user_by_id(user_name)
        return user.get_contact_no() if user else "NONE"

    def update_password(self, user_id: str, new_password: str) -> str:
        return self.passport_dao.update_password(user_id, new_password)

    def get_passport_details(self, passport_id: str) -> Optional[Passport]:
        return self.passport_dao.find_passport_by_id(passport_id)

    def get_visa_details(self, visa_id: str) -> Optional[VDetails]:
        return self.visa_dao.find_visa_by_id(visa_id)

    def create_passport(self, passport: Passport) -> str:
        return self.passport_dao.save_passport(passport)

    def create_visa(self, visa: VDetails) -> str:
        return self.visa_dao.save_visa(visa)

    def cancel_visa(self, visa_id: str) -> str:
        return self.visa_dao.cancel_visa(visa_id)
