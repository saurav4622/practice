a = "ITISWHATITIS"
character = input("Character: ")
n = int(input("position: "))
string = a[:n-1] + character + a[n:]
print(string)