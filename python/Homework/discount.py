#1.  In a shop, a discount of 10% on purchase amount is given only if purchase amount exceeds Rs. 5000. Find net payable amount.
def discount(amount):
    deduct = amount * ((10)/100)
    result  = amount - deduct
    return result

print("DISCOUNT COUNTER")
amount = float(input("Enter your Purching Amount: "))
if (amount < 5000):
    print("Your Total will be:",amount)
else:
    print("Your Total will be:",discount(amount))
