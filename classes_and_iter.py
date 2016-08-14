class MontyHallProblem(object):
    def __init__(self):
        self.words = ['Monty', 'Hall', 'Problem]
        self.idx = 0
    
    def __iter__(self):
        self.idx = 0
        return self
        # return MontyHallProblem()
    
    def __next__(self):
        if self.idx == len(self.words):
            raise StopIteration()
        word = self.words[self.idx]
        self.idx += 1
        return word
        
""" By altering __iter__ method,
can change behavior of the class when more than one instance is called

        self.idx = 0
        return self
        
        OR
        
        return self
        
        OR
        
        return MontyHallProblem()
        
"""

m = MontyHallProblem()

it1 = iter(m)
print(next(it1))
print(next(it1))
print('++++++++++++')
it2 = iter(m)
print(next(it2))


