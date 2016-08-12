class Fib:
  ''' Iterator which will return fib values'''
   # Usually capitalized to differentiate from Python built-ins
  def __init__(self, maximum):
    self.maximum = maximum
    # self is not a reserved word in Python
    # But, it's a bad idea to use anything else here.
    # Self refers to the instance of the class called
    
  def __iter__(self):
    self.a = 0
    self.b = 1
    return self
    # Necessary anytime someonecalls iter(Fib)
    
  def __next__(self):
    fib = self.a
    if fib > self.max:
      raise StopIteration # Stopping conditions.
    self.a, self.b = self.b, self.a + self.b
    return fib # Need to use return, not yield.  Yield is for generators
    # Necessary anytime someone calls next(Fib)
