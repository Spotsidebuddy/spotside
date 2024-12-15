import turtle as t
t.speed('fastest')
def minkovski(l, n):
    if n == 0:
        t.forward(l)
        return
    x = l/4
    minkovski(x, n - 1)
    t.left(90)
    minkovski(x, n - 1)
    t.right(90)
    minkovski(x, n - 1)
    t.right(90)
    minkovski(x, n - 1)
    minkovski(x, n - 1)
    t.left(90)
    minkovski(x, n - 1)
    t.left(90)
    minkovski(x, n - 1)
    t.right(90)
    minkovski(x, n - 1)

side = 700
depth = 3
t.up()
t.goto(-side/2, 0)
t.down()

minkovski(side, depth)
t.exitonclick()
