from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
from typing import List

app = Flask(__name__)
CORS(app)  # Enable CORS


# Dummy service class to simulate your business logic
class PassportVisaServices:
    def get_visas_list_by_passport_id(self, passport_id: str) -> List[dict]:
        # Mock implementation
        if passport_id == "valid_passport_id":
            return [{"visa_id": "visa1", "details": "details1"}, {"visa_id": "visa2", "details": "details2"}]
        else:
            raise ValueError("PassportId Not Found")

    def save_visa(self, passport_id: str, visa: dict) -> str:
        # Mock implementation
        if passport_id == "valid_passport_id":
            return "new_visa_id"
        else:
            return None

    def get_v_details_by_visa_id(self, visa_id: str) -> dict:
        # Mock implementation
        if visa_id == "valid_visa_id":
            return {"visa_id": visa_id, "details": "Visa Details"}
        else:
            return None

    def no_of_visas(self) -> int:
        # Mock implementation
        return 100

    def get_passport_id_with_in_visa_issue_range(self, user_name: str, visa_issue_date: str) -> str:
        # Mock implementation
        if user_name == "valid_user" and visa_issue_date == "2024-09-10":
            return "passport_id_within_range"
        else:
            return None

    def get_all_v_details_by_user_name(self, user_name: str) -> List[dict]:
        # Mock implementation
        if user_name == "valid_user":
            return [{"visa_id": "visa1", "details": "details1"}, {"visa_id": "visa2", "details": "details2"}]
        else:
            return None


services = PassportVisaServices()


@app.route('/GetVisasListByPassportId/<string:passport_id>', methods=['GET'])
def get_visas_list_by_passport_id(passport_id):
    try:
        visas = services.get_visas_list_by_passport_id(passport_id)
        return jsonify(visas), 200
    except ValueError:
        return jsonify("PassportId Not Found"), 404


@app.route('/SaveVisa/<string:passport_id>', methods=['POST'])
def save_visa(passport_id):
    visa = request.json
    new_visa_id = services.save_visa(passport_id, visa)
    if new_visa_id is None:
        return jsonify("Visa Not Created."), 501  # Not Implemented
    else:
        return jsonify(new_visa_id), 200


@app.route('/GetVDetailsByVisaId/<string:visa_id>', methods=['GET'])
def get_v_details_by_visa_id(visa_id):
    v_details = services.get_v_details_by_visa_id(visa_id)
    if v_details is None:
        return jsonify(f"Visa Not Found By {visa_id}"), 404
    else:
        return jsonify(v_details), 200


@app.route('/NoOfVisas', methods=['GET'])
def no_of_visas():
    count = services.no_of_visas()
    return jsonify(count), 200


@app.route('/GetPassportIdWithInVisaIssueDate/<string:user_name>/<string:visa_issue_date>', methods=['GET'])
def get_passport_id_within_visa_issue_date(user_name, visa_issue_date):
    try:
        # Convert the visa_issue_date to the correct format
        datetime.strptime(visa_issue_date, '%Y-%m-%d')  # Validate date format
    except ValueError:
        return jsonify("Invalid date format"), 400

    passport_id = services.get_passport_id_with_in_visa_issue_range(user_name, visa_issue_date)
    if passport_id is None:
        return jsonify("No Passport On Visa IssueDate"), 404
    else:
        return jsonify(passport_id), 200


@app.route('/GetAllVisasByUserName/<string:user_name>', methods=['GET'])
def get_all_visas_by_user_name(user_name):
    visas = services.get_all_v_details_by_user_name(user_name)
    if visas is None:
        return jsonify("NOT FETCH"), 501  # Not Implemented
    else:
        return jsonify(visas), 200


if __name__ == '__main__':
    app.run(debug=True)
