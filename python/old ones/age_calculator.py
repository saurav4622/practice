while True:
	a=int(input('enter your birth year.:'))
	b=int(input('enter recent year.:'))
	c=b-a
	d=int(input('enter your year in future in which you want to know your age.: '))
	if c<18:
		print('your current age is',c,'you are immature..to use this program. best of luck for your journey.')
	elif 18<c<80:
		print('your current age is',c,'you are eligible to vote.hope you choose the best and look after your family as you are mature now. ')
	else:
		print('your current age is ',c,'now you are an most experienced and old person of the family, look towards your health.')
	print('your age will be', d-a,'in year',d)
	print('thanks for coming..!!!!')