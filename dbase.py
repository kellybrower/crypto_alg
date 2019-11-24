def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    aye = a
    bee = b
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    while x0 < 0:
    	x0, y0 = x0 + bee//b, y0 - aye//b #condition make u the smallest postive
    return b, x0, y0

def gcd(a,b):
	while b:
		a, b = b, b//a
	return a
		
def dbase(e,c,p):
	''' Returns solution x 
		such that x^e = c mod p where p is prime'''
	d = pow(e,p-2,p-1)
	return pow(c,d,p)
	

def dbase_comp(e,c,N):
	''' Returns solution x
		such that x^e = c mod N where N = p*q for dif primes p, q.'''
	j = 0
	k = 0
	#find the factors of N (there's only two by assumption)
	for i in range(2,N):
		if N % i == 0 and j == 0:
			j = i
		if N % i == 0 and j != 0:
			k = i
	lcm = ((j-1)*(k-1))//(gcd(j-1, k-1)) 
	for l in range(2, lcm):
		if (l*e) % lcm == 1:
			d = l
	return pow(c,d,N)
	
def dbase_comp_x(e,c,N):
	''' Returns solution x
		such that x^e = c mod N where N = p*q for dif primes p, q.'''
	j = 0
	k = 0
	#find the factors of N (there's only two by assumption)
	for i in range(2,N):
		if N % i == 0 and j == 0:
			j = i
		if N % i == 0 and j != 0:
			k = i
	phi = (j-1)*(k-1)
	_,d,_ = xgcd(e, phi)
	return pow(c,d,N)