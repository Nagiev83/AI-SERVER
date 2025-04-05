from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Используем переменную окружения для API ключа
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return "Привет! Сервер работает."

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    user_message = data.get("message", "")

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        ai_message = response.choices[0].message.content
        return jsonify({"reply": ai_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
