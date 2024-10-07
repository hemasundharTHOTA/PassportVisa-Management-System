from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS

# Dummy service class to simulate your business logic
class PassportVisaServices:
    def get_by_user_name(self, user_id):
        # Mock implementation
        return {"user_id": user_id, "name": "John Doe"} if user_id == "123" else None

    def is_contact_exist(self, contact):
        # Mock implementation
        return "True" if contact == "1234567890" else "False"

    def is_email_exist(self, email):
        # Mock implementation
        return "True" if email == "test@example.com" else "False"

    def no_of_users(self):
        # Mock implementation
        return 10

    def insert_user(self, user):
        # Mock implementation
        pass

    def get_contact_no(self, user_name):
        # Mock implementation
        return "1234567890" if user_name == "john_doe" else None

    def check_password(self, user_name, password):
        # Mock implementation
        if user_name == "john_doe" and password == "password":
            return {"user_name": user_name}
        else:
            raise Exception("Invalid credentials")

    def update_password(self, user_name, new_password):
        # Mock implementation
        return "Password Updated" if user_name == "john_doe" else None

    def get_passport_by_user_name(self, user_name):
        # Mock implementation
        return {"passport_id": "ABC123", "user_name": user_name} if user_name == "john_doe" else None

    def get_no_of_passports(self):
        # Mock implementation
        return 5

    def get_passport_id_by_user_name(self, user_name):
        # Mock implementation
        return "ABC123" if user_name == "john_doe" else None

    def save_passport(self, passport):
        # Mock implementation
        pass

services = PassportVisaServices()

@app.route('/getByUserId/<string:user_id>', methods=['GET'])
def get_by_id(user_id):
    user = services.get_by_user_name(user_id)
    if user is None:
        return jsonify({"error": "NOT FOUND"}), 500
    else:
        return jsonify(user), 200

@app.route('/CheckM_E/<string:contact>/<string:email>', methods=['GET'])
def check_m_e(contact, email):
    contact_exist = services.is_contact_exist(contact)
    email_exist = services.is_email_exist(email)
    if contact_exist == "True" and email_exist == "True":
        return jsonify("BOTH"), 200
    elif contact_exist == "True":
        return jsonify("CONTACT"), 200
    elif email_exist == "True":
        return jsonify("EMAIL"), 200
    else:
        return jsonify("NONE"), 200

@app.route('/NoOfUsers', methods=['GET'])
def no_of_users():
    count = services.no_of_users()
    return jsonify(count), 200

@app.route('/InsertUser', methods=['POST'])
def insert_user():
    user = request.json
    existing_user = services.get_by_user_name(user.get("user_name"))
    if existing_user is None:
        services.insert_user(user)
        return jsonify(user), 200
    else:
        return jsonify({"error": "Exist"}), 500

@app.route('/GetContactNo/<string:user_name>', methods=['GET'])
def get_contact_no(user_name):
    contact_no = services.get_contact_no(user_name)
    if contact_no is None:
        return jsonify("NONE"), 200
    else:
        return jsonify(contact_no), 200

@app.route('/CheckPassword/<string:user_name>/<string:password>', methods=['GET'])
def check_password(user_name, password):
    try:
        user = services.check_password(user_name, password)
        return jsonify(user), 200
    except Exception as e:
        return jsonify("NONE"), 404

@app.route('/UpdatePassword/<string:user_name>', methods=['PUT'])
def update_password(user_name):
    new_password = request.data.decode('utf-8')
    status = services.update_password(user_name, new_password)
    if status is None:
        return jsonify("User Not Found"), 404
    else:
        return jsonify(status), 200

@app.route('/GetPassportByUserName/<string:user_name>', methods=['GET'])
def get_passport_by_user_name(user_name):
    passport = services.get_passport_by_user_name(user_name)
    if passport is None:
        return jsonify("Passport Not Found"), 404
    else:
        return jsonify(passport), 200

@app.route('/NoOfPassports', methods=['GET'])
def no_of_passports():
    count = services.get_no_of_passports()
    return jsonify(count), 200

@app.route('/GetPassportId/<string:user_name>', methods=['GET'])
def get_passport_id_by_user_name(user_name):
    passport_id = services.get_passport_id_by_user_name(user_name)
    if passport_id is None:
        return jsonify("Passport Not Found"), 404
    else:
        return jsonify(passport_id), 200

@app.route('/SavePassport', methods=['POST'])
def save_passport():
    passport = request.json
    try:
        services.save_passport(passport)
        return jsonify(passport.get("passport_id")), 200
    except Exception as e:
        return jsonify("Not Passport Saved"), 500

if __name__ == '__main__':
    app.run(debug=True)
