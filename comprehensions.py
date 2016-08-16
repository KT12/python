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

