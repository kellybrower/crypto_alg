#a function that prints 
#the sequence of numbers n**2
def sq(n):
	a = 0
	for a in range(n):
		a = a + 1
		a =  a**2
		print(a, end=' ')
	print()
sq(100)
