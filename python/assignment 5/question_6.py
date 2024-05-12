#write a Python Program to take a List (user input) and separate positive and negative elements of the list and print it.
numbers = list(map(int, input("Enter numbers: ").split()))
negative = []
positive = []
for num in numbers:
    if num < 0:
        negative.append(num)
    else:
        positive.append(num)
print(f"Negative: {negative} || Positive: {positive}")
