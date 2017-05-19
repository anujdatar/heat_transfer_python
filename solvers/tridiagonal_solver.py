# -*- coding: utf-8 -*-

import numpy as np


def tdma_solver(sub, diag, sup, source):
    ''' Tri-diagonal matrix algorithm '''
    
    n = diag.shape[0]
    
    # Thomas algorithm
    for i in range(n-1):
    # normalize with diagonal entities
        sup[i] = sup[i]/diag[i]
        source[i] = source[i]/diag[i]
        diag[i] = 1
            
    # forward elimination
        alpha = sub[i+1]
        sub[i+1] = 0
        diag[i+1] = diag[i+1] - alpha*sup[i]
        source[i+1] = source[i+1] - alpha*source[i]
    
    solution = np.zeros(n)
    
    solution[n-1] = source[n-1]/diag[n-1]
    
    for i in range(n-2, -1, -1):
        solution[i] = source[i] - sup[i]*solution[i+1]
        
    return solution