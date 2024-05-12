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

def decimal_to_binary(num):
    binary = []
    while num > 0:
        a = num % 2
        binary.append(a)
        num = num // 2
    binary.reverse()
    changing = list(map(str, binary))
    changed = "".join(changing)
    return changed

number = 8439
print(digit_sum(number))
print(reverse(number))
print(decimal_to_binary(number))