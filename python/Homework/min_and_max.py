def max(one,two,three):
    if((one>two>three) or (one>three>two)):
        print(one,"is the greatest")
    elif((two>one>three) or (two>three>one)):
        print(two,"is the greatest")
    elif((three>one>two) or (three>two>one)):
        print(three,"is the greatest")
    else:
        print("No number is greater")
        
def min(one,two,three):
    if((one<two<three) or (one<three<two)):
        print(one,"is the lowest")
    elif((two<one<three) or (two<three<one)):
        print(two,"is the lowest")
    elif((three<one<two) or (three<two<one)):
        print(three,"is the lowest")
    else:
        print("No number is lower")
              
print("## MINIMUM or MAXIMUM ##")
choice = int(input("1.MINIMUM\n2.MAXIMUM\nEnter your Choice: "))

if (choice == 2):
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    third = int(input("Enter third number: "))
    max(first,second,third)
elif(choice == 1):
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    third = int(input("Enter third number: "))
    min(first,second,third)
else:
    print("INVALID CHOICE")