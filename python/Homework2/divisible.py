#write a python program which are divisible by 5 but not 10.
def divisible(num):
    if(num % 5==0 ) & (num % 10!=0):
        print(num)
        
lower = int(input("Enter Lower Limit: "))
upper = int(input("Enter Upper Limit: "))
for i in range(lower,upper+1):
    divisible(i)
