
def first_top(thickness,c):
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
        
def upper_pillar(thickness,c):
    for i in range(thickness):
        print((c*thickness).center(thickness*2,)+(c*thickness).center(thickness*6))
        
def middle_belt(thickness,c):
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))
        
def lower_pillars(thickness,c):
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
        
def lower_top(thickness,c):
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
        
wid = int(input())
char = 'H'
first_top(wid,char)
upper_pillar(wid,char)
middle_belt(wid,char)
lower_pillars(wid,char)
lower_top(wid,char)

