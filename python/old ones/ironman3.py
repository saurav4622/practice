import turtle

# Set the turtle's speed
turtle.speed('fastest')

# Set the background color
turtle.bgcolor('#000000')

# Draw the head
turtle.color('#FFD700')
turtle.begin_fill()
turtle.circle(50)
turtle.end_fill()

# Draw the eyes
turtle.color('#FFFFFF')
turtle.penup()
turtle.goto(-15, 55)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()
turtle.penup()
turtle.goto(15, 55)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.end_fill()

# Draw the mouth
turtle.color('#FF0000')
turtle.penup()
turtle.goto(-25, 35)
turtle.pendown()
turtle.pensize(5)
turtle.goto(25, 35)

# Draw the body
turtle.color('#FFD700')
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.pensize(10)
turtle.goto(0, -100)

# Draw the arms
turtle.color('#FFD700')
turtle.penup()
turtle.goto(-50, -30)
turtle.pendown()
turtle.pensize(10)
turtle.goto(-100, -30)
turtle.penup()
turtle.goto(50, -30)
turtle.pendown()
turtle.pensize(10)
turtle.goto(100, -30)

# Draw the hands
turtle.color('#FFD700')
turtle.penup()
turtle.goto(-100, -30)
turtle.pendown()
turtle.pensize(15)
turtle.goto(-100, -70)
turtle.penup()
turtle.goto(100, -30)
turtle.pendown()
turtle.pensize(15)
turtle.goto(100, -70)

# Draw the legs
turtle.color('#FFD700')
turtle.penup()
turtle.goto(-35, -100)
turtle.pendown()
turtle.pensize(10)
turtle.goto(-35, -200)
turtle.penup()
turtle.goto(35, -100)
turtle.pendown()
turtle.pensize(10)
turtle.goto(35, -200)

# Draw the feet
turtle.color('#FFD700')
turtle.penup()
turtle.goto(-35, -200)
turtle.pendown()
turtle.pensize(15)
turtle.goto(-75, -200)
turtle.penup()
turtle.goto(35, -35)
