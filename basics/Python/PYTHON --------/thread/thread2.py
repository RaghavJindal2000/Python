import threading
import time
class myThread (threading.Thread):
	def __init__(self, threadID, name, delay):
		threading.Thread.__init__(self)
		#super().__init__()
		self.threadID = threadID
		self.name = name
		self.delay = delay
		print(threadID,name,delay)
	def run(self):
		print ("Starting " + self.name)
		abcd(self.name, self.delay, 5)
		print ("Exiting " + self.name)
def abcd(threadName, delay, counter):
   while counter>0:
      time.sleep(delay)
      print (threadName, time.ctime())
      counter -= 1
thread1 = myThread(1, "Thread-1", 3)
thread2 = myThread(2, "Thread-2", 1)
thread3 = myThread(3, 'Thread-3', 2)
thread1.start()
thread2.start()
thread3.start()