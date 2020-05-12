import threading

class Sample(threading.Thread):
	def run(self):
		for i in range(10):
			if i==5:
				self.stop()
			print("hello")
	def stop(self):
		self.running = False
obj = Sample()
obj.start()			
obj.stop()