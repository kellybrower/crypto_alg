def fast(N, g, A):
	a = g  #set a to g
	b = 1  #set b to 1
	while A>0:  #as long as A > O
		if A % 2 == 1:	#if A is odd
			b = (b*a) % N	#then b is b times a mod N
		a = (pow(a, 2)) % N #a gets squared mod N
		A = A//2 #A gets cut in half and rounded down
	return b #once A = 0, return b, this is g^A mod N