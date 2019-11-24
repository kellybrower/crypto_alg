#oreviously seen on web https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Python
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

def congruential_pub(q,f,g):
	ig, f_inv, ig = xgcd(f,q)
	h = (f_inv * g) % q
	print('This is Alice\'s public key:', h)
	e = 619168806
	a = (f*e) % q
	p = (f_inv * a) % g
	print('This is Bob\'s plain text:', p)
	m = 10220
	r = 19564
	c = (r*h + m) % q
	print('This is Bob\'s encrypted text:', c)

'''
Kellys-MacBook-Pro:mystuff kellybrower$ python3 -i congruential.py
>>> congruential_pub(918293817,19928,18643)
This is Alice's public key: 767748560
This is Bob's plain text: 962
This is Bob's encrypted text: 619167208
>>> 
'''