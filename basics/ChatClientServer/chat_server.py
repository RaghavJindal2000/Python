import socket, threading
def accept_client():
	while True:
		cli_sock, cli_add = ser_sock.accept()
		uname = cli_sock.recv(1024)
		CONNECTION_LIST.append((uname, cli_sock))
		print(CONNECTION_LIST)
		print('%s is now connected' %uname)
		thread_client = threading.Thread(target = broadcast_usr,
													args=[uname, cli_sock])
		thread_client.start()
def broadcast_usr(uname, cli_sock):
    while True: 
        try:
            data = cli_sock.recv(1024)
            if data:
                print (uname,"Spoke",data)
                b_usr(cli_sock, uname, data)
        except Exception as x:
            print(x)
            break
def b_usr(cs_sock, sen_name, msg):
    for client in CONNECTION_LIST:
        if client[1] != cs_sock:
            client[1].send(sen_name)
            client[1].send(msg)
		
CONNECTION_LIST = []
ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = 'localhost'
PORT = 50243
ser_sock.bind((HOST, PORT))
ser_sock.listen(1)
print('Chat server started on port : ',PORT)
thread_ac = threading.Thread(target = accept_client)
thread_ac.start()

'''
Here we made a socket instance and passed it two parameters. 
The first parameter is AF_INET and the second one is SOCK_STREAM. 
AF_INET refers to the address family ipv4.
The SOCK_STREAM means connection oriented TCP protocol.
'''