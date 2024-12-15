import turtle

t = turtle.Turtle()


def circle_right():
    i = 1
    while i < 61:
        t.forward(4)
        t.right(6)
        i += 1


def circle_left():
    i = 1
    while i < 61:
        t.forward(4)
        t.left(6)
        i += 1


def flower(n):
    i = 1
    if n % 2 == 0:
        while i <= (n / 2):
            circle_left()
            circle_right()
            t.left(360 / n)
            i += 1

    if n % 2 == 1:
        while i <= n:
            circle_left()
            t.left(360 / n)
            i += 1


t.speed(10)
flower(8)
turtle.exitonclick()
