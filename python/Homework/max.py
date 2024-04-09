#Maximum among five numbers
one = int(input("Enter 1st value: "))
two = int(input("Enter 2nd value: "))
three = int(input("Enter 3rd value: "))
four = int(input("Enter 4th value: "))
five = int(input("Enter 5th value: "))
if (one > two) & (one > three) &  (one > four) & (one > five):
    print ("The maximum number is ", one)
elif (two > one) & (two > three) &  (two > four) & (two < five):
    print("The maximum number is ", two)
elif (three > one) & (three > two) & (three > four) & (three > five):
    print("The maximum number is ", three)
elif (four > one) & (four > two) & (four > three) & (four > five):
    print("The maximum number will be", four)
elif (five > one) & (five > two) & (five > three) & (five > four):
    print("The maximum number will be", five)
else:
    print("All Numbers are equal")