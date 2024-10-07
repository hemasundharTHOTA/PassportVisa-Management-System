# File: ProjectPV/PassportVisa/controllers/passport_controller.py

from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime
from Project_PV.PassportVisa.models.pojo.Passport import    Passport
from Project_PV.PassportVisa.models.dao.serviceImpl import PassportVisaService  # Ensure correct import

class PassportController:
    def __init__(self, app: Flask):
        self.app = app
        self.PVServices = PassportVisaService()  # Instantiate the service

        @app.route('/SubmitPassport', methods=['POST'])
        def submit_passport():
            p = request.form.to_dict()  # Convert form data to dictionary
            passport = Passport(**p)  # Create Passport object

            user = self.PVServices.get_user_by_id(passport.userName)  # Ensure method name matches your service
            if user is None:
                flash("Please enter a valid username.")
                return render_template('PassportApplicationForm.html')

            user_dob = user.dob
            is_eligible = self.PVServices.check_age(user_dob, passport.issueDate)  # Ensure this method exists
            if not is_eligible:
                flash("Date of apply must be after your date of birth.")
                return render_template('PassportApplicationForm.html')

            user_passport_id = self.PVServices.get_passport_id_by_user_name(passport.userName)
            if user_passport_id is None:
                passport_id = self.PVServices.save_new_passport(passport)  # Ensure method name matches
                if passport_id is None:
                    flash("Passport not created. Network or server problem.")
                    return render_template('BadRequestPage.html')
                else:
                    flash("Passport created successfully.")
                    p_details = self.PVServices.get_p_details(passport_id)  # Ensure method name matches
                    if p_details is not None:
                        amount = "2500/-" if passport.serviceType.lower() == "normal" else "5000/-"
                        return render_template('Payment.html',
                                               PDetails=p_details,
                                               Amount=amount,
                                               PID=p_details.passportId,
                                               EDate=p_details.expiryDate)
                    else:
                        flash("Passport details not fetched.")
                        return render_template('BadRequestPage.html')
            else:
                flash(f"User - {passport.userName} already has an existing passport.")
                p_details = self.PVServices.get_p_details(user_passport_id)
                return render_template('PassportApplicationForm.html',
                                       PID=f"Your existing passport ID: {p_details.passportId}")

        @app.route('/Re-PassportForm')
        def re_passport_form():
            return render_template('PassportRenewal.html')

        @app.route('/SubmitRe-PassportForm', methods=['POST'])
        def submit_re_passform():
            p = request.form.to_dict()
            passport = Passport(**p)
            user = self.PVServices.get_user_by_id(passport.userName)
            if user is None:
                flash("Please enter a valid username.")
                return render_template('PassportRenewal.html')

            passport_id = self.PVServices.get_passport_id_by_user_name(passport.userName)
            if passport_id is None:
                flash(f"User - {passport.userName} does not have a passport.")
                return render_template('PassportRenewal.html')

            expiry_date = self.PVServices.get_p_details(passport_id).expiryDate
            if expiry_date < passport.issueDate:
                latest_pid = self.PVServices.save_new_passport(passport)
                if latest_pid is None:
                    flash("Re-passport not created.")
                    return render_template('PassportRenewal.html')
                else:
                    latest_p_details = self.PVServices.get_p_details(latest_pid)
                    amount = "2500/-" if passport.serviceType.lower() == "normal" else "5000/-"
                    return render_template('Payment.html',
                                           PDetails=latest_p_details,
                                           Amount=amount,
                                           PID=latest_p_details.passportId,
                                           EDate=latest_p_details.expiryDate)
            else:
                flash("Your passport has not expired, so you can't apply for renewal.")
                return render_template('PassportRenewal.html')
