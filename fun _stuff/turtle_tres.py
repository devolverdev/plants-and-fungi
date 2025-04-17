import turtle


def draw_flower(t, petals, size):
    if petals == 0:
        return
    for _ in range(2):
        t.circle(size, 60)
        t.left(120)
    t.right(360 / petals)
    draw_flower(t, petals - 1, size)


t = turtle.Turtle()
t.color("magenta")
t.speed(0)
draw_flower(t, 36, 100)
turtle.done()
