from flask import Flask, jsonify, request, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Dummy service class to mimic the Java service
class PassportVisaServices:
    def get_p_details(self, passport_id):
        # Mock implementation
        return {"passport_id": passport_id, "name": "John Doe"} if passport_id == "123" else None

    def get_all_passports_by_username(self, username):
        # Mock implementation
        return [{"passport_id": "123", "name": "John Doe"}, {"passport_id": "456", "name": "Jane Smith"}] if username == "john_doe" else None

services = PassportVisaServices()

@app.route('/GetPDetaislByPassportId/<string:passport_id>', methods=['GET'])
def get_p_details(passport_id):
    pd = services.get_p_details(passport_id)
    if pd is None:
        return jsonify({"error": "Passport Not Found"}), 404
    else:
        return jsonify(pd), 200

@app.route('/GetAllPassportsByUserName/<string:user_name>', methods=['GET'])
def get_all_passports_by_username(user_name):
    p_list = services.get_all_passports_by_username(user_name)
    if p_list is None:
        return jsonify({"error": "NOT FETCH"}), 501
    else:
        return jsonify(p_list), 200

if __name__ == '__main__':
    app.run(debug=True)
