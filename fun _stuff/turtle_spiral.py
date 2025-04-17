# 🌀 turtle_spiral.py

import turtle
import colorsys
 

t = turtle.Turtle()

t.screen.colormode(255)  # 💡 Enable RGB tuples like (255, 0, 0)

t.speed(0)
turtle.bgcolor("black")

hue = 0
n = 36

for i in range(360):
    col = colorsys.hsv_to_rgb(hue, 1, 1)
    col = tuple(int(c * 255) for c in col)
    t.color(col)
    t.forward(i * 2)
    t.left(59)
    hue += 0.005

turtle.done()



####

