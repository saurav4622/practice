def circle(radius):
    return math.pi * radius ** 2
def rectangle(length,breadth):
    return length*breadth
def  triangle(base,height):
    return  (1/2)*base*height
def square(side):
    return side**2

print("THIS IS A AREA FOUNDER PROGRAM")
print("Choose the one from below.")
print("1.Circle\n2.Rectangle\n3.Square\n4.Triangle")
i=int(input("Enter your choice:"))
if  i==1:
    r = float(input("Enter your Radius: "))
    print("The Area of Circle  is ",circle(r))
elif i == 2 :
    l = float(input("Enter Length: "))
    b = float(input("Enter Breadth: "))
    print("The Area of Rectangle is ",rectangle(l,b))
elif i == 3:
    s = float(input("Enter Side Length: "))
    print("The Area of Square is ",square(s))
elif i == 4:
    h = float(input("Enter Height: "))
    b = float(input("Enter Base: "))
    print("The Area of Triangle is",triangle(b,h))
else:
    print("##INVALID INPUT##")