import calendar
print("what you want to know:-")
print("1.year only")
print("2. year and month")
choice=int(input("enter your choice here:-"))
yy=int(input("enter year in (YYYY) format ="))
if choice==2:   
    mm=int(input("enter month in (MM) format ="))
    print(calendar.month(yy, mm))
elif(choice==1):   
    print(calendar.calendar(yy)) 
else:
    print("INVALID INPUT !!\U0001F612")

year1=int(input("enter your starting year: "))
year2=int(input("enter your ending year: "))
print("leap days=",calendar.leapdays(year1,year2))


