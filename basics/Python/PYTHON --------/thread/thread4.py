import threading
import time
st=time.time()
def home():
	for x in range(5):
		print(x,'Hello',time.ctime())
		time.sleep(2)
		w=threading.Thread(target=index)		
		w.start()
def index():
	for x in range(5):
		print(x,'world',time.ctime())
		time.sleep(1)

q=threading.Thread(target=home)		
q.start()