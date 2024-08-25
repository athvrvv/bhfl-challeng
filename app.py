from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    highest_lowercase = [max([x for x in alphabets if x.islower()], default="")]

    response = {
        "is_success": True,
        "user_id": "john_doe_17091999",  # Replace with actual data
        "email": "john@xyz.com",  # Replace with actual data
        "roll_number": "ABCD123",  # Replace with actual data
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": highest_lowercase
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Ensure this matches the port you're using
