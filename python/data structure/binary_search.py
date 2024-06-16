def binary_search(arr, target):
    low = 0
    up = len(arr)-1
    while low <= up:
        mid = (low+up)//2
        if arr[mid] == target:
            return mid
        else:
            if arr[mid] < target:
                low = mid+1
            else:
                up = mid-1
        low += 1


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)

key = int(input("Enter a number to search: "))
binary_search(list1, key)
