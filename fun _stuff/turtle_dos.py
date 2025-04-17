import turtle
import colorsys

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)

h = 0
for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    t.forward(i * 3 / 2)
    t.left(59)
    t.circle(i / 2, 60)
    h += 0.005

turtle.done()
