from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from config import OPENAI_API_KEY

app = Flask(__name__)
client = OpenAI(api_key=OPENAI_API_KEY)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_text = data.get("text", "")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Du bist ein lebendiger, freundlicher deutscher Gesprächspartner. "
                    "Du hilfst Lernenden dabei, ihr Deutsch zu verbessern. "
                    "Antworte IMMER ausschließlich auf Deutsch, "
                    "auch wenn der Benutzer in einer anderen Sprache schreibt. "
                    "Sprich in natürlichem, alltagsnahen Deutsch (ungefähr B2–C1), "
                    "sei geduldig und ermutigend. "
                    "Korrigiere Fehler höflich, wenn es sinnvoll ist."
                ),
            },
            {"role": "user", "content": user_text},
        ],
    )

    answer = response.choices[0].message.content
    return jsonify({"answer": answer})


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)