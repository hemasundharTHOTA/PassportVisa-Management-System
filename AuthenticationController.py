from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_bcrypt import Bcrypt
from Project_PV.PassportVisa.models.dao.serviceImpl.PassportVisaService import PassportVisaService

class AuthenticationController:
    def __init__(self, app: Flask):
        self.app = app
        self.bcrypt = Bcrypt(app)
        self.PVServices = PassportVisaService()  # Instantiate your service class

        # Define routes
        @app.route('/LoginForm1')
        def login_form():
            return render_template('LoginForm.html', First="1")

        @app.route('/GettingContact', methods=['GET'])
        def get_contact():
            user_name = request.args.get('userName')
            contact_no = self.PVServices.get_contact_no(user_name)
            if contact_no == "ERROR":
                flash("Contact number fetching problem.")
                return render_template('BadRequestPage.html')
            elif contact_no == "NONE":
                flash("USER NOT FOUND")
                return render_template('LoginForm.html', userName=user_name)
            else:
                return render_template('LoginForm.html', ContactNo=contact_no, userName=user_name)

        @app.route('/CheckPassword', methods=['POST'])
        def check_password():
            password = request.form.get('password')
            user_name = request.form.get('userName')
            user = self.PVServices.get_user_by_id(user_name)
            if user is None:
                flash("User name not found.")
                return render_template('LoginForm.html', userName=user_name)
            else:
                if self.bcrypt.check_password_hash(user.get_password(), password):
                    session['LoginUser'] = user.get_user_name()  # Store user details in session
                    session['Name'] = user.get_first_name()
                    return redirect(url_for('main_login_page'))  # Ensure this route exists
                else:
                    flash("Wrong password.")
                    return render_template('LoginForm.html', userName=user_name)

        @app.route('/ForgotPassword1')
        def forgot_password():
            return render_template('forgotpassword.html')

        @app.route('/GetHintQuestion', methods=['GET'])
        def get_hint_question():
            user_id = request.args.get('userid')
            user = self.PVServices.get_user_by_id(user_id)
            if user is None:
                flash("User name not found.")
            return render_template('forgotpassword.html', userid=user_id, User=user)

        @app.route('/submitForgotForm', methods=['POST'])
        def submit_forgot_form():
            user_id = request.form.get('userid')
            hint_answer = request.form.get('hintanswer')
            confirm_password = request.form.get('confirmpassword')
            user = self.PVServices.get_user_by_id(user_id)
            if user is None:
                flash(f"User name {user_id} not found.")
                return render_template('forgotpassword.html', userid=user_id)
            if user.get_hint_answer() == hint_answer:
                encrypted_password = self.bcrypt.generate_password_hash(confirm_password).decode('utf-8')
                status = self.PVServices.update_password(user_id, encrypted_password)
                if status == "Success":
                    flash(f"User name - {user_id} updated successfully.")
                else:
                    flash("Updating password failed. Please try again.")
            else:
                flash("Wrong hint answer.")
            return render_template('forgotpassword.html', userid=user_id, User=user)

        @app.route('/UpdatePassword')
        def update_password():
            return render_template('UpdatePassword.html')

        @app.route('/UpdatePasswordSubmit', methods=['POST'])
        def update_password_submit():
            user_id = request.form.get('userid')
            new_password = request.form.get('newpassword')
            encrypted_password = self.bcrypt.generate_password_hash(new_password).decode('utf-8')
            status = self.PVServices.update_password(user_id, encrypted_password)
            if status == "Success":
                flash("Password updated successfully.")
            else:
                flash("Password updating failed. Please try again.")
            return render_template('UpdatePassword.html')
