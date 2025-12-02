from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(force=True)
    user_text = data.get("text", "")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Du bist ein lebendiger, freundlicher deutscher Gesprächspartner. "
                    "Du antwortest immer ausschließlich auf Deutsch."
                ),
            },
            {"role": "user", "content": user_text},
        ],
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
