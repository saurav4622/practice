def abbre(string):
    abb = []
    for i in string:
        if i.isupper():
            abb.append(i)
    a = ".".join(abb)
    print(a)
string = input("Enter the abbreviatit string in capital letters: ")
abbre(string)