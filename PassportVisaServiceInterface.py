# File: ProjectPV/PassportVisa/interfaces/passport_visa_interface.py

from abc import ABC, abstractmethod
from Project_PV.PassportVisa.models.pojo.UserDetails import UserDetails
from Project_PV.PassportVisa.models.pojo.Passport import Passport
from Project_PV.PassportVisa.models.pojo.Visa import VDetails

class PassportVisaServiceInterface(ABC):

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> UserDetails:
        return UserDetails()  # Replace with actual retrieval logic

    @abstractmethod
    def get_contact_no(self, user_name: str) -> str:
        return "1234567890"  # Replace with actual retrieval logic

    @abstractmethod
    def update_password(self, user_id: str, new_password: str) -> str:
        return "Password updated"  # Replace with actual update logic

    @abstractmethod
    def get_passport_details(self, passport_id: str) -> Passport:
        return Passport()  # Replace with actual retrieval logic

    @abstractmethod
    def get_visa_details(self, visa_id: str) -> VDetails:
        return VDetails()  # Replace with actual retrieval logic

    @abstractmethod
    def create_passport(self, passport: Passport) -> str:
        return "Passport created"  # Replace with actual creation logic

    @abstractmethod
    def create_visa(self, visa: VDetails) -> str:
        return "Visa created"  # Replace with actual creation logic

    @abstractmethod
    def cancel_visa(self, visa_id: str) -> str:
        return "Visa canceled"  # Replace with actual cancellation logic
