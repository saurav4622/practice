#write a Python program to take a  List (user given) and count total number of even and odd numbers.
numbers = list(map(int, input("Enter Numbers: ").split()))
even = []
odd = []
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f"Even numbers: {even} || Odd: {odd}")
