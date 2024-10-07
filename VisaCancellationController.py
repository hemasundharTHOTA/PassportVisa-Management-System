# File: ProjectPV/PassportVisa/controllers/visa_cancellation_controller.py

from flask import Flask, render_template, request, flash
from Project_PV.PassportVisa.models.dao.serviceImpl import PassportVisaService  # Ensure correct import
from Project_PV.PassportVisa.models.pojo.visa_cancel_form import VisaCancelForm  # Ensure correct import

class VisaCancellationController:
    def __init__(self, app: Flask):
        self.app = app
        self.PVServices = PassportVisaService()  # Using the correct service class

        # Define routes
        @app.route('/VisaCancelForm')
        def visa_cancel_form():
            return render_template('VisaCancellation.html')

        @app.route('/SubmitingVisaCancelation', methods=['POST'])
        def submit_visa_cancelation():
            # Get form data and create VisaCancelForm object
            form_data = request.form.to_dict()
            vc = VisaCancelForm(**form_data)

            # Fetch user details
            user = self.PVServices.get_user_by_id(vc.user_name)
            if user is None:
                flash("User Not Found")
                return render_template('VisaCancellation.html', Error="User Not Found")

            # Fetch passport details
            p_details = self.PVServices.get_p_details(vc.passport_number)
            if p_details is None:
                flash("Passport Details Not Found")
                return render_template('VisaCancellation.html', Error="Passport Details Not Found")

            # Fetch visa details
            v_details = self.PVServices.get_v_details_by_visa_id(vc.visa_number)
            if v_details is None:
                flash(f"No Visa Found On - {vc.visa_number}")
                return render_template('VisaCancellation.html', Error=f"No Visa Found On - {vc.visa_number}")

            # Check if the visa corresponds to the passport number
            if v_details.passport_id.lower() == vc.passport_number.lower():
                # Ensure cancellation date is between issue date and expiry date
                if vc.date_of_cancel > v_details.issue_date and vc.date_of_cancel < v_details.expiry_date:
                    # Attempt to cancel the visa
                    status = self.PVServices.cancel_visa(v_details.visa_id, vc.date_of_cancel)
                    if status is None:
                        flash("Visa Not Cancelled")
                        return render_template('BadRequestPage.html', Error="Visa Not Cancelled")
                    else:
                        # Calculate charges for the cancellation
                        reg_fee = self.PVServices.get_amount(v_details.occupation, v_details.country)
                        cancel_charges = self.PVServices.get_cancel_charges(v_details.occupation, reg_fee,
                                                                             vc.date_of_cancel, v_details.expiry_date)
                        return render_template('VisaCancellationPayment.html', VDetails=v_details,
                                               VID=v_details.visa_id, Amount=cancel_charges,
                                               Message="Visa Cancelled Successfully")
                else:
                    flash(f"No Active Visas To Cancel on {vc.date_of_cancel}")
                    return render_template('VisaCancellation.html',
                                           Error=f"No Active Visas To Cancel on {vc.date_of_cancel}")
            else:
                flash(f"No Visa Found On Passport - {vc.passport_number} with {vc.visa_number}")
                return render_template('VisaCancellation.html',
                                       Error=f"No Visa Found On Passport - {vc.passport_number} with {vc.visa_number}")
