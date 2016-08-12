# Using yield to create a Fibonacci generator

def fib(maximum):
  a,b = 0,1
  while a <= maximum:
    yield a
    a,b = b, a+b
