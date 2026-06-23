from flask import Flask, jsonify, request
from models.predict import predict_digit
from models.storage import save_prediction

app = Flask(__name__)

@app.route("/")
def home():
	return jsonify({
		"service": "PixelWise API",
		"status": "running"
	})


@app.route("/predict")
def predict():

	result = predict_digit()

	save_prediction(
		result["digit"],
		result["confidence"]
	)

	return jsonify(result)

@app.route("/health")
def health():
	return jsonify({
		"status": "healthy"
	})

@app.route("/history")
def history():

	import sqlite3

	conn = sqlite3.connect("pixelwise.db")

	rows = conn.execute(
		"SELECT * FROM predictions"
	).fetchall()

	conn.close()

	return jsonify(rows)

@app.route("/echo", methods=["POST"])
def echo():
	data = request.json
	return jsonify({
		"received": data
	})

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
