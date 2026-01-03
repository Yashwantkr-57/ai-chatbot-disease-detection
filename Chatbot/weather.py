import requests

API_KEY = "845055f6b31614c3ae411fa9705736b7"

# ==================================================
# 🌦 CURRENT WEATHER
# ==================================================
def get_weather(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    # ❌ City not found / API error
    if data.get("cod") != 200:
        print("FULL WEATHER DATA:", data)
        return None

    return {
        "city": data["name"],
        "temp": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"].lower(),
        "rain": data.get("rain", {}).get("1h", 0)
    }


# ==================================================
# 🌧 12-HOUR RAIN PROBABILITY (FORECAST)
# ==================================================
def get_rain_probability_12h(city):
    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != "200":
        print("FORECAST ERROR:", data)
        return None

    rain_slots = 0
    total_slots = 4   # 4 × 3h = 12 hours

    for slot in data["list"][:total_slots]:
        description = slot["weather"][0]["description"].lower()
        if "rain" in description or "drizzle" in description:
            rain_slots += 1

    probability = int((rain_slots / total_slots) * 100)
    return probability


