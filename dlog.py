def fast(N, g, A):
	a = g  #set a to g
	b = 1  #set b to 1
	while A>0:  #as long as A > O
		if A % 2 == 1:	#if A is odd
			b = (b*a) % N	#then b is b times a mod N
		a = (pow(a, 2)) % N #a gets squared mod N
		A = A//2 #A gets cut in half and rounded down
	return b #once A = 0, return b, this is g^A mod N

def dlog(N, g, A):
	dad = [] #store powers of g in a list	

	for i in range(1, A): # create the powers of g
		dad.append(fast(N, g, i))
	if A in dad: #the element of the list that matches the exponent is the logarithm
		return dad.index(A) + 1 #add one because python starts at 0
	else:
		print('it ain\'nt here, babe') #you're out of luck