import string
count = 0
str = "My name is Sourabh Parui I study in Techno India Hoohgly!!"
for i in str:
    if i in string.punctuation:
        count += 1
print("Total Puntuation:", count)