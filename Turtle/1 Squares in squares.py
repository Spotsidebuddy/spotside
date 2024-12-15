import turtle

x = 1
y = 1
n = 10
number_of_squares = 10
spacing_btw_squares = 5

while x <= number_of_squares:
    while y <= 4:
        turtle.left(90)
        turtle.forward(n)
        y += 1
    turtle.penup()
    turtle.forward(spacing_btw_squares)
    turtle.right(90)
    turtle.forward(spacing_btw_squares)
    turtle.left(90)
    turtle.pendown()
    x += 1
    y = 1
    n += 10
