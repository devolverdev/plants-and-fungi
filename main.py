# main.py

from garden.utils import load_json
from garden.mood_mapper import suggest_remedy
from garden.plant_lookup import find_plant

plant_name = input("🌿 Which plant would you like to look up? ")
info = find_plant(plant_name)
print(info)

# Load plants and fungi JSON safely
plants = load_json("data/plants.json")
fungi = load_json("data/fungi.json")

# Ask the user for their mood
mood = input("💭 How are you feeling? ").lower()
remedy = suggest_remedy(mood)

# Show results
print("🌿 Suggested remedy:", remedy)
print("🌿 Loaded Plants:", plants)
print("🍄 Loaded Fungi:", fungi)

# Optional: Try loading a missing file to test error handling
# missing = load_json("data/does_not_exist.json")

print("✅ Program finished without crashing.")
