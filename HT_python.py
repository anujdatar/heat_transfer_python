''' Heat transfer using python '''
import time
import numpy as np
import matplotlib. pyplot as plt

from settings import import_material
from settings import import_process
from settings import import_solver_settings

from solvers import gauss_seidel

from functions import heat_out

STEF_BOLTZ = 5.67e-8

problem_type = 'Transient'  # 'SteadyState' or 'Transient'
material = 'Ti6Al4V'
solver = 'GaussSeidel'  # 'Gauss-Seidel' or 'ADI'
heat_loss_type = 'ConvRad' # 'Cond' or 'Conv' or 'ConvRad'

print('%s analysis, %s solver, %s heat loss, material => %s'
      %(problem_type, solver, heat_loss_type, material))

if solver == 'GaussSeidel':
    bdry_offset = 1
elif solver == 'ADI':
    bdry_offset = 0

# import material properties, process and algorithm parameters
rho, Cp, k, phi_melt, emmi = import_material(material)
L_pow, L_spot, L_vel, phi_inf, hc_air = import_process()
epsit, max_iter, omega = import_solver_settings(solver)

alpha = k/(rho*Cp)

dx = L_spot

# calculate time step size
total_time = dx/L_vel
dt = total_time

# coefficient
coeff = alpha/(dx*dx)
if problem_type == 'SteadyState':
    coeff_p = 4 * coeff
elif problem_type == 'Transient':
    coeff_p = (4*coeff) + (1/dt)

# heat flux input
L_flux = L_pow / (L_spot * L_spot)

# Grid size
n = 30
m = 30
lx = n*dx
nx = n + 1 + 2*bdry_offset
ny = m + 1 + 2*bdry_offset

# setting up initial and empty matrices
phi = np.zeros((ny, nx)) + phi_inf
source_in = np.zeros((ny, nx))
resid = np.zeros((ny, nx))

phi_eff = np.zeros((ny, nx))
hc_eff = np.zeros((ny, nx))

phi_old = np.copy(phi)

source_in[4:7, 4:7] = L_flux
#phi[4:7, 4:7] = phi_melt

print('n = %d, dx = %e, dt = %f, input heat flux = %e' %(n, dx, dt, L_flux))

# start iterative algorithm
start_timer = time.time()

curr_time = 0

while curr_time < total_time:
    curr_time += dt

    source_out = heat_out(hc_air, phi, phi_old, phi_inf, emmi, heat_loss_type)
    source_net = np.subtract(source_in, source_out)
    source_net = np.multiply(alpha/k, source_net)

    if problem_type == 'SteadyState':
        source = np.copy(source_net)
    elif problem_type == 'Transient':
        source = np.add(source_net, np.multiply(phi, 1/dt))

    phi, phi_old, iter_count, iter_update, resid, dphi_max, conv_err = \
    gauss_seidel(phi, phi_inf, source, epsit, max_iter,
                 omega, coeff, coeff_p, resid)

resid_max = np.max(resid)
end_timer = time.time() - start_timer
print('Analysis time = %.2f seconds' % end_timer)

print('max phi %.2f, iters %d, iter_update %e, resid_max %e'
      %(np.max(phi), iter_count, iter_update, resid_max))

plt.contourf(phi)
plt.jet()
plt.colorbar()

print('\nlx = %.2e, dx = %.2e, dt = %.2e, input flux = %.2e' %(lx, dx, dt, L_flux))
