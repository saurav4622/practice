def length_of_string(astring):
    string = astring.upper()
    count = 0
    vowels = ['A','E','I','O','U']
    vowel = 0
    consonant = 0
    space = 0
    for i in string:
        count += 1
        if  i in vowels:
            vowel += 1
        elif ' ' in i:
            space += 1
        else:
            consonant += 1
    print("Total Characters =",count,"\nTotal Vowels =",vowel,"\nTotal Consonants =",consonant,"\nTotal white-spaces =",space)
            
string = input("Enter a String: \n")
print("==========================")
length_of_string(string)