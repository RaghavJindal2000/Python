from threading import Thread
class Sample(Thread):
	def run(self):
		for i in range(10):
			print(i,"Hello World",Thread.getName(self))
obj1 = Sample(name="A")
obj2 = Sample(name="B")
obj1.start()
obj2.start()			