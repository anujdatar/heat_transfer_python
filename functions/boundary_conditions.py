# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:59:17 2017

@author: Anuj
"""

#import numpy as np

STEF_BOLTZ = 5.670367e-8

def boundary_conditions_source(source, coeff, phi_inf):
    """ modify source vector based on the boundary conditions
    for the edges and corner nodes

    Args:
        source: source vector
        coeff: coefficient value
        phi_inf: ambient temperature

    Returns:
        source vector
    """

    nx = source.shape[1]
    ny = source.shape[0]

# Western Face #### for x = x_min, and y = 1:ny-1
    for j in range(1,ny-1):
        source[j, 0] = source[j, 0] - coeff*phi_inf

# for x = x_max, and y = 1:ny-1 ### Eastern most face
    for j in range(1,ny-1):
        source[j, nx-1] = source[j, nx-1] - coeff*phi_inf

# for y = y_min, and x = 1:nx-1 ### Southern most face
    for i in range(1,nx-1):
        source[0, i] = source[0, i] - coeff*phi_inf

# for y = y_max, and x = 1:nx-1 ### Northern most face
    for i in range(1,nx-1):
        source[ny-1, i] = source[ny-1, i] - coeff*phi_inf

# x = x_min and y = y_min ### South-western corner
    source[0, 0] = source[0, 0] - coeff*phi_inf - coeff*phi_inf

# x = x_max and y = y_min ### South-eastern corner
    source[0, nx-1] = source[0, nx-1] - coeff*phi_inf - coeff*phi_inf

# x = x_min and y = y_max ### North-western corner
    source[ny-1, 0] = source[ny-1, 0] - coeff*phi_inf - coeff*phi_inf

# x = x_max and y = y_max ### North-eastern corner
    source[ny-1, nx-1] = source[ny-1, nx-1] - coeff*phi_inf - coeff*phi_inf

    return source
