#write a recursive function to :-
# 1. Find the sum of the digits of the number.
# 2. Print a number in reverse form
# 3. Convert a Decimal number to its equivalent binary number.
def digit_sum(num):
    if num == 0:
        return 0
    else:
        new = num % 10 + digit_sum(num // 10)
        return new

def reverse(num, new=0):
    if num == 0:
        return new
    else:
        last_digit = num % 10
        new = new * 10 + last_digit
        return reverse(num // 10, new)

number = 8439
print(digit_sum(number))
print(reverse(number))
