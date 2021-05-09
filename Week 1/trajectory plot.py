
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

dim = 2 # system dimension (x,y)
nums = 1000 # number of steps
R = np.zeros(dim) # particle position
V = np.zeros(dim) # particle velocity
Rs = np.zeros([dim,nums]) # particle position (at all steps)
Vs = np.zeros([dim,nums]) # particle velocity (at all steps)
Et = np.zeros(nums) # total enegy of the system (at all steps)
time = np.zeros(nums) # time (at all steps)

m, k, zeta = 1.0, 1.0, 0.25
# Initial condition
R[0], R[1] = 1., 1. # Rx(0), Ry(0)
V[0], V[1] = 1., 0. # Vx(0), Vy(0)
dt = 0.1*np.sqrt(k/m) # set \Delta t
box = 5 # set size of draw area

fig, ax = plt.subplots(figsize=(7.5,7.5))
ax.plot(Rs[0,0:nums],Rs[1,0:nums]) # parameteric plot Rx(t) vs. Ry(t)
plt.show()