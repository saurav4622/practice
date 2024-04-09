#In a certain company, the commission of sales persons is calculated as per the following rules:
print(" ::: COMMISSION MANAGER ::: ")
nm=str(input(" Please enter your name :- "))
print("nice to meet you",nm)
print("As per the company guidelines you will receive a certain amount based on your sales report ")
sls=int(input(" What is your estimated sales amount :- "))
print("Well",sls,"it's quite good amount ")
# pa = the amount company have to pay to this employee 
if sls<5000:
    print("Your final amount is ",sls*5/100)
elif sls<=7500:
    print("Your final amount is",(sls*10/100)+100)
elif sls>10000:
    print("Your final amount is",sls*15/100)
print("Thank you",nm,"for the contribution")