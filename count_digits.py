#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 22:49:13 2017

@author: ktt
"""

# Count zero's in every number from 1 to n

def count_number(digit=0, end=1000000):
    n = str(digit)
    return sum(str(k).count(n) for k in range(1, int(end+1)))
