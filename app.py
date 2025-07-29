from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)  # Разрешаем CORS, чтобы можно было обращаться с других доменов

API_KEY = "d5f376fc9cd813e26279f6f0bf10d6f6"
API_URL = f"https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=eu&markets=h2h&apiKey={API_KEY}"

@app.route("/api/odds")
def get_odds():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)



