def prime(n):
    flag = 0
    for i in range(2, n+1):
        if n % i == 0:
            flag += 1
    if (flag > 2):
        print("Not Prime")
    else:
        print("Prime")

n = int(input("Enter a number: "))
prime(n)