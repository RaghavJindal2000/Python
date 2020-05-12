f=open("temp.txt","a")
while True:
	a=input("Enter exit to exit\nEnter the Message to Write into File :")
	if(a=="exit"):
		break
	else:
		f.write(a)     
f.close()
f=open("temp.txt","r")
print(f.read())
