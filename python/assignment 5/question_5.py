#write a Python program to take a  List (user given) and count total number of even and odd numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f"Even numbers: {even} || Odd: {odd}")