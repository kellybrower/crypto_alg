def sqrt2(a, n):
	'''returns the 2^k solutions to x^2 = a mod n
		where n = p1*...pk for pj distinct odd prime'''
	[*x1]= [i for i in range(n) if pow(i,2,n) == a]
	return x1