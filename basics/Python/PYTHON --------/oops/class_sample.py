class Sample:
	"This is help."
	def example(self):
		'Hello World'
		print("Hello")
	def __str__(self):
		return "Hello World"
a=Sample()
print(help(a))
