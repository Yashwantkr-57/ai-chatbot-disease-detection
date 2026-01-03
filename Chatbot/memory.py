import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "memory.json")

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return {}
    with open(MEMORY_FILE, "r") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)

def get_user_context(user_id="default"):
    memory = load_memory()
    if user_id not in memory:
        memory[user_id] = {
            "last_intent": None,
            "stage": None,
            "data": {}
        }
        save_memory(memory)
    return memory[user_id]

def update_user_context(user_id, updates):
    memory = load_memory()
    if user_id not in memory:
        get_user_context(user_id)

    memory[user_id].update(updates)
    save_memory(memory)
