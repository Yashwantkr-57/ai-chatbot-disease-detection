from .nlp import predict_class, intents
from .responses import get_response, fallback_response
from .memory import get_user_context, update_user_context
from .weather import get_weather
from .weather_rules import analyze_weather
from .city_extractor import extract_city
from .disease_engine import detect_disease


EXIT_KEYWORDS = {
    "exit", "cancel", "stop", "restart", "reset",
    "hi", "hello", "help", "new question"
}


def reset_context(user_id):
    update_user_context(user_id, {
        "last_intent": None,
        "stage": None,
        "data": {}
    })


def process_message(msg, user_id="default"):
    msg = msg.strip().lower()
    context = get_user_context(user_id)

    last_intent = context["last_intent"]
    stage = context["stage"]
    data = context["data"]

    # ==================================================
    # 🚨 EXIT / INTERRUPT HANDLING (HIGHEST PRIORITY)
    # ==================================================
    if msg in EXIT_KEYWORDS:
        reset_context(user_id)
      # Let NLP handle the message

    # ==================================================
    # 🌱 ACTIVE CROP FLOW
    # ==================================================
    if last_intent == "crop_advice":

        # ---- STEP 1: ASK CROP NAME ----
        if stage == "awaiting_crop":
            data["crop"] = msg

            update_user_context(user_id, {
                "last_intent": "crop_advice",
                "stage": "awaiting_issue",
                "data": data
            })

            return (
                f"Got it. You are growing {msg.title()}.\n"
                "Now please describe the symptoms "
                "(spots, color changes, wilting, mold, etc.)."
            )

        # ---- STEP 2: ASK SYMPTOMS ----
        if stage == "awaiting_issue":
            crop = data.get("crop")

            result = detect_disease(crop, msg)

            if not result:
                return (
                    "Please describe the symptoms clearly.\n"
                    "Example: brown spots on leaves, wilting, mold."
                )

            reset_context(user_id)

            return (
                f"🌱 Crop: {crop.title()}\n"
                f"🦠 Possible Disease: {result['disease']}\n"
                f"💡 Recommendation: {result['solution']}"
            )

    # ==================================================
    # 🧠 NLP INTENT DETECTION
    # ==================================================
    ints = predict_class(msg)
    if not ints:
        return fallback_response()

    top_intent = ints[0]["intent"]
    confidence = float(ints[0]["probability"])

    if confidence < 0.40:
        return "Can you please explain a little more?"

    # ==================================================
    # 🌦 WEATHER
    # ==================================================
    if top_intent == "weather":
        city = extract_city(msg)

        if not city:
            update_user_context(user_id, {
                "last_intent": "weather",
                "stage": "awaiting_location",
                "data": {}
            })
            return "Please tell me your city name."

        weather = get_weather(city)
        if not weather:
            return "Sorry, I couldn't find weather for that location."

        advice = analyze_weather(weather)

        response = [
            f"🌦️ Weather in {weather['city']}:",
            f"🌡️ Temperature: {weather['temp']}°C",
            f"💧 Humidity: {weather['humidity']}%",
            f"☁️ Condition: {weather['description'].title()}"
        ]

        if advice:
            response.append("")
            response.extend([f"⚠️ {a}" for a in advice])

        return "\n".join(response)

    # ==================================================
    # 🌱 START CROP ADVICE
    # ==================================================
    if top_intent == "crop_advice":
        update_user_context(user_id, {
            "last_intent": "crop_advice",
            "stage": "awaiting_crop",
            "data": {}
        })
        return "Which crop are you growing?"

    # ==================================================
    # 👋 GREETING
    # ==================================================
    if top_intent == "greeting":
        return get_response(ints, intents)

    # ==================================================
    # 🔁 DEFAULT
    # ==================================================
    return get_response(ints, intents)
