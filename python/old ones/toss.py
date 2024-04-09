i=1
a=int(input('how many odds do you want='))
for i in range(0,a):
	l1=['heads','tails']
	import random
	comp=random.choice(l1)
	user=str(input('[heads/tails]='))
	if user==comp:
		print('you won the toss')
	elif user=='heads':
				if comp=='tails':
					print('lost')
	else:
		print('you lost')
i+=1
