from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

BOT_TOKEN = "7899833498:AAFvFEUKkSh7PfuZH1SQcXO1Vt50oaeV2N0"
CHAT_ID = "7006969586"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Telegram Signal Bot is running", "status": "ok"})

@app.route("/signal", methods=["POST"])
def signal():
    data = request.json
    text = (
        f"📊 Торговый сигнал:\n"
        f"Валюта: {data.get('asset')}\n"
        f"Действие: {data.get('action')}\n"
        f"Уверенность: {data.get('confidence')}%\n"
        f"Время входа: {data.get('entry_time')}\n"
        f"Таймфрейм: {data.get('timeframe')}\n\n"
        f"_Сообщение отправлено автоматически._"
    )
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"}
    response = requests.post(url, json=payload)
    return jsonify({"status": "sent", "telegram_response": response.json()}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
