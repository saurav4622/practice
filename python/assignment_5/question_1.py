#write a Python Program to take a List (user input) and show it's sum and average.
numbers = list(map(int, input("Enter numbers: ").split()))
sums = 0
product = 1
for i in range(len(numbers)):
    sums = sums + numbers[i]
    product = product * numbers[i]
print(f"Sum : {sums} || Product : {product}")
