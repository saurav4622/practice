#Write a program to find the area and perimeter of the circle
pie = 3.14
radius = float(input("Enter Radius: "))
area = pie * (radius**2)
perimeter = 2 * pie * radius
print("Perimeter: ",perimeter, "\nArea: ", area)