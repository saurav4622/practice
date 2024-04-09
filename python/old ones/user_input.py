
i = 1
while i == 1:
    a = input("Enter Y or N: ")
    a= a.upper()# Prompt the user for input
    if a != "Y" and a != "N":
        print("Invalid Input. Try Again.")
    else:
        print("Your Data is stored.")
        i = 0  # Break out of the while loop if the input is valid
