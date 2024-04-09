print("welcome to the Calculator")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
a=int(input("Please select any option from the list ::- "))
b=int(input("Please enter your first number :-"))
c=int(input("Please enter your second number :-"))
if a==1:
    print("Your result is :- ",b+c)
elif a==2:
    print("Your result is :- ",b-c)
elif a==3:
    print("Your result is :- ",b*c)
elif a==4:
    print("Your result is :- ",b/c)
else :
    print("404 ERROR ")