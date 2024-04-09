import math
a=str(input("enter your name here: "))
b=float(input("enter your weight in kg here: "))
print("enter your height: ")
c=float(input("(feet):-"))
d=float(input("(inch):-"))
ht=(c/12)+d
print(math.trunc(ht),"is your height in meters")
