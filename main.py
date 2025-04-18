from garden.data_loader import load_data
from garden.mood_mapper import suggest_remedy, MoodNotFound
from garden.utils import load_json
import logging

logging.basicConfig(filename="logs.txt", level=logging.INFO)

# Load codex data
plants = load_data("plants.json")
fungi = load_data("fungi.json")

# Ask user
mood = input("💭 How are you feeling? ")

try:
    remedy = suggest_remedy(mood)
    print("🌿 Suggested remedy:", remedy)
except MoodNotFound as e:
    print("⚠️", e)
    remedy = None

# Show full codex
print("🌿 Loaded Plants:")
print(plants)

print("🍄 Loaded Fungi:")
print(fungi)
