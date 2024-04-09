import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the speed of the turtle
t.speed(5)

# Move the turtle to the starting point
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the outer arc of the heart
t.begin_fill()
t.fillcolor("red")
t.left(140)
t.forward(224)
t.circle(-120, 200)

# Draw the inner arc of the heart
t.left(120)
t.circle(120, 200)
t.forward(224)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until it's closed manually
turtle.done()
