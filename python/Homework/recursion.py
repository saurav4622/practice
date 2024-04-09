def digit_sum(number):
    sum= 0
    add = 0
    while(number>0):
        a = number % 10
        sum = sum * 10 + a
        add = add + sum
        number = number // 10
    print("The reverse of the number:",sum, "and the sum is",add)

number = int(input("Enter your number: "))
digit_sum(number)
