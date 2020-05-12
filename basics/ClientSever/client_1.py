import socket,threading
s=socket.socket()
host='localhost'
port=12345
s.connect((host,port))
print("connected to",host,"on port",port)

def broadcast():
	while True:
		message=input()
		if message:
			s.send(str.encode(message))
thread_client = threading.Thread(target=broadcast)
thread_client.start()	
while True:
	data=s.recv(2048)
	print(data)	
s.close()