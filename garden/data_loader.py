# garden/data_loader.py

import json
import os

def load_data(filename):
    """Load JSON data from the data/ folder."""
    path = os.path.join("data", filename)
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found in /data/")
        return {}
    except json.JSONDecodeError:
        print(f"⚠️ File '{filename}' is not valid JSON.")
        return {}
