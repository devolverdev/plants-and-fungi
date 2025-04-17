import turtle
import random
from PIL import Image


# ---- Style Setup ----
screen = turtle.Screen()
screen.bgcolor("midnightblue")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

colors = ["gold", "violet", "deeppink", "turquoise", "lavender"]
shapes = ["🌸", "🌙", "💫", "🔮", "🦋"]

# ---- Draw Background Star Spiral ----
def draw_star_spiral():
    for i in range(90):
        t.color(random.choice(colors))
        t.forward(i * 2)
        t.left(144)

# ---- Add Title + Affirmation ----
def write_text(title, affirmation):
    t.penup()
    t.goto(-80, 150)
    t.color("white")
    t.write(f"🔮 {title}", font=("Georgia", 18, "bold"))

    t.goto(-100, -200)
    t.write(f"✨ {affirmation}", font=("Georgia", 14, "italic"))

# ---- Make a Card ----
title = random.choice(["The Bloom", "The Seeker", "The Prism", "The Spiral", "The Flame"])
affirmation = random.choice([
    "I trust my journey.",
    "Everything I seek is within me.",
    "I bloom through stillness.",
    "I flow with change.",
    "My magic is real and radiant."
])

draw_star_spiral()
write_text(title, affirmation)

# ---- Save the Result (Screenshot) ----
ts = t.getscreen()
ts.getcanvas().postscript(file="mystic_card.eps")  # Save as EPS
print("🌟 Saved as mystic_card.eps")
turtle.done()
