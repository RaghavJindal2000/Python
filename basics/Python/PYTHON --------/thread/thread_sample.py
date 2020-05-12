import threading
import time
class Sample(threading.Thread):
	def run(self):
		for a in range(10):
			print(a,threading.currentThread().name,time.ctime())
			time.sleep(1)	
o=Sample(name="A")
ob=Sample(name="B")
o.start()
ob.start()