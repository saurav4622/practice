#WAPP to print Fibonacci Series
def  fibonacci(n):
    a, b = 0, 1
    print(a)
    print(b)
    while(a < n-3):
        c = a+b
        print(c)
        a = b
        b = c

limit = int(input("Enter Range: "))
fibonacci(limit)