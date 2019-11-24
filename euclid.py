def euclid(a, b):
  d = deque(maxlen = 2)
  d.append(b)
  q = (a//b)
  r = a - (b(a//b))
  d.append(r)
  while r != 0:
    r = d[0]*q + d[1]
    d.append(r)
  return(d[1])  
