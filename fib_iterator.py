class Fib:
  ''' Iterator which will return fib values'''
   # Usually capitalized to differentiate from Python built-ins
  def __init__(self, maximum):
    self.maximum = maximum
    # self is not a reserved word in Python
    # But, it's a bad idea to use anything else here.
    
  def __iter__(self):
    self.a = 0
    self.b = 1
    return self
    
  def __next__(self):
    fib = self.a
    if fib > self.max:
      raise StopIteration
    self.a, self.b = self.b, self.a + self.b
    return fib
