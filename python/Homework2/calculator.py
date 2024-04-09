#Write a Python program to add, subtract, product and division of two numbers.
choice = int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter your choice:"))
a = int(input("Enter First Number: "))
b = int(input("Enter Second number: "))
if choice == 1:
    print("Addition",a+b)
elif choice == 2:
    print("Subtraction",a-b)
elif choice == 3:
    print("Multiplication",a*b)
elif choice == 4:
    print("Division",a/b)
else:
    print("Invalid Input")