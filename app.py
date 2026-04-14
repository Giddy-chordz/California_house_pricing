import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np

app = Flask(__name__)

# load model + scaler
model = pickle.load(open("regmodel.pkl", "rb"))
scaler = pickle.load(open("scaling.pkl", "rb"))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json['data']

    features = np.array([
        data["MedInc"],
        data["HouseAge"],
        data["AveRooms"],
        data["AveBedrms"],
        data["Population"],
        data["AveOccup"],
        data["Latitude"]
    ]).reshape(1, -1)

    # scale properly
    new_data = scaler.transform(features)

    # predict using scaled data
    prediction = model.predict(new_data)

    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)