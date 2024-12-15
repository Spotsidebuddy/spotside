import turtle as t
import math as m
t.speed(10)


def levi(l, n):
    if n == 0:
        t.forward(l)
        return
    x = m.sqrt((l**2)/2)
    t.left(45)
    levi(x, n - 1)
    t.right(90)
    levi(x, n - 1)
    t.left(45)


l = 400
n = 13
levi(l, n)
t.exitonclick()
