import joblib
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)
model = None
appHasRunBefore = False

@app.before_request
def init():
    global model
    global appHasRunBefore

    if not appHasRunBefore:
        # Load model from mounted path
        model = joblib.load("/mnt/models/spam_classifier.pkl")
        appHasRunBefore = True

@app.route("/v2/greet", methods=["GET"])
def status():
    global model
    if model is None:
        return "Flask Code: Model was not loaded."
    return "Flask Code: Model loaded successfully."

@app.route("/v2/predict", methods=["POST"])
def predict():
    global model
    if model is None:
        return jsonify({"error": "Model not loaded."})

    data = request.get_json()
    message = data.get("message", "")

    prediction = model.predict([message])[0]
    label = "spam" if prediction == 1 else "ham"

    return jsonify({
        "input": message,
        "prediction": int(prediction),
        "label": label
    })

if __name__ == "__main__":
    print("Starting Spam Classifier Serving...")
    init()
    app.run(host="0.0.0.0", port=9001, debug=True)
