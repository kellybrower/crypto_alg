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

def minv(m1, m2):
	"""returns m1 inverse and m2 inverse modulo m1"""
	ig,u,v = xgcd(m1, m2)
	m1inv = u
	m2inv = v % m1
	return m1inv, m2inv
	

def chinese_rem(a1, a2, m1, m2):
	"""The chinese remainder algorithm for two equivalences:
	returns x such that x is a solution to a1 = x mod m1 and a2 = x mod m2
	"""
	m1inv, m2inv  = minv(m1, m2)
	x = ((a1*(m2inv)*m2) + (a2*(m1inv)*m1)) % (m1*m2)
	return x
	
	
	
