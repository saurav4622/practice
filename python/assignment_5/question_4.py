#write a python program to take a list (user input) and delete duplicate elements from the list.
numbers = list(map(int, input("Enter numbers: ").split()))
duplicate = []
for num in numbers:
    if num not in duplicate:
        duplicate.append(num)
print(duplicate)
