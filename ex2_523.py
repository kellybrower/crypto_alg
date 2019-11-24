def n_tri(a):
	"""compute the nth trianglular number without the formula"""
	i = 0
	b = 0
	while i < a:
		i+=1
		b+=i
	return b