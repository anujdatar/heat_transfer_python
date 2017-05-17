# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:37:45 2017

@author: Anuj
"""

import numpy as np

def gauss_seidel(phi):
    
    nx = phi.shape[1]
    ny = phi.shape[0]
    
    
    iter_count = 0
    iter_update = 0
    conv_err = 0
    
    