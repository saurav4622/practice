#this program is generated in june 7 2021 at 12:12 pm.
print('welcome to programed calculator.let us begin with selecting which type of calculation you want please select below.!!')#this is the normal statement ehich will be displayed to the user..
def add(x,y):
    c=x+y                #this is the program which can be used as a additional function
    return c
def sub(x,y):
    c=x-y
    return c
def div(x,y):
    c=x/y
    return c
def multi(x,y):
    c=x*y
    return c
    
print('1.add')
print('2.subtract')
print('3.division')
print('4.multiplication')
z=input('enter which term you want:.(1,2,3,4)=')
a=float(input('enter your first number='))
b=float(input('enter your second number='))
if z=='1':
    print('''your sum will be''',add(a,b))
elif z=='2':
    print('your difference will be',sub(a,b))
elif z=='3':
    print('your multiplication will be',div(a,b))
elif z=='4':
    print('your division will be',multi(a,b))
else:
    print('%invalid input@')

print('thanks for visiting..!!! please provide feedback below..') 
input('you can give your feedback here.=')
    