# 🌿 bash_garden.py

from colorama import init, Fore, Style
import time
import random

init(autoreset=True)

plants = [
    Fore.GREEN + "🌱",
    Fore.YELLOW + "🌼",
    Fore.MAGENTA + "🌸",
    Fore.RED + "🌹",
    Fore.CYAN + "🌾"
]

print("🌿 Planting seeds...\n")
time.sleep(1)

for i in range(10):
    plant = random.choice(plants)
    print(" " * random.randint(0, 30) + plant)
    time.sleep(0.4)

print("\n🌈 Your bash garden is blooming!")
