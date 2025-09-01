import json
import os

DB_FILE = "data/confessions.json"
os.makedirs("data", exist_ok=True)

def load_confessions():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_confessions(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_confession(confession_id: str, user_id: int):
    data = load_confessions()
    data[confession_id] = user_id
    save_confessions(data)

def get_user_by_confession(confession_id: str):
    data = load_confessions()
    return data.get(confession_id)
