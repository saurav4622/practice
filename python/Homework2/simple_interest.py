#Write a python program to find the simple interest
pa = float(input("Enter the Principle Amount: ₹"))
ri = float(input("Enter the Rate of Interest (in percentage): "))
time = float(input("Enter the Time Period (in years): "))
si = (pa * ri * time)/100
print("The Simple Interest is : ₹", si)