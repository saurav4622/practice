string = "my name is Sourabh"
sub = "am"
flag = 0

for i in range(len(string)):
    if (string[i:i+len(sub)]) == sub:
        flag += 1

print("The occurrence of your Sub-string: " + sub + " in String: " + string + " is " + ' " ' + str(flag) + ' " ')
