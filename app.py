from flask import Flask, request
import os
import requests

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

@app.route('/')
def home():
    return "Bridge is working!"

@app.route('/send', methods=['POST'])
def send_to_telegram():
    if not TELEGRAM_TOKEN or not CHAT_ID:
        return "Missing Telegram configuration", 500

    data = request.json
    text = data.get("text", "No text received")

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}

    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return "Message sent!"
    else:
        return f"Error: {response.text}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
