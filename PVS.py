from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from typing import List, Dict, Optional


# Define Models
class UserDetails(models.Model):
    username = models.CharField(max_length=255, primary_key=True)
    contact_no = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    # Add other fields as necessary

class Passport(models.Model):
    passport_id = models.CharField(max_length=255, primary_key=True)
    user_name = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    issued_date = models.DateField()
    expiry_date = models.DateField()
    book_type = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    # Add other fields as necessary

class Visa(models.Model):
    visa_id = models.CharField(max_length=255, primary_key=True)
    passport = models.ForeignKey(Passport, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()
    # Add other fields as necessary


# Define Service Class
class PassportVisaService:

    def is_contact_exist(self, mobile: str) -> bool:
        return UserDetails.objects.filter(contact_no=mobile).exists()

    def is_email_exist(self, email: str) -> bool:
        return UserDetails.objects.filter(email=email).exists()

    def no_of_users(self) -> int:
        return UserDetails.objects.count()

    def insert_user(self, user: UserDetails) -> UserDetails:
        user.save()
        return user

    def get_contact_no(self, user_name: str) -> Optional[str]:
        try:
            user = UserDetails.objects.get(username=user_name)
            return user.contact_no
        except ObjectDoesNotExist:
            return None

    def check_password(self, user_name: str, password: str) -> Optional[UserDetails]:
        try:
            return UserDetails.objects.get(username=user_name, password=password)
        except ObjectDoesNotExist:
            return None

    def get_by_user_name(self, user_name: str) -> Optional[UserDetails]:
        try:
            return UserDetails.objects.get(username=user_name)
        except ObjectDoesNotExist:
            return None

    def update_password(self, user_name: str, confirm_password: str) -> Optional[str]:
        try:
            user = UserDetails.objects.get(username=user_name)
            user.password = confirm_password
            user.save()
            return "Password Updated"
        except ObjectDoesNotExist:
            return None

    def get_passport_by_user_name(self, user_name: str) -> Optional[Passport]:
        try:
            return Passport.objects.get(user_name__username=user_name)
        except ObjectDoesNotExist:
            return None

    def save_passport(self, passport: Passport) -> str:
        passport.save()
        return "Passport Saved"

    def get_no_of_passports(self) -> int:
        return Passport.objects.count()

    def get_passport_id_by_user_name(self, user_name: str) -> Optional[str]:
        try:
            passport = Passport.objects.filter(user_name__username=user_name).latest('issued_date')
            return passport.passport_id
        except ObjectDoesNotExist:
            return None

    def get_p_details(self, passport_id: str) -> Optional[Dict]:
        try:
            passport = Passport.objects.get(passport_id=passport_id)
            visas = Visa.objects.filter(passport=passport)
            visa_countries = [visa.country for visa in visas]
            return {
                "passport_id": passport.passport_id,
                "user_name": passport.user_name.username,
                "book_type": passport.book_type,
                "pin": passport.pin,
                "city": passport.city,
                "country": passport.country,
                "service_type": passport.service_type,
                "expiry_date": passport.expiry_date,
                "issue_date": passport.issued_date,
                "state": passport.state,
                "visas": visa_countries
            }
        except ObjectDoesNotExist:
            return None

    def get_visas_list_by_passport_id(self, passport_id: str) -> List[Dict]:
        visas = Visa.objects.filter(passport__passport_id=passport_id)
        return [{
            "passport_id": visa.passport.passport_id,
            "user_name": visa.user_name,
            "country": visa.country,
            "occupation": visa.occupation,
            "issue_date": visa.issue_date,
            "expiry_date": visa.expiry_date,
            "visa_id": visa.visa_id
        } for visa in visas]

    def save_visa(self, passport_id: str, visa: Visa) -> Optional[str]:
        try:
            passport = Passport.objects.get(passport_id=passport_id)
            visa.passport = passport
            visa.save()
            return visa.visa_id
        except ObjectDoesNotExist:
            return None

    def get_v_details_by_visa_id(self, visa_id: str) -> Optional[Dict]:
        try:
            visa = Visa.objects.get(visa_id=visa_id)
            return {
                "visa_id": visa_id,
                "user_name": visa.user_name,
                "country": visa.country,
                "occupation": visa.occupation,
                "passport_id": visa.passport.passport_id,
                "expiry_date": visa.expiry_date,
                "issue_date": visa.issue_date
            }
        except ObjectDoesNotExist:
            return None

    def no_of_visas(self) -> int:
        return Visa.objects.count()

    def get_passport_id_within_visa_issue_range(self, user_name: str, visa_issue_date: str) -> Optional[str]:
        visa_issue_date = parse_date(visa_issue_date)
        passports = Passport.objects.filter(user_name__username=user_name)
        for passport in passports:
            if passport.issued_date < visa_issue_date < passport.expiry_date:
                return passport.passport_id
        return None

    def cancel_visa(self, visa_id: str, cancel_date: str) -> str:
        try:
            visa = Visa.objects.get(visa_id=visa_id)
            visa.expiry_date = parse_date(cancel_date)
            visa.save()
            return "Cancelled"
        except ObjectDoesNotExist:
            return "Not Found"

    def get_all_passports_by_username(self, user_name: str) -> List[Dict]:
        passports = Passport.objects.filter(user_name__username=user_name)
        return [{
            "user_name": passport.user_name.username,
            "passport_id": passport.passport_id,
            "issue_date": passport.issued_date,
            "expiry_date": passport.expiry_date
        } for passport in passports]

    def get_all_v_details_by_user_name(self, user_name: str) -> List[Dict]:
        visas = Visa.objects.filter(user_name=user_name)
        return [{
            "user_name": visa.user_name,
            "passport_id": visa.passport.passport_id,
            "visa_id": visa.visa_id,
            "issue_date": visa.issue_date,
            "expiry_date": visa.expiry_date,
            "country": visa.country
        } for visa in visas]
