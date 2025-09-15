from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("models/pollutant_avg_model.pkl")
df = pd.read_csv("data/processed_data.csv")

@app.route("/")
def index():
    latest = df.tail(1)
    latest_avg = latest['pollutant_avg'].values[0]
    return render_template("index.html", latest_avg=latest_avg)

@app.route("/eda")
def eda():
    summary = pd.read_csv('static/summary.csv', index_col=0)
    return render_template("eda.html", summary=summary)

@app.route("/model")
def model_dashboard():
    return render_template("model.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # Encode pollutant_id
    pollutant_id = pd.Series([data['pollutant_id']]).astype('category').cat.codes[0]
    features = [
        float(data['latitude']),
        float(data['longitude']),
        pollutant_id,
        float(data['pollutant_min']),
        float(data['pollutant_max'])
    ]
    pred = model.predict([features])[0]
    return jsonify({"predicted_avg": round(pred, 2)})

if __name__ == "__main__":
    app.run(debug=True)