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

#%%

import numpy as np
from solvers import tdma_solver

A = np.array([[1, 3, 0, 0], [2, 4, 1, 0], [0, 1, 3, 2], [0, 0, 2, 4]])
B = np.array([14, 22, 20, 24])

#print(A)
#print(B)

u = np.array([3, 1, 2, 0], dtype=float)
d = np.array([1, 4, 3, 4], dtype=float)
l = np.array([0, 2, 1, 2], dtype=float)
b = np.array([14, 22, 20, 24], dtype=float)

n = 4

for i in range(n-1):
    # normalize
    u[i] = u[i]/d[i]
    b[i] = b[i]/d[i]
    d[i] = 1

    # forward elimination
    alpha = l[i+1] #/ d[i+1]
    l[i+1] = 0 #l[i+1] - alpha
    d[i+1] = d[i+1] - alpha*u[i]
    b[i+1] = b[i+1] - alpha*b[i]
    
    print(i, alpha, l, d, u, b)
x1 = np.zeros(n)

x1[n-1] = b[n-1] / d[n-1]

for i in range(n-2, -1, -1):
    x1[i] = b[i] - u[i]*x1[i+1]
print(x1)

x2 = np.linalg.solve(A, B)
print(x2)

x3 = tdma_solver(l, d, u, b)
print(x3)

#%%


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

#%%

import numpy as np
from solvers import tdma_solver

A = np.array([[1, 3, 0, 0], [2, 4, 1, 0], [0, 1, 3, 2], [0, 0, 2, 4]])
B = np.array([14, 22, 20, 24])

#print(A)
#print(B)

u = np.array([3, 1, 2, 0], dtype=float)
d = np.array([1, 4, 3, 4], dtype=float)
l = np.array([0, 2, 1, 2], dtype=float)
b = np.array([14, 22, 20, 24], dtype=float)

n = 4

for i in range(n-1):
    # normalize
    u[i] = u[i]/d[i]
    b[i] = b[i]/d[i]
    d[i] = 1

    # forward elimination
    alpha = l[i+1] #/ d[i+1]
    l[i+1] = 0 #l[i+1] - alpha
    d[i+1] = d[i+1] - alpha*u[i]
    b[i+1] = b[i+1] - alpha*b[i]
    
    print(i, alpha, l, d, u, b)
x1 = np.zeros(n)

x1[n-1] = b[n-1] / d[n-1]

for i in range(n-2, -1, -1):
    x1[i] = b[i] - u[i]*x1[i+1]
print(x1)

x2 = np.linalg.solve(A, B)
print(x2)

x3 = tdma_solver(l, d, u, b)
print(x3)

#%%
from functions import compile_coeff
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7 ,8, 9])

ll, l, d, u, uu = compile_coeff(a, a, a, a, a, 'row', 3, 3)
