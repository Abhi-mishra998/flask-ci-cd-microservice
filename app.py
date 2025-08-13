from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

# ----------------------------
# Logging Setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# Root Route

@app.route("/", methods=["GET"])
def home():
    return jsonify(message="Welcome to the Flask CI/CD Microservice!"), 200

# Health Check Route
@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="healthy"), 200
# Predict Route (Odd/Even Check)
# Supports both GET and POST

@app.route("/predict", methods=["GET", "POST"])
def predict():
    # If GET method → read from query params
    if request.method == "GET":
        number = request.args.get("number", type=int)
    else:
        # If POST method → read from JSON body
        data = request.get_json(silent=True)
        number = data.get("number") if data else None

    # Validation
    if number is None:
        logging.warning("Missing 'number' parameter.")
        return jsonify(error="Please provide a valid integer 'number'."), 400
    if not isinstance(number, int):
        logging.warning(f"Invalid type for 'number': {type(number)}")
        return jsonify(error="'number' must be an integer."), 400

    # Odd/Even logic
    prediction = "even" if number % 2 == 0 else "odd"
    logging.info(f"Prediction request for {number}: {prediction}")

    return jsonify(number=number, prediction=prediction), 200

# Main Entry

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

