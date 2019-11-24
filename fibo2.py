def fib(n):
  a, b = 0, 1
  while b < n:
    a, b = b, a + b

  return a, b
  x = fib(7)
  print x
