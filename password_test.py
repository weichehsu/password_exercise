#密碼重試程式
password = 'a123456'
number = 0
while number<3:
	user_password = input('請輸入密碼: ')
	number = number + 1
	if user_password == password:
		print('登入成功')
		break
	else:
		if 3-number > 0:
			print('密碼錯誤! 還有', 3-number, '次機會')
		else:
			print('登入失敗!')

