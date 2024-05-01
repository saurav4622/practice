#WAPP to check the number is odd or even,palindrome,armstrong,prime,perfect,krishnamurthy or not.
def odd_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


def palindrome(number):
    new = 0
    copy = number
    while (number > 0):
        div = number % 10
        new = new * 10 + div
        number = number // 10
    if (new == copy):
        print("Palindrome")
    else:
        print("Non-Palindrome")


def armstrong(number):
    power = len(str(number))
    copy = number
    result = 0
    while (number > 0):
        div = number % 10
        result = result + pow(div, power)
        number = number // 10
    if (result == copy):
        print("Armstrong number")
    else:
        print("Non-Armstrong number")


def prime(number):
    flag = 0
    i = 2
    while (i <= number):
        if (number % i == 0):
            flag += 1
        i += 1
    if (flag > 1):
        print("Non-prime")
    else:
        print("Prime")


def perfect_number(number):
    i = 1
    sum = 0
    while (i < number):
        if (number % i == 0):
            sum = sum + i
        i += 1
    if sum == number:
        print("Perfect number")
    else:
        print("Non-perfect number")


def krishnamurthy(number):
    def factorial(number):
        i = 1
        sum = 1
        while (i <= number):
            sum = sum * i
            i += 1
        return sum

    new = 0
    copy = number
    while (number > 0):
        a = number % 10
        new = new + factorial(a)
        number = number // 10
    if (new == copy):
        print("Krishnamurthy/Peterson Number")
    else:
        print("Non-Krishnamurthy/Non-Peterson Number")


print("###########Number Checker############")
choice = int(input(
    "1.Palindrome\n2.Armstrong\n3.Prime\n4.Perfect Number\n5.Krishnamurthy Number/Peterson Number\n6.Odd or Even\nEnter your choice = "))
number = int(input("Enter a number: "))
if choice == 1:
    palindrome(number)
elif choice == 2:
    armstrong(number)
elif choice == 3:
    prime(number)
elif choice == 4:
    perfect_number(number)
elif choice == 5:
    krishnamurthy(number)
elif choice == 6:
    odd_even(number)
else:
    print("Invalid choice")
