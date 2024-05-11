#write a python program to take a list (user input) and sort it and after that reverse it, print both results.
def sorting(number, n):
    if n == 1:
        return
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            number[i], number[i + 1] = number[i + 1], number[i]
    sorting(number, n - 1)
    return number

def reverse(number, n):
    return number[::-1]

numbers = list(map(int, input("Enter the list of numbers: ").split()))
print(f"Sorted Elements: {sorting(numbers, len(numbers))} || Reversed Elements: {reverse(numbers, len(numbers))}")
