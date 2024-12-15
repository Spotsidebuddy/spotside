import turtle as t
import math as m


def dragon_curve(l, n, flag=True):          #starting with f
    if n == 0:                              #end condition
        t.forward(l)
        return
    x = m.sqrt(l**2/2)
    if (2*int(flag) - 1) == 1:              #if f (flag == True)
        dragon_curve(x, n - 1, True)   # f
        t.left(90)                          # -
        dragon_curve(x, n - 1, False)  # h
    if (2*int(flag) - 1) == -1:             # if h (flag == False)
        dragon_curve(x, n - 1, True)   # f
        t.right(90)                         # +
        dragon_curve(x, n - 1, False)  # h



def dragon(l, n):
    t.right(45*n)
    dragon_curve(l, n)
    t.exitonclick()

dragon(400, 5)
