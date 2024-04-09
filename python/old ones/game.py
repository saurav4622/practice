my="Saurav"
ty="Type your option here:-"
print("\n")
print("LETS SEE HOW MUCH YOU KNOW YOUR FRIEND...!!!")
print("\n")
print("WHICH GENDER ARE YOU:-")
print("1.Male\n2.Female")
gen=int(input("select(1/2)= "))
name=str(input("enter your name here: "))
sum=0
if gen==1:
    print("lets start Mr.",name.capitalize())
elif gen==2:
    print("lets start Ms.",name.capitalize())
else:
    print("Sorry but we don't have any other gender preferences till..!!",name.capitalize(),"\U0001F607")
    
enter=input("press enter")

print("\n")

print("A.What is",my,"favorite day of the week?")
print("\t1.sunday\n\t2.monday\n\t3.tuesday\n\t4.wednesday\n\t5.thursday\n\t6.friday\n\t7.saturday")
ans1=int(input(ty))
if ans1==7:
    sum=sum+1
else:
    ans="Saurav chose saturday"
    
print("\n")

print("2.Which one will",my," choose?")
print("\t1.beach\n\t2.mountain")
ans2=int(input(ty))
if ans2==1:
    sum=sum+1
else:
    breakpoint

print("\n")

print("B.If",my,"had one wish what would it be?")
print("\t1.unlimited food\n\t2.to be a billionaire\n\t3.have superpowers\n\t4.to be best at everything.")
ans3=int(input(ty))
if ans3==1:
    sum=sum+1
else:
    breakpoint

print("\n")

print("C.What would",my,"likes to do in his/her free time?")
print("\t1.Gymming\n\t2.Shopping\n\t3.Swimming\n\t4.Watching movie\n\t5.Go for a trip\n\t6.Reading\n\t7.Sleeping\n\t8.Netflix and chill")
ans4=int(input(ty))
if ans4==4:
    sum=sum+1
else:
    breakpoint

print("\n")

print("D.Which animal would",my,"wants as a pet?")
print("\t1.Dog\n\t2.Cat\n\t3.Rabbit\n\t4.Turtle")
ans5=int(input(ty))
if ans5==1:
    sum=sum+1
else:
    breakpoint
    
print("\n")

print("E.What does",my,"prefer?")
print("\t1.Tea\n\t2.Coffee")
ans6=int(input(ty))
if ans6==1:
    sum=sum+1
else:
    breakpoint
    
print("\n")

print("F.What is",my,"favorite colour?")
print("\t1.Red\n\t2.Blue\n\t3.Green\n\t4.yellow\n\t5.pink\n\t6.Black\n\t7.White\n\t8.Purple\n\t9.Orange")
ans7=int(input(ty))
if ans7==2:
    sum=sum+1
else:
    breakpoint

print("\n")

print("G.What is more important to",my,"?")
print("\t1.family and friends\n\t2.money\n\t3.love\n\t4.career")
ans8=int(input(ty))
if ans8==1:
    sum=sum+1
else:
    breakpoint

print("\n")

print("H.Which one would",my,"choose?")
print("\t1.sun\n\t2.moon")
ans9=int(input(ty))
if ans9==2:
    sum=sum+1
else:
    breakpoint
    
print("\n")

print("I.Which one brings smile to",my,"face")
print("\t1.call from crush\n\t2.call from buddies\n\t3.call from parents\n\t4.hangout with friends")
ans10=int(input(ty))
if ans10==4:
    sum=sum+1
else:
    breakpoint

print("\n\n")
print("===================================================")
if sum==10:
    print("you are the best friend of",my)
elif 9>=sum>=7:
    print("you are a good friend of",my)
elif 6>=sum>=4:
    print("you might hangout with",my)
else:
    print("you don't know",my)
print("===================================================")
