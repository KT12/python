# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 00:39:50 2016

@author: Ken
"""
a_list = [1,'4',9,'a',False,0,4]

sqints = [e**2 for e in a_list if type(e) == int]

'''
Input sequence is a_list
Variable representing memebers of input sequence is e
Optional Predicate expression is if type(e) == int
Output expression is e**2
'''

'''
Related built-ins map, filter, and lambda 
can also be used in comprehensions
'''

# Filter applies predicate to sequence
filter(lambda e: type(e)==int, a_list)

# Map modifies each member of a sequence

map(lambda e: e**2, a_list)

# Combine map and filter, use list() to assign to list
list(map(lambda e: e**2, filter(lambda e: type(e)==int, a_list)))

'''
Nested comprehensions
Can use a nested comprehension to create Identity matrix n*n
'''
n = 3

I = [[1 if item_idx == row_idx else 0 for item_idx in range(n)] for row_idx in range(n)]

# Upper triangle matrix

U = [[1 if item_idx >= row_idx else 0 for item_idx in range(n)] for row_idx in range(n)]

# Lower triangle matrix

L = [[1 if item_idx <= row_idx else 0 for item_idx in range(n)] for row_idx in range(n)]

# Hollow matrix

H = [[1 if item_idx != row_idx else 0 for item_idx in range(n)] for row_idx in range(n)]


''' Set Comprehensions '''

names = ['Omar', 'JOHN', 'alice', 'Taku', 'Jimi', 'bob', 'ALICE', 'J', 'Bob', 'T']

# Return set of all names with only the first letter capitalized for all names longer than 1 letter

tags = {name[0].upper() + name[1:].lower() for name in names if len(name) > 1}


''' Dict Comprehensions '''

# Return dict which combines character counts that are not case sensitive

case_freq = {'a':10, 'b': 34, 'z': 51, 'A': 7, 'C': 42, 'Z':3}

total_freq = {k.lower(): case_freq.get(k.lower(),0)+case_freq.get(k.upper(),0) for k in case_freq.keys()}