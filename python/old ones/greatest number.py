while True:
	a=float(input('enter your first number.:'))
	b=float(input('enter your second number.:'))
	c=float(input('enter your third number.:'))
	if a>b>c or a>c>b:
		print(a,'is the greatest number.')
	elif b>a>c or b>c>a:
		print(b,'is the greatest number.')
	elif c>b>a or c>a>b:
		print(c,'is the greatest number.')