# -*- coding: utf-8 -*-

import numpy as np

from .tridiagonal_solver import tdma_solver

def adi_tdma(phi, source, coeff, max_iter, epsit):
    '''Alternating Direction Implicit using a TDMA solver'''
    
    n = phi.shape[1]
    m = phi.shape[0]
    nm = n*m
    
    coeff_m = np.zeros(nm) + coeff
    
    iter_count = 0
    iter_update = 10*epsit
    conv_err = epsit
    
    while iter_count < max_iter and iter_update > conv_err:
        iter_count += 1
        
        phi_max = 0
        dphi_max = 0
        
# row sweep ########################################################
        phi_row = phi.flatten()
        source_row = source.flatten()
        
        A_source = np.multiply(coeff_m, phi_row)
        
        