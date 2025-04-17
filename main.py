# main.py


from garden.mood_mapper import suggest_remedy

from garden.data_loader import load_data

# Load plants and fungi JSON

plants = load_data("plants.json")
fungi = load_data("fungi.json")

mood = input("💭 How are you feeling? ")
remedy = suggest_remedy(mood)


print("🌿 Suggested remedy:", remedy)
print("🌿 Loaded Plants:")
print(plants)

print("🍄 Loaded Fungi:")
print(fungi)
