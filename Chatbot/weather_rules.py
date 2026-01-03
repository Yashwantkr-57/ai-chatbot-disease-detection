def analyze_weather(weather, crop=None):
    advice = []

    temp = weather["temp"]
    humidity = weather["humidity"]
    rain = weather.get("rain", 0)
    description = weather["description"].lower()

    # 🌧 Rain alert — STRICT & CORRECT
    if rain > 0:
        advice.append("🌧 Rain expected. Avoid irrigation today.")

    # 🌡 Temperature alerts
    if temp > 35:
        advice.append("🔥 High temperature detected. Risk of heat stress.")
    elif temp < 10:
        advice.append("❄ Low temperature detected. Protect crops from cold.")

    # 🌫 High humidity alert (not rain!)
    if humidity > 85:
        advice.append("💧 Very high humidity. Risk of fungal diseases.")

    # 🌱 Crop-specific logic
    if crop == "tomato":
        if temp > 32:
            advice.append("🍅 Tomatoes may suffer heat stress. Increase shading.")
        if humidity > 80:
            advice.append("🍅 High humidity may cause fungal diseases in tomatoes.")

    return advice
