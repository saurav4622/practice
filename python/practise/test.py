def abbreviations(name):
    new = name.split()
    abb = ""
    for word in new:
        abb += word[0].upper()
    print(".".join(abb))

string = "techno india hooghly"
abbreviations(string)