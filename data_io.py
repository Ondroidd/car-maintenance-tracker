import json
import os


DATA_FILE = "data.json"


def load_data(filename=DATA_FILE):
    if not os.path.exists(filename):
        return {
            "maintenance": [],
            "fuel": []
        }

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data, filename=DATA_FILE):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
