
print("DISCOUNT COUNTER")
amount = float(input("Enter your Purching Amount: "))
if (amount < 5000):
    total = amount - (amount*(5/100))
    print("Your Total after 5% discount will be: ₹",total)
elif (5000 <= amount <= 7500):
    total = amount - (amount*(10/100))
    print("Your Total after 10% discount will be: ₹",total)
elif (7501 <= amount <= 10000):
    total = amount - (amount*(15/100))
    print("Your Total after 15% discount will be: ₹",total)
else:
    total = amount - (amount*(20/100))
    print("Your Total after 20% discount will be: ₹",total)
