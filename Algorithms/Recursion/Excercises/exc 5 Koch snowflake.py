import turtle as t
def draw_curve(l, n):
    if n == 0:
        t.forward(l)
        return
    x = l/3
    draw_curve(x, n - 1)
    t.left(60)
    draw_curve(x, n - 1)
    t.right(120)
    draw_curve(x, n - 1)
    t.left(60)
    draw_curve(x, n - 1)

def draw_snowflake(side, n):
    t.up()
    t.goto(-side/2, side/2)
    t.down()
    draw_curve(side, n)
    t.right(120)
    draw_curve(side, n)
    t.right(120)
    draw_curve(side, n)


draw_snowflake(400, 4)

t.exitonclick()