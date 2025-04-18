import json
import logging

def load_data(filename):
    try:
        with open(f"data/{filename}") as f:
            data = json.load(f)
            logging.info(f"✅ Loaded data/{filename} successfully.")
            return data
    except FileNotFoundError:
        logging.error(f"❌ File not found: data/{filename}")
        return {}
    except json.JSONDecodeError:
        logging.error(f"❌ Failed to decode JSON: data/{filename}")
        return {}
