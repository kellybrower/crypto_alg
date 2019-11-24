def factor(N, d, e):
	k = 1
	while k*N < d*e:
		k+=1
	p_plus_q = (k*N - d*e + k + 1) // k
	
	p_minus_q = pow((pow(p_plus_q,2) - 4*N), 0.5)
	
	p = (p_plus_q + p_minus_q)//2
	q = p_plus_q - p
	
	return (int(p),int(q))