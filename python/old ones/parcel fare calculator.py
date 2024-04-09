print("TELEPHONE BILL CALCULATOR")
nm=str(input("Please enter your name:-"))
print("Welcome to YODAPHONE",nm)
# cc = the total number of calls 
cc=int(input("Total number of calls :- "))
if cc<=75:
    print("The total payable amount is :- 250 rs.")
elif cc<=150:
    print("The total payable amount is :-",250+((cc-75)*80/100))
elif cc<=225:
    print("The total payable amount is :-",250+(((75*80/100)+cc-150)*1.00))
else:
    print("The total payable amount is :-",250+((75*80/100)+75*1.00)+(cc-225)*1.20)
    