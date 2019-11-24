def binsearch(A, T):
	'''typical binary search'''
	L = 0
	R = len(A)
	while L<=R and A:
		m = (L+R)//2
		if A[m] < T:
			L = m + 1
		elif A[m] > T:
			R = m - 1
		else:
			return m	
def fast(N, g, A):
	'''find g^{A} mod N using successive squares algorithm'''
	a = g  #set a to g
	b = 1  #set b to 1
	while A>0:  #as long as A > O
		if A % 2 == 1:	#if A is odd
			b = (b*a) % N	
		a = pow(a, 2, N) #a gets squared mod N
		A = A//2 #A gets cut in half and rounded down
	return b #once A = 0, return b, this is g^A mod N
		
def shanks(N, g, h):
	'''shanks(small step, big step) algorithm 
	for finding a hash collision to solve DLP'''
	small_steps = list()
	big_steps = list()
	n = 1 + int(pow(N,0.5))
	
	for i in range(0, n):
		small_steps.append(fast(N,g,i))
		big_steps.append((h*fast(N, fast(N, g, (N-2)*n), i)) % N)
	small_sorted = sorted(small_steps)
	big_sorted = sorted(big_steps)
	
	for small_step in small_sorted:
		collision = binsearch(big_sorted, small_step)
		if collision:
			return (small_steps.index(small_step) 
			+ (big_steps.index(big_sorted[collision])*n))
	