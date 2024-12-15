import turtle as t


def butterfly(n):
    t.left(90)
    rad = 50
    i = 1
    while i <= n:
        t.circle(rad)
        t.circle(-1 * rad)
        rad +=5
        i += 1


n = int(t.textinput('How many wings, brother?', ''))
butterfly(n)
