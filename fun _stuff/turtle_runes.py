import turtle
import random
import time

# Elder Futhark rune meanings (simplified)
runes = {
    "ᚠ": "Fehu – Wealth, prosperity",
    "ᚢ": "Uruz – Strength, endurance",
    "ᚦ": "Thurisaz – Chaos, defense",
    "ᚨ": "Ansuz – Wisdom, divine message",
    "ᚱ": "Raidho – Journey, movement",
    "ᚲ": "Kenaz – Fire, creativity",
    "ᛃ": "Jera – Harvest, reward",
    "ᛇ": "Eiwaz – Transformation, death/rebirth",
    "ᛉ": "Algiz – Protection, sanctuary",
    "ᛟ": "Othala – Heritage, ancestry"
}

# Setup turtle
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("✨ Rune Divination ✨")

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.color("white")

def draw_rune(rune, meaning):
    pen.clear()
    pen.penup()
    pen.goto(0, 0)
    pen.write(rune, align="center", font=("Courier", 120, "bold"))
    pen.goto(0, -100)
    pen.write(meaning, align="center", font=("Courier", 16, "italic"))

# Draw border
def draw_circle_frame():
    frame = turtle.Turtle()
    frame.color("purple")
    frame.pensize(4)
    frame.penup()
    frame.goto(0, -250)
    frame.pendown()
    frame.circle(250)
    frame.hideturtle()

draw_circle_frame()
time.sleep(1)

# Pick a random rune
rune, meaning = random.choice(list(runes.items()))
draw_rune(rune, meaning)

turtle.done()
