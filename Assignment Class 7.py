# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 12:01:28 2019

@author: acer
"""

#   Assignment Class 7
#    Problem Statement
#    Write a function to find moving average in an array over a window:
#    Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
#############################################################################
# Method 1
#############################################################################
from collections import deque
import itertools

def moving_average(iterable, n=3):
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable) 
    # create an iterable object from input argument
    d = deque(itertools.islice(it, n-1))  
    # create deque object by slicing iterable
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n

# example on how to use it
for i in  moving_average([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]):
    print(i)

#############################################################################
# Method 2
#############################################################################
import numpy as np
dataset = np.asarray([3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150])
ma = list()
window = 3
for t in range(0, len(dataset)):
    if t+window <= len(dataset):
        indices = range(t, t+window)
        ma.append(np.average(np.take(dataset, indices)))
else:
    ma = np.asarray(ma)