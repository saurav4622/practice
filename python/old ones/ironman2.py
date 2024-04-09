import turtle

# create a turtle
t = turtle.Turtle()

# set the turtle's speed
t.speed(5)

# draw the head
t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()

# move the turtle to the position for the body
t.penup()
t.goto(0, -50)

# draw the body
t.color("yellow")
t.begin_fill()
t.circle(75, 180)
t.end_fill()

# move the turtle to the position for the left arm
t.goto(-60, -10)

# draw the left arm
t.color("yellow")
t.begin_fill()
t.circle(20, 180)
t.end_fill()

# move the turtle to the position for the right arm
t.goto(60, -10)

# draw the right arm
t.color("yellow")
t.begin_fill()
t.circle(20, 180)
t.end_fill()

# hide the turtle
t.hideturtle()

# keep the window open until it is closed
turtle.mainloop()
