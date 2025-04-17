# garden/species.py

import json

def load_plants(path="data/plants.json"):
    """Load plant data from the JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def describe_plant(name, info):
    """Print plant info nicely."""
    uses = info.get("uses", "unknown")
    element = info.get("element", "unknown")
    print(f"🌿 {name.title()} helps with {uses} and is linked to the element: {element}")
