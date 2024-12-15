import turtle as t

def cantor(l, n, x=0, y=0):
    l_short = l/3
    if n == 0:
        t.up()
        t.goto(x, y)
        t.down()
        t.forward(l)
        return
    elif n >= 1:
        t.up()
        t.goto(x, y)
        t.down()
        t.forward(l)
        cantor(l/3, n - 1, x, y - 10)
        cantor(l/3, n - 1, x + 2 * l/3, y - 10)

t.width(3)
cantor(400, 3)
t.exitonclick()