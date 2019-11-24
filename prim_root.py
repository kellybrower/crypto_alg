def prim_root(p): #only works with primes
	li = list()
	for i in range(2, p):
		if 	(p-1) % i == 0:
			li.append(i)
	li_sort = sorted(li)
	for i in li_sort:	
		if pow(i, p-1, p) == 1:
			return i
		else:
			return -1
	
