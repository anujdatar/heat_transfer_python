# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:37:45 2017

@author: Anuj
"""

import numpy as np

def gauss_seidel(phi, phi_bdry, source, epsit, max_iters,
                 omega, coeff, coeff_p, resid):

    nx = phi.shape[1]
    ny = phi.shape[0]


    iter_count = 0
    iter_update = 10 * epsit
    conv_err = epsit

    while iter_count < max_iters and iter_update > conv_err:
        iter_count += 1

        phi_max = 0
        dphi_max = 0
        #resid_max = 0
        phi_old = np.copy(phi)

        for i in range(1, nx-1):
            for j in range(1, ny-1):
                phi[j, i] = ((omega * (source[j, i] + coeff*phi[j, i-1]
                                      + coeff*phi[j-1, i] + coeff*phi[j+1, i]
                                      + coeff*phi[j, i+1])/coeff_p)
                             + (1-omega)*phi[j, i])

                phi_max = max(phi_max, abs(phi[j,i]))
                dphi = abs(phi[j, i] - phi_old[j, i])
                dphi_max = max(dphi_max, dphi)

        phi[phi < phi_bdry] = phi_bdry

#        for i in range(1, nx-1):
#            for j in range(1, ny-1):
#                resid[j, i] = (source[j, i] + coeff*phi[j, i-1]
#                               + coeff*phi[j-1, i] + coeff*phi[j+1, i]
#                               + coeff*phi[j, i+1] - coeff_p*phi[j, i])

        resid[1:ny-1, 1:nx-1] = (source[1:ny-1, 1:nx-1]
                                 + coeff*phi[1:ny-1, 0:nx-2]
                                 + coeff*phi[0:ny-2, 1:nx-1]
                                 + coeff*phi[2:ny, 1:nx-1]
                                 + coeff*phi[1:ny-1, 2:nx]
                                 - coeff_p*phi[1:ny-1, 1:nx-1])

        iter_update = dphi_max
        conv_err = epsit * phi_max

    return phi, phi_old, iter_count, iter_update, resid, dphi_max, conv_err