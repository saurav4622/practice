#write a python program to take a list and show its minimum and maximum elements and its difference.
def max_min(a):
    min = a[0]
    max = a[len(a)-1]
    for nums in a:
        if nums < min:
            min = nums
        elif nums > min:
            if nums > max:
                max = nums
    return f"{max - min} is the difference between {min} and {max}"

numbers = list(map(int, input("Enter integers:").split()))
print(max_min(numbers))
