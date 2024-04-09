  
in1 = int(input())
pad = len(bin(in1)[2:])
for i in range(1,in1+1):
    print(str(i).rjust(pad),str(oct(i)[2:]).rjust(pad),str(hex(i)[2:]).upper().rjust(pad),str(bin(i))[2:].rjust(pad))