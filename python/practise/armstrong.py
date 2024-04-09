def armstrong(num1):
    sum = 0 #sum setted to zero for initiallization
    temp = num1  #temp setted to check the value in if else statement
    power = len(str(num1))  #length is used to determine the power of the sum
    while(num1>0):   #the loop will execute until the value of num1 is less than or equal to zero
        a = num1 % 10  #here a is storing the reminder of the inputted number.
        sum = sum + (a ** power)   #sum is storing the sum of the value with the reminder for taking the last digit from the right one by one and performing exponential operation and sumition.
        num1 = num1 // 10   #decresing the value of num1
        
    if(sum == temp):
        result = "Armstrong number"
    else:
        result = "Not an Armstrong Number"
    
    return result
                  
    
arm = int(input("Enter a number: "))  #input is taken
print(armstrong(arm))  #function is called
