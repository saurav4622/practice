#this code is generated on 14th feb,2022.
print('Hello there.!! ')
name=str(input('enter your name='))
print('choose one of them below')
print('1.birth year')
print('2.age')
a2=int(input('(1/2)='))
if a2==2:
	current_age=int(input('enter your current age='))
	recent_year=int(input('enter current year='))
	desired_year=int(input('enter in which year you want to know your age='))
	a1=desired_year-recent_year
	
	b1=current_age+a1
	print('So',name.capitalize(),'your age in ',desired_year,'will be',b1)
elif a2==1:
	b2=int(input('enter your birth year='))
	recent_year=int(input('enter current year='))
	desired_year=int(input('enter in which year you want to know your age='))
	a1=desired_year-recent_year
	b3=recent_year-b2
	b4=b3+a1
	print('So',name.capitalize(),'your age in',desired_year,'will be',b4)
else:
	print('#404 error# \n%invalid input%') 

	
