#write a function to:-
# 1. count number of words in a string.
def counting(name):
    count = 0
    for letter in name:
        if letter == " ":
            continue
        count += 1
    print(f"Total number of letters: {count}")

# 2. count number of vowels and consonants in a string.
def vowels_count(name):
    name.lower()
    vowels = 0
    consonants = 0
    for letter in name:
        if letter in "aeiou":
            vowels += 1
        else:
            consonants += 1
    print(f"Total Vowels: {vowels} || Total Consonants: {consonants}")

# 3. Find the full abbreviation of a name. (Ex. techno India Hooghly => T.I.H)
def abbreviations(name):
    new = name.split()
    abb = ""
    for word in new:
        abb += word[0].upper()
    print(f"{name} => {".".join(abb)}")

string = input("Enter a string: ")
counting(string), vowels_count(string), abbreviations(string)
