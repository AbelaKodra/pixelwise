from flask import Flask, jsonify, request
from models.predict import predict_digit

app = Flask(__name__)

@app.route("/")
def home():
	return jsonify({
		"service": "PixelWise API",
		"status": "running"
	})


@app.route("/predict", methods=["GET"])
def predict():
	return jsonify(predict_digit())

@app.route("/health", methods=["GET"])
def health():
	return jsonify({
		"status": "healthy"
	})

@app.route("/echo", methods=["POST"])
def echo():
	data = request.json
	return jsonify({
		"received": data
	})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
