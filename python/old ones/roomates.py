while True:
	str1=str(input('your friend is visiting:'))
	if str1=='yes':
		print('city tour')
	elif str1=='no':
		str2=str(input('room mate free:'))
		if str2=='yes':
	 		print('play fifa')
		elif str2=='no':
			str3=int(input('money in pocket.:'))
			if str3>=500:
				print('eat out in a restaurant.')
			elif 200<=str3<=300:
				print('eat in hostel cafe')
			elif str3<=100:
				print('eat maggie noodles')