with open("intro.txt","r")as names_file:
	with open("temp2.txt","r")as body_file:
		body = body_file.read()
	for name in names_file:
		name=names_file.read()
		print(name)
		print(body)
		mail=name+body
	with open("lol.txt",'w+')as mail_file:
		mail_file.write(mail)
#pip install pyinstaller		
#pyinstaller -F --windowed filename.py