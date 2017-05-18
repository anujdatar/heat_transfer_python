# -*- coding: utf-8 -*-
"""
Created on Tue May 16 01:42:46 2017

@author: anujd
"""

import numpy as np

STEF_BOLTZ = 5.67e-8

def heat_out(hc_air, phi, phi_old, phi_inf, emmi, heat_loss_type):
    '''calculate heat out based on convection and radiation
    '''

    if heat_loss_type == 'Cond':
        source_out = np.zeros(phi.shape)

    elif heat_loss_type == 'Conv':
        source_out = hc_air * np.subtract(phi, phi_old)

    else:
        phi_eff = (phi**3 + np.multiply(phi_inf, phi**2) +
                   np.multiply(phi_inf**2, phi) + phi_inf**3)

        hc_eff = np.add(emmi * STEF_BOLTZ * phi_eff, hc_air)

        source_out = np.multiply(hc_eff, np.subtract(phi, phi_inf))

    return source_out
