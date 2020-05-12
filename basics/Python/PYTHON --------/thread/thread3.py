import threading
import time
def send():
	for x in range(5):
		print(x,"Hello",time.ctime())
		time.sleep(1)
def recive():
	for i in range(5):
		print(i,'World',time.ctime())
		time.sleep(2)

obj1 = threading.Thread(name="A",target=send)		
obj2 = threading.Thread(name="B",target=recive)		
obj1.start()
obj2.start()
