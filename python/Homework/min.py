#minimum between three
first = int(input("Enter First: "))
second = int(input("Enter Second: "))
third = int(input("Enter Third: "))
if (first < second) & (first < third):
    print("The smallest number is ", first)
elif (second < first) & (second < third):
    print("The smallest number is ", second)
elif (third < first) & (third < second):
    print("The smallest number is ", third)
else:
    print("Three Numbers are equal")