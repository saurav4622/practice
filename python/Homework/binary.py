def binary(number):
    rems = []
    while(number>1):
        div = number % 2
        rems.append(div)
        number = number // 2
    rems.reverse()
    new_num = ''.join(map(str,rems))
    new_binary = int(new_num)
    print(new_binary)
    
a = int(input("Enter a decimal number : "))
binary(a)
        