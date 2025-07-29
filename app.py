from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = "d5f376fc9cd813e26279f6f0bf10d6f6"
API_URL = f"https://api.the-odds-api.com/v4/sports/upcoming/odds/?regions=eu&markets=h2h&apiKey={API_KEY}"

@app.route("/api/odds")
def get_odds():
    try:
        response = requests.get(API_URL)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # Запускаем на 0.0.0.0, чтобы сервис был доступен извне (Render)
    app.run(host="0.0.0.0", port=port)
