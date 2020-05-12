with open("intro.txt",'r') as names_file:
	with open("temp.txt",'r') as body_file:
		body = body_file.read()
	for name in names_file:
		nam=names_file.read()
		print(name)
		print(body)
		mail = nam+body
	with open("hello.txt",'w+') as mail_file:
		mail_file.write(mail)
		#print(mail_file.read())
