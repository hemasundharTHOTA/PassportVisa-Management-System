from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS


# Dummy service class to simulate your business logic
class PassportVisaServices:
    def cancel_visa(self, visa_id, cancel_date):
        # Mock implementation
        # Here, cancel_date should be a string in 'YYYY-MM-DD' format
        if visa_id == "valid_visa_id":
            return "Cancelled"
        else:
            return "Not Cancelled"


services = PassportVisaServices()


@app.route('/VisaCancel/<string:visa_id>/<string:cancel_date>', methods=['PUT'])
def cancel_visa(visa_id, cancel_date):
    try:
        # Parse the cancel_date string to a datetime object
        cancel_date = datetime.strptime(cancel_date, '%Y-%m-%d').date()
    except ValueError:
        return jsonify("Invalid date format"), 400

    # Call the service method
    status = services.cancel_visa(visa_id, cancel_date)

    if status.lower() == "cancelled":
        return jsonify(status), 200
    else:
        return jsonify(status), 304  # 304 Not Modified


if __name__ == '__main__':
    app.run(debug=True)
