# File: ProjectPV/PassportVisa/controllers/visa_controller.py

from flask import Flask, render_template, request, session, flash
from datetime import timedelta
from Project_PV.PassportVisa.models.pojo.Visa import Visa  # Ensure correct import
from Project_PV.PassportVisa.models.dao.serviceImpl import PassportVisaService  # Ensure correct import

class VisaController:
    def __init__(self, app: Flask):
        self.app = app
        self.PVServices = PassportVisaService()  # Using the correct service class

        # Define routes
        @app.route('/ApplyVisa')
        def apply_visa():
            return render_template('VisaApplication.html')

        @app.route('/SubmittingVisaForm', methods=['POST'])
        def submitting_visa_form():
            # Get form data and create Visa object
            form_data = request.form.to_dict()
            visa = Visa(**form_data)

            # Fetch user details by user name
            user = self.PVServices.get_user_by_id(visa.user_name)
            if user is None:
                flash("User name not found.")
                return render_template('VisaApplication.html', Error="User name not found.")

            # Add 10 days to the visa issue date
            visa.issue_date = visa.issue_date + timedelta(days=10)

            # Check for active passports within the visa issue date range
            passport_id = self.PVServices.get_passport_id_within_visa_issue_date_range(visa.user_name, visa.issue_date)
            if passport_id is None:
                flash(f"No active passport found on date {visa.issue_date}.")
                return render_template('VisaApplication.html', Error=f"No active passport found on date {visa.issue_date}.")

            # Fetch list of visas by passport ID
            VList = self.PVServices.get_visa_list_by_passport_id(passport_id)
            if VList is not None and len(VList) == 0:
                # Create a new visa
                VID = self.PVServices.save_new_visa(passport_id, visa)
                if VID is None:
                    flash("New visa not created.")
                    return render_template('BadRequestPage.html', Error="New visa not created.")

                vDetails = self.PVServices.get_v_details_by_visa_id(VID)
                if vDetails is None:
                    flash("Visa details not fetched.")
                    return render_template('BadRequestPage.html', Error="Visa details not fetched.")

                Amount = self.PVServices.get_amount(visa.occupation, visa.country)
                return render_template('VisaPayment.html', VDetails=vDetails, Amount=Amount,
                                       Country=vDetails.country, VID=vDetails.visa_id, EDate=vDetails.expiry_date)

            elif len(VList) > 0:
                # Check if visa eligibility for the country is valid
                check_country_visa_eligibility = self.PVServices.check_country_visa_eligibility(VList, visa)
                if check_country_visa_eligibility:
                    VID = self.PVServices.save_new_visa(passport_id, visa)
                    if VID is None:
                        flash("New visa not created.")
                        return render_template('BadRequestPage.html', Error="New visa not created.")

                    vDetails = self.PVServices.get_v_details_by_visa_id(VID)
                    if vDetails is None:
                        flash("Visa details not fetched.")
                        return render_template('BadRequestPage.html', Error="Visa details not fetched.")

                    Amount = self.PVServices.get_amount(visa.occupation, visa.country)
                    return render_template('VisaPayment.html', VDetails=vDetails, Amount=Amount,
                                           Country=vDetails.country, VID=vDetails.visa_id, EDate=vDetails.expiry_date)

                else:
                    flash(f"An active visa already exists for this country on date {visa.issue_date}.")
                    return render_template('VisaApplication.html',
                                           Error=f"An active visa already exists for this country on date {visa.issue_date}.")

            else:
                flash("Failed to fetch visa list.")
                return render_template('BadRequestPage.html', Error="Failed to fetch visa list.")

        @app.route('/myVisas')
        def get_all_visas_by_user_name():
            # Get the user name from the session
            user_name = session.get('UserName')

            # Fetch all visas by the user name
            VList = self.PVServices.get_all_visas_by_user_name(user_name)
            if VList is None:
                flash("No visas fetched.")
                return render_template('BadRequestPage.html', Error="No visas fetched.")

            return render_template('MyVisas.html', visas=VList)
