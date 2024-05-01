def odd_even(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

def perfect_number(n):
    sum_1 = 0
    for i in range(1, n):
        if n % i == 0:
            sum_1 = sum_1 + i
    if sum_1 == n:
        print("Perfect number")
    else:
        print("Non-Perfect number")

def peterson(n):
    copy = n
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact = fact * i
        return fact
    new_num = 0
    while n > 0:
        new = n % 10
        new_num = new_num + factorial(new)
        n = n // 10
    if copy == new_num:
        print("{} is a Peterson number".format(new_num))
    else:
        print("{} is not a Peterson number".format(copy))

def armstrong(n):
    copy = n
    sum = 0
    power = len(str(n))
    while n > 0:
        digit = n % 10
        sum += digit ** power
        n = n // 10
    if sum == copy:
        print("{} is an armstrong number".format(copy))
    else:
        print("{} is not an armstrong number".format(copy))


print("::::::::::::::::::::::::::::::::::::")
print("1.Odd or Even\n2.Perfect number\n3.Peterson Number\n4.Armstrong Number\n5.Quit")
print("::::::::::::::::::::::::::::::::::::")
i = 1
while i > 0:
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Quitting from the menu...")
        break
    elif choice > 5 or choice < 1:
        print("Invalid choice... Please Try Again (Press 5 to Quit)")
        continue

    number = int(input("Enter a number: "))

    if choice == 1:
        odd_even(number)
    elif choice == 2:
        perfect_number(number)
    elif choice == 3:
        peterson(number)
    elif choice == 4:
        armstrong(number)
