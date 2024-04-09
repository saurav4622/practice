print("======================")
print("         MENU")
print("======================")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("======================")
a=int(input("enter your option here: "))
sum1=float(input("enter your first number: "))
sum2=float(input("enter your second number: "))
if a==1:
    print("your sum will be =",sum1+sum2)
elif a==2:
    print("your differnce will be =",sum1-sum2)
elif a==3:
    print("your product will be =",sum1*sum2)
elif a==4:
    print("your division will be =",sum1/sum2)
else:
    print("INVALID INPUT MF..!!")
    