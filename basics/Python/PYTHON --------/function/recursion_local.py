def display(a):
	a=a+1 
	print(a,"In Display function")
	if(a<5):
		display(a)
	print(a,"Back to display")
print("In Main")
display(0)
print("Back to main")
'''
5.Back to main
4.Back to main
3.Back to main
2.Back to main
1.Back to main
'''