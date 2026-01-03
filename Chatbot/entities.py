import re

CROPS = ["tomato", "potato", "wheat", "rice", "maize"]
ISSUES = ["disease", "pest", "fertilizer", "watering"]

def extract_entities(message):
    message = message.lower()
    entities = {}

    for crop in CROPS:
        if crop in message:
            entities["crop"] = crop
            break

    for issue in ISSUES:
        if issue in message:
            entities["issue"] = issue
            break

    # Simple location extraction
    match = re.search(r"in ([a-zA-Z ]+)", message)
    if match:
        entities["location"] = match.group(1).strip()

    return entities
