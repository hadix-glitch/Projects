# Using turtle to create coloured shapes.
import turtle

# Creating a simple house using turtle.

# turtle.bgcolor("Yellow")
# turtle.pensize("3")
# turtle.pencolor("red")
# turtle.forward(150)
# turtle.left(90)
# turtle.forward(150)
# turtle.left(45)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(45)
# turtle.forward(75)
# turtle.right(90)
# turtle.forward(30)
# turtle.left(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(48)
# turtle.left(90)
# turtle.forward(22)
# turtle.right(90)
# turtle.forward(15)
# turtle.right(90)
# turtle.forward(22)
# turtle.penup()
# turtle.goto(40, 110)
# turtle.pendown()
# turtle.forward(20)
# turtle.left(90)
# turtle.forward(30)
# turtle.left(90)
# turtle.forward(20)
# turtle.left(90)
# turtle.forward(30)
# turtle.pendown()
# turtle.done()
# This completes the drawing of house.

for i in range(120):
    for colours in ["red", "green", "blue"]:
        turtle.color(colours)
        turtle.bgcolor("pink")
        turtle.pensize(2)
        turtle.circle(160)
        turtle.left(1)
        turtle.speed(100)
turtle.done()  # This creates a more complex circular shape