# garden/utils.py

import json
import logging

logging.basicConfig(filename="logs.txt", level=logging.INFO)


def load_json(path):
    try:
        with open(path, "r") as file:
            data = json.load(file)
            logging.info(f"✅ Loaded {path} successfully.")
            return data
    except FileNotFoundError:
        logging.error(f"❌ File not found: {path}")
        return {}
    except json.JSONDecodeError:
        logging.error(f"❌ Could not decode JSON in {path}")
        return {}
    except Exception as e:
        logging.exception(f"😱 Unexpected error: {e}")
        return {}
