while True:
	a=float(input('enter your amount in rupees.:'))
	b=str(input('enter your desired currency.:'))
	if b == 'dollar':
		print('your amount in dollar is',a/73.25)
	elif b=='dinar':
		print('your amount in dinar is',a/239.92)
	elif b=='euro':
		print('your amount in euro is',a/87.25)
	elif b=='taka':
		print('your amount in taka is',a*1.16)
	elif b=='yuan':
		print('saala desh drohi bhaag yha se')
	elif b=='baht':
		print('your amount in baht is',a/2.37)
	elif b=='bitcoin':
		print('ohho amir log aye hai hamare gareeb khaane mai vese apka amount ',a/856220.62,'beth rha hai')
	else:
		print('kyu bhai vijay malya banne ka shok hai kya')
	print('goodbye!!')
