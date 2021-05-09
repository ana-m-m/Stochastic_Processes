"""Numerically solve the following differential equation and determine for with
the initial condition at .
Then compare it with the analytical solution.
y(t) 0 ≤ t ≤ 10
y = 1 t = 0
y = exp(−t)"""
# dy(t)/dt = -y(t)

# % matplotlib inline

import numpy as np # import numpy library as np
import matplotlib.pyplot as plt # import pyplot library as plt

plt.style.use('ggplot') # use "ggplot" style for graphs

# Euler method

dt, tmin, tmax = 0.1, 0.0, 10.0 # set \Delta t,t0,tmax
step=int((tmax-tmin)/dt)

# create array t from tmin to tmax with equal interval dt
t = np.linspace(tmin,tmax,step)
y = np.zeros(step) # initialize array y as all 0
ya = np.exp(-t) # analytical solution y=exp(-t)
plt.plot(t,ya,label='Exact',lw=5) # plot y vs. t (analytical)
y[0]=1.0 # initial condition

for i in range(step-1):
    y[i+1]=y[i]-dt*y[i] # Euler method Eq.(A8)

plt.plot(t,y,ls='--',lw=3,label='Numerical') # plot y vs t (numerical)
plt.plot(t,y/ya,lw=3,label='Ratio') # plot y/ya vs. t
plt.legend() #display legends
plt.show() #display plots