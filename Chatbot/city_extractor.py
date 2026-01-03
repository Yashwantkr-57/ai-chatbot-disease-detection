import re

COMMON_CITIES = [
    "delhi", "mumbai", "kolkata", "chennai", "bengaluru",
    "hyderabad", "pune", "ahmedabad", "jaipur", "chandigarh",
    "shimla", "dehradun", "ranchi", "patna", "bhopal",
    "indore", "raipur", "guwahati", "shillong", "meghalaya"
]

def extract_city(text):
    if not text:
        return None

    text = text.lower()

    # Direct match
    for city in COMMON_CITIES:
        if city in text:
            return city.title()

    # Fallback: last word
    words = re.findall(r"[a-zA-Z]+", text)
    if words:
        return words[-1].title()

    return None
