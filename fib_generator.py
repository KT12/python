# Using yield to create a Fibonacci generator

def fib(maximum):
  a,b = 0,1
  while a <= maximum:
    yield a
    a,b = b, a+b

# Generator can be used with for loops
# for _ in fib(100):
#     print(n)

# Generator can also be used with list
# list(fib(100))
