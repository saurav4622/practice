#this program is genrated on 2-september-2020
while True:
	a=str(input('enter in which term you want to take the area.:'))
	f=str(input('enter your unit.:'))
	if a=='rectangle':
		b=(float(input('enter len.:')))
		c=(float(input('enter breadth.:')))
		print('your answer will be',b*c,f)
	elif a=='square':
		d=float(input('enter your sides.:'))
		print('your answer will be',d**2,f)
	elif a=='circle':
		e=float(input('enter your radius.:'))
		print('your answer will be',3.14*e**2,f)
	elif a=='triangle':
		g=float(input('enter your height.:'))
		h=float(input('enter your base.:'))
		print('your answer will be',1/2*g*h,f)
	else:
		print('bhaisahab isse jada nhe aata programmer hu mathematician nhe.')
	print('thanks for coming...!!!')