def isvowels(char):
    vowels = ['A','E','I','O','U']
    if char.capitalize() in vowels:
        print("Vowel")
    else:
        print("Consonant")
    
string = input("Enter a Character: ")
isvowels(string)