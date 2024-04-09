def gcd(num1,num2):
    i = 1
    if num1 > num2:
        check = num1
    else:
        check = num2
    while(i<=check):
        if(num1 % i==0) and (num2 % i==0):
            gcd = i
        i += 1
    print("GCD of 2 numbers:",num1,"&",num2,"=",gcd)
    
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
gcd(num1,num2)