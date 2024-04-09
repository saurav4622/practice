#WAPP to find the sum and product of the digits of user.
def  digit_sum(a):
    sum = 0
    while(a > 0):
        b = a % 10
        sum = sum + b
        a = a//10
    print("The sum is :",sum)

def digit_product(a):
    product = 1
    while(a>0):
        b = a % 10
        product = product * b
        a= a // 10
    print("Product =",product)

a = int(input("Enter your number: "))
digit_sum(a),digit_product(a)
