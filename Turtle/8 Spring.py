import turtle as t


def spiral(n):
    t.penup()
    t.goto(-180, 0)
    t.pendown()
    if n <= 0:
        print('Welp!')
    elif n == 1:
        t.left(90)
        t.circle(-30, 180)
        t.circle(-6, 180)
        t.circle(-30, 90)
    elif n == 2:
        t.left(90)
        t.circle(-30, 180)
        t.circle(-6, 180)
        t.circle(-30, 180)
    elif n > 2:
        i = 1
        t.left(90)
        t.circle(-30, 180)
        t.circle(-6, 180)
        t.circle(-30, 180)
        while i <= n - 2:
            t.circle(-6, 180)
            t.circle(-30, 180)
            i += 1
    t.circle(-6, 30)
    t.exitonclick()


spiral(3)
