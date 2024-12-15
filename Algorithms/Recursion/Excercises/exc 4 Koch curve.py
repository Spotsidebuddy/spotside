import turtle as t

t.penup()
t.left(180)
t.forward(300)
t.left(180)
t.down()

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







draw_curve(600, 0)

t.exitonclick()
