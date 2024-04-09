import math  #importing maths module to work on some of it's function
float=12.9843279
print(math.trunc(float))   #this function is used to print only integer part removing the values of decimal
print(math.ceil(float))   #this function is used to return the smallest integer greater than the number.
print(math.floor(float))   #this function will return the greatest integer smaller that the number.
f='{0:.3g}'.format(float)  
print(f)
print(round(float))         #this function will round of the number.
print(round(float,2))