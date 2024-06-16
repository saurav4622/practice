def linear_search(array, item):
    for i in range(0, len(array)):
        if array[i] == item:
            return i
    return -1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
key = int(input("Enter a item to search: "))
result = linear_search(list1, key)
if result == -1:
    print("Element not found")
else:
    print("Element found at index", result+1)
