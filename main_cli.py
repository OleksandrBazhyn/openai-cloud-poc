from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def chat():
    print("🇩🇪 Online-Deutscher Gesprächspartner")
    print("Tippe 'exit', um zu beenden.\n")

    while True:
        user_input = input("Du: ")

        if user_input.lower() == "exit":
            break

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
                        "Korrigiere Fehler höflich, wenn es passt, und erkläre kurz warum."
                    ),
                },
                {"role": "user", "content": user_input},
            ],
        )

        answer = response.choices[0].message.content
        print("Partner:", answer, "\n")


if __name__ == "__main__":
    chat()
