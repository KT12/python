# Use a generator instead of a list comprehension if you are only iterating once
# Generators can't be sliced or indexed, can't be added to lists
# Generators consume less memory

lst = [n**2 for n in range(1000)]
gen = (n**2 for n in range(1000))

import sys

print(sys.getsizeof(lst))   # 9024
print(sys.getsizeof(gen))   # 88
