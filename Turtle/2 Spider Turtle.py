import turtle

x = 1
number_of_legs = 12
length_of_legs = 75

while x <= number_of_legs:
    turtle.forward(length_of_legs)
    turtle.stamp()
    turtle.back(length_of_legs)
    turtle.left(360 / number_of_legs)
    x += 1
