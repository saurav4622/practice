numbers = list(map(float,input("Enter numbers using space:\n").split()))
length = len(numbers)
average = sum(numbers)/length
print("The Average of your numbers {} is {}".format(numbers, average))
