# -*- coding: utf-8 -*-
"""
Created on Thu May 18 01:44:08 2017

@author: anujd
"""

import numpy as np

a = np.zeros((3,4))
b = np.zeros((a.shape[0], a.shape[1]))
c = np.zeros(a.shape)

print(a, '\n')
print(b, '\n')
print(c, '\n')

#%%
def myfunction(a, b=1, c=2):

    a2 = a*a
    b2 = b*b
    c2 = c*c

    print(a2, b2, c2)

p = 5
q = 6
r = 7

myfunction(p)
myfunction(p, q, r)
myfunction(p, c=q, b=r)