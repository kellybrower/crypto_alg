def sqrtmod(a1, a2, p1, p2):
	'''returns the 4 residues from a pair of modulos'''
	if p1 % 4 == 3 and p2 % 4 == 3:
		x = pow(a1, (p1+1)//4,p1)
		neg_x = -pow(a1, (p1+1)//4, p1)
		y = pow(a2, (p2+1)//4, p2)
		neg_y = -pow(a2, (p2+1)//4, p2)
		sqrts = [x, neg_x, y, neg_y]
		return sqrts
		
	else:
		print('nope')

def squaremod(sqrts, a1, a2, p1, p2):
	x = sqrts[0]
	y = sqrts[2]
	if p1>p2:
		while pow(x,2) % p2 != a2:
			x += p1
		return x
	else:
		while pow(y,2) % p1 != a1:
			y += p2
		return y
		
	