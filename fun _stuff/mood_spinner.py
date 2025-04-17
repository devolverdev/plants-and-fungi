# 🎰 mood_spinner.py

import tkinter as tk
import random

moods = {
    "sad": ("rose quartz", "#f4c2c2"),
    "tired": ("mint", "#a8ffb0"),
    "anxious": ("lavender", "#cda4de"),
    "joyful": ("citrine", "#fff475"),
    "creative": ("amethyst", "#b388eb")
}

root = tk.Tk()
root.title("🌈 Mood Spinner")
root.geometry("400x300")
root.config(bg="#f0eaff")

label = tk.Label(root, text="🌟 Click to receive a mood remedy!", font=("Helvetica", 14), bg="#f0eaff")
label.pack(pady=30)

result = tk.Label(root, text="", font=("Helvetica", 18), bg="#f0eaff")
result.pack(pady=20)

def spin():
    mood, (item, color) = random.choice(list(moods.items()))
    root.config(bg=color)
    result.config(text=f"{mood.title()} → {item.title()}")

btn = tk.Button(root, text="🎡 Spin the Mood Wheel!", command=spin, font=("Helvetica", 14))
btn.pack(pady=20)

root.mainloop()
