from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(
    api_key="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"
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
    app.run(host='0.0.0.0', port=10000)
