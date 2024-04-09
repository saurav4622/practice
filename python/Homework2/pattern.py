#write a python program to print the following output.
def pattern1(limit):
    for i in range(1,limit+1):
        print(i*5,end=" ")
    print("\n")
    
def pattern2(limit):
    i = 1
    j = 2
    sum = 0
    while(i<=limit):
        print(j,end=" ")
        sum += j
        j += 3
        i += 1
    print("\nsum =",sum,"\n")
    
def pattern3(limit):
    i = 1
    j = 1
    sum = 0
    while(i<=limit):
        print(j,end=" ")
        sum += j
        j = j*10+1
        i += 1
    print("\nsum =",sum,"\n")
    
def pattern4(limit):
    i =1
    j = 1
    jump = 0
    sum = 0
    while(i<=limit):
        print(j,end=" ")
        sum += j
        jump  += 1
        j += jump
        i+=1
    print("\nsum =",sum,"\n")

def pattern5(limit):
    i = 1
    j = 1
    power = 1
    sum = 0
    while(i<=limit):
        product = j**power
        print(product,end=" ")
        power += 1
        sum += product
        j += 2
        i += 1
    print("\nsum =",sum)
            
limit = int(input("Enter range: "))
pattern1(limit)
pattern2(limit)
pattern3(limit)
pattern4(limit)
pattern5(limit)