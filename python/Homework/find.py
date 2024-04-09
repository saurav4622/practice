import string as str
def check(string):
    vowel = punches = consonant = white_spaces = digit =0
    vowels = ['a','e','i','o','u']
    for char in string:
        if char.lower() in vowels:
            vowel += 1
        elif char in str.punctuation:
            punches += 1
        elif ' ' in char:
            white_spaces += 1
        elif char in str.digits:
            digit += 1
        else:
            consonant += 1
    print("Total vowels:",vowel)
    print("Total Puntuations:",punches)
    print("Total White Spaces:",white_spaces)
    print("Total Digits:",digit)
    print("Total Consonants:",consonant)
    
new_string = input("Enter String:\n")
print("===========================")
check(new_string)
print("===========================")
