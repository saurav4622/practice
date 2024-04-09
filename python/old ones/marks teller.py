while True:
	a=float(input('enter your marks.:'))
	if 100>=a>=60:
		print('first division')
	elif 50<=a<60:
		print('second division')
	elif 40<=a<50:
		print('third division')
	elif a>100:
		print('a person cannot score more than 100..you stupid..!!!')
	else:
		print('failed.better luck next time..!!')