import turtle
import math

t = turtle.Turtle()


def polygon(n, r):
    i = 1
    t.up()
    t.goto(r, 0)
    t.down()
    while i <= n:
        t.left((180 - 360 / n) / 2)
        t.left(360 / n)
        t.forward(2 * r * math.sin(math.pi / n))
        i += 1
        t.right((180 - 360 / n) / 2)


def polygons(x):
    i = 1
    r = 30
    n = 3
    while i <= x:
        polygon(n, r)
        r += 10
        i += 1
        n += 1

polygons(3)
turtle.exitonclick()