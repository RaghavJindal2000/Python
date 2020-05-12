import socket,threading
s=socket.socket()
host='localhost'
port=12345
s.bind((host,port))
s.listen(5)
c,addr=s.accept()
print(c)
print("got connection",addr)

def broadcast():
	while True:
		message=input()
		if message:
			c.send(str.encode(message))
			
th = threading.Thread(target=broadcast)
th.start()

while True:
		data=c.recv(1000)
		print(data)
c.close()
'''
Here we made a socket instance and passed it 
two parameters. 
The first parameter is AF_INET and the second 
one is SOCK_STREAM. 
AF_INET refers to the address family ipv4.
The SOCK_STREAM means connection oriented TCP 
protocol.
'''