from rapidfuzz import fuzz

CROP_DISEASES = {
    "tomato": {
        "early blight": {
            "symptoms": ["brown spots", "yellow leaves", "leaf drop"],
            "solution": "Remove infected leaves and apply fungicide."
        },
        "late blight": {
            "symptoms": ["dark patches", "mold", "wilting"],
            "solution": "Use disease-free seeds and apply fungicide spray."
        }
    },

    "potato": {
        "early blight": {
            "symptoms": ["brown rings", "dry spots"],
            "solution": "Apply fungicide and rotate crops."
        },
        "late blight": {
            "symptoms": ["water-soaked lesions", "white mold"],
            "solution": "Destroy infected plants and spray fungicide."
        }
    },

    "rice": {
        "blast disease": {
            "symptoms": ["diamond spots", "gray center", "leaf drying"],
            "solution": "Use resistant varieties and apply nitrogen carefully."
        },
        "bacterial blight": {
            "symptoms": ["yellowing", "leaf drying", "ooze"],
            "solution": "Ensure proper drainage and avoid excessive nitrogen."
        }
    },

    "wheat": {
        "rust disease": {
            "symptoms": ["orange pustules", "powdery spots"],
            "solution": "Use resistant varieties and fungicide spray."
        }
    },

    "maize": {
        "leaf blight": {
            "symptoms": ["elongated gray spots", "leaf drying"],
            "solution": "Remove infected residue and apply fungicide."
        }
    }
}


def detect_disease(crop, user_text):
    crop = crop.lower()
    user_text = user_text.lower()

    if crop not in CROP_DISEASES:
        return None

    best_match = None
    best_score = 0

    for disease, info in CROP_DISEASES[crop].items():
        for symptom in info["symptoms"]:
            score = fuzz.partial_ratio(symptom, user_text)

            if score > best_score and score >= 60:
                best_score = score
                best_match = {
                    "disease": disease.title(),
                    "solution": info["solution"]
                }

    return best_match
