#Write a python program to find the simple interest
pa = float(input("Enter the Principle Amount: ₹"))
ri = 6.5
time = float(input("Enter the Time Period (in years): "))
si = (pa * ri * time)/100
print("The Simple Interest is : ₹", si)