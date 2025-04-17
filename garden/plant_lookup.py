# garden/plant_lookup.py

import logging
from garden.utils import load_json

plants = load_json("data/plants.json")

def find_plant(name):
    try:
        plant = plants[name.lower()]
        return plant
    except KeyError:
        logging.error(f"❌ Plant '{name}' not found in codex.")
        return f"🌾 No info for {name}... maybe try growing it?"
