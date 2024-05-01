def fibonacci(n):
    a,b = 0,1
    print(a)
    print(b)
    for i in range(n-2):
        a,b = b,a+b
        print(b)
n = int(input("Enter a number: "))
fibonacci(n)