import turtle  
turtle.speed(0)
turtle.bgcolor('black')
turtle.pencolor('purple')
for i in range(220):
    turtle.rt(i)
    turtle.circle(120,i)
    turtle.fd(i)
    turtle.rt(90)
turtle.done()