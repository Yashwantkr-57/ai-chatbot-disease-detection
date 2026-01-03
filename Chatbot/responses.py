import random

def get_response(ints, intents_json):
    tag = ints[0]["intent"]

    for intent in intents_json["intents"]:
        if intent["tag"] == tag:

            # Stable replies for greetings
            if tag == "greeting":
                return intent["responses"][0]

            # Random replies for others
            return random.choice(intent["responses"])


def fallback_response():
    return (
        "I'm still learning 🌱\n"
        "Please try asking in a different way."
    )
