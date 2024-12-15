import turtle as t
"""ПРИМЕР ОТРИСОВКИ ФРАКТАЛА"""
t.shape('arrow')
t.speed(1)
def draw(l, n):
    if n == 0:
        t.left(180)
        return

    x = l / (n + 1)
    for i in range(n):
        t.forward(x)
        t.left(45)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        t.left(90)
        draw(0.5 * x * (n - i - 1), n - i - 1)
        t.right(135)

    t.forward(x)
    t.left(180)
    t.forward(l)

draw(300, 0)

t.exitonclick()