# File: ProjectPV/PassportVisa/controllers/main_controller.py

from flask import Flask, render_template, request, redirect, url_for, session, flash
from Project_PV.PassportVisa.models.dao.serviceImpl import PassportVisaService  # Ensure correct import


class MainController:
    def __init__(self, app: Flask):
        self.app = app
        self.PVServices = PassportVisaService()  # Instantiate the service

        # Define routes
        @app.route('/MainLogin')
        def main_login_page():
            return render_template('MainLoginPage.html')

        @app.route('/ApplyPassport')
        def apply_passport():
            return render_template('PassportApplicationForm.html')

        @app.route('/RenewalPassport')
        def renewal_passport():
            return render_template('RenewalPassport.html')

        @app.route('/CancellationVisa')
        def cancellation_visa():
            return render_template('CancellationVisa.html')

        @app.route('/Profile')
        def profile():
            user_name = session.get('UserName')
            if user_name is None:
                flash("User details not fetched.")
                return redirect(url_for('main_login_page'))  # Redirect to login if not authenticated

            user = self.PVServices.get_user_by_id(user_name)  # Ensure this method exists in your service
            if user is None:
                flash("User not found.")
                return render_template('BadRequestPage.html')
            return render_template('Profile.html', user=user)

        @app.route('/PassportServices')
        def passport_services():
            return render_template('PassportServicesPage.html')

        @app.route('/VisaServices')
        def visa_services():
            return render_template('VisaServicesPage.html')

        @app.route('/myPassports')
        def my_passports():
            user_name = session.get('UserName')
            if user_name is None:
                flash("User not authenticated.")
                return redirect(url_for('main_login_page'))  # Redirect to login if not authenticated

            p_list = self.PVServices.get_all_passports_by_user_name(
                user_name)  # Ensure this method exists in your service
            if p_list is None or not p_list:
                flash("No passports found.")
                return render_template('BadRequestPage.html')
            return render_template('MyPassports.html', passports=p_list)

        @app.route('/MoreDetails')
        def more_details():
            return render_template('MoreDetails.html')
