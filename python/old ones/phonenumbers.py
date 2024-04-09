import phonenumbers
from phonenumbers import geocoder
a=input("enter your phone number here: ")
phonenumber=phonenumbers.parse(a)
print(geocoder.description_for_number(phonenumber,'en'))