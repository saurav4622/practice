while True:
	a=str(input('enter your stream.:'))
	if a=='commerce':
		print('dont know')
	elif a=='science':
		str1=str(input('enter your subject pcm or pcb.:'))
		if str1=='pcm':
			p=float(input('enter your marks of physics.:'))
			c=float(input('enter your marks of chemistry.:'))
			m=float(input('enter your marks of maths.:'))
		elif str1=='pcb':
			p=float(input('enter your marks of physics.:'))
			c=float(input('enter your marks of chemistry.:'))
			m=float(input('enter your marks of bio.:'))
		e=float(input('enter your marks of english.:'))
		o=str(input('enter comp or phy.:'))
		if o=='comp':
			com=float(input('enter your comp marks.:'))
		elif o=='phy':
			com=float(input('enter your marks of physical.:'))
		total=(p+c+m+e+com)/500
		if total>60:
			print('you places first division your marks are',total)
		elif 60>=total>=50:
			print('you places second division your marks are',total)
		elif 50>total>=40:
			print('you places third division your marks are',total)
		elif 40>total>=29:
			print('you passed the exam your marks are',total)
		else:
			print('you failed the exam better luck next time')
	
	
			
			
			
		