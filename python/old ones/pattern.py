import turtle
import colorsys
tr = turtle.Turtle()
sc=turtle.Screen().bgcolor('black')
tr.speed(100)
n= 70
h=0
for i in range(360):
    c=colorsys.hsv_to_rgb(h,1,0.8)
    h+=1/n
    tr.color(c)
    tr.left(1)
    tr.fd(1)
    for i in range(2):
          tr.left(5)
          tr.circle(100)