import turtle as t

def star(n):
    i = 1
    l = 200
    t.up()
    t.goto((l / 2), 0)
    t.down()
    t.left(180)
    if n % 2 == 0:
        while i <= n:
            t.forward(l)
            t.left(180 - 360 / n)
            i += 1
    if n % 2 == 1:
        while i <= (n):
            t.forward(l)
            t.left(180 - 180 / n)
            i +=1

n = 9
star(n)
t.exitonclick()