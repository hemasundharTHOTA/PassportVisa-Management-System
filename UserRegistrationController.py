import random
import string
from flask import Flask, render_template, request, flash, session
from Project_PV.PassportVisa.models.pojo.UserDetails import UserDetails  # Ensure correct import
from Project_PV.PassportVisa.models.dao.serviceImpl import PassportVisaService  # Ensure correct import

class UserRegistrationController:
    def __init__(self, app: Flask):
        self.app = app
        self.PVServices = PassportVisaService()  # Using the correct service class

        # Define routes
        @app.route('/MainHome')
        def main_home():
            return render_template('MainHome.html')

        @app.route('/services')
        def services():
            return render_template('services.html')

        @app.route('/ContactPage')
        def contact_page():
            return render_template('ContactPage.html')

        @app.route('/registerForm')
        def register_form():
            return render_template('registerForm2.html')

        @app.route('/submitRegisterForm', methods=['POST'])
        def submit_register_form():
            # Get form data and create UserDetails object
            user_data = request.form.to_dict()
            user = UserDetails(**user_data)

            # Check for contact and email existence
            is_m_e_exist = self.PVServices.check_contact_and_email(user)

            # Handling various cases of already existing contact and email
            if is_m_e_exist.lower() == "contact":
                flash("Contact already exists.")
                return render_template('registerForm2.html', User=user, CONTACT="Already exists")
            elif is_m_e_exist.lower() == "email":
                flash("Email already exists.")
                return render_template('registerForm2.html', User=user, EMAIL="Email already exists.")
            elif is_m_e_exist.lower() == "both":
                flash("Contact number and email already exist.")
                return render_template('registerForm2.html', User=user, CONTACT="Contact already exists.",
                                       EMAIL="Email already exists.")
            elif is_m_e_exist.lower() == "none":
                # Creating new user and inserting into the database
                current_user = self.PVServices.create_new_user_and_insert(user)
                if current_user is None:
                    flash("Error inserting user.")
                    return render_template('BadRequestPage.html', Error="Insert error.")
                else:
                    # Generating a password for the new user
                    current_user.password = self.generate_password()
                    return render_template('ConfirmPage.html', user=current_user)
            else:
                flash("Unexpected error with mobile and email checks.")
                return render_template('BadRequestPage.html', Error="Mobile and Email check error.")

        def generate_password(self, length=8):
            """Generate a random password of a given length."""
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(length))
            return password
