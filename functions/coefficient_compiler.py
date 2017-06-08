# -*- coding: utf-8 -*-
"""
Created on Thu May 18 17:00:57 2017

@author: Anuj
"""

import numpy as np

def compile_diags(A_ll, A_l, A_d, A_u, A_uu, sweep, x, y):
    """ compile diagonal elements of the coefficient matrix in proper order """

    if sweep == 'row':
        n = x
        m = y
    elif sweep == 'col':
        n = y
        m = x
    nm = n*m

    ll = np.zeros(nm)
    l = np.zeros(nm)
    d = np.copy(A_d)
    u = np.zeros(nm)
    uu = np.zeros(nm)

    # sub-sub diagonal
    for i in range(n, nm):
        ll[i] = A_ll[i-n]

    # sub-diagonal
    for i in range(1, nm):
        l[i] = A_l[i-1]
        if i%n == 0:
            l[i] = 0

    # super diagonal
    for i in range(nm-1):
        u[i] = A_u[i+1]
        if i%n == 0:
            u[i-1] = 0

    # super-super diagonal
    for i in range(nm-n):
        uu[i] = A_uu[i+n]

    return ll, l, d, u, uu


def compile_amat(ssub, sub, dia, sup, ssup, sweep, x, y):
    """construct the coefficient matrix for a system of equations
    from its diagonal, sub-sub and sub diagonal and, super-super and super
    diagonal vectors

    Args:
        ssub: sub-sub-diagonal vector
        sub: sub-diagonal vector
        dia: diagonal vector
        sup: super-diagonal vector
        ssup: super-super-diagonal vector

    Returns:
        the constructed matrix A
    """
    if sweep == 'row':
        n = x
        m = y
    elif sweep == 'col':
        n = y
        m = x
    nm = n * m
    A = np.zeros((nm,nm))

    for i in range(nm):
        if i == 0:
            A[i, i] = dia[i]
            A[i, i+1] = sup[i]
        elif i == nm-1:
            A[i, i-1] = sub[i]
            A[i, i] = dia[i]
        else:
            A[i, i-1] = sub[i]
            A[i, i] = dia[i]
            A[i, i+1] = sup[i]
    for i in range(n,nm):
        A[i, i-n] = ssub[i]

    for i in range(nm-n):
        A[i, i+n] = ssup[i]

    return A
