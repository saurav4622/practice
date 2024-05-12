#write a recursive function to :-
# 1. Find the sum of the digits of the number.
# 2. Print a number in reverse form
# 3. Convert a Decimal number to its equivalent binary number.
def digit_sum(num):
    new = 0
    while num > 0:
        a = num % 10
        new = new + a
        num = num // 10
    return new
number = int(input("Enter a number: "))
print(digit_sum(number))
