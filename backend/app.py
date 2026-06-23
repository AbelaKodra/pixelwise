from flask import Flask, jsonify
from models.predict import predict_digit

app = Flask(__name__)

@app.route("/")
def home():
	return "PixelWise Backend laeuft!"

@app.route("/predict")
def predict():
	return jsonify(predict_digit())

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
