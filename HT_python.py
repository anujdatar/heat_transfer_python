
import time
import numpy as np

from functions import import_material
from functions import import_process
from functions import import_solver_settings

from functions import heat_out

STEF_BOLTZ = 5.67e-8

n = 100
m = 100

material = 'Ti6Al4V'
rho, Cp, k, phi_melt, emmi = import_material(material)

L_pow, L_spot, L_vel, phi_inf, hc_air = import_process()

solver = 'Gauss-Seidel'


alpha = k/(rho*Cp)

dx = L_spot

dt = dx/L_vel
time_steps = 1

coeff = alpha/(dx*dx)

L_flux =  L_pow / (L_spot * L_spot)

nx = n + 1
ny = m + 1

phi = np.zeros((ny, nx)) + phi_inf
source_in = np.zeros((ny, nx))
resid = np.zeros((ny, nx))

phi_eff = np.zeros((ny, nx))
hc_eff = np.zeros((ny, nx))

phi_old = np.copy(phi)

source_in[4:7, 4:7] = L_flux
phi[4:7, 4:7] = phi_melt

#heat_loss_type = 1
#source_out = heat_out(hc_air, phi, phi_old, phi_inf, emmi, STEF_BOLTZ)#,heat_loss_type)

start_timer = time.time()

time_step = 0
while time_step < time_steps:
    time_step += 1

    source_out = heat_out(hc_air, phi, phi_old, phi_inf, emmi, STEF_BOLTZ)
    source_net = np.subtract(source_in, source_out)
    source_net = np.multiply(alpha/k, source_net)
    
    

