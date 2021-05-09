import numpy as np # import numpy library as np
import matplotlib.pyplot as plt # import pyplot library as plt

plt.style.use('ggplot') # use "ggplot" style for graphs

NSTEP = 10000 # number of random steps
plt.xlabel("number of steps") # name of x axis
plt.ylabel("position") # name of y axis
for nseed in range(10): # generate 10 random walks
    # initialize random step generator with different nseeds
    np.random.seed(nseed)
    # generate random sequencies of NSTEP +1/-1 steps
    step = np.random.choice([-1,1],NSTEP)
    # calculate position of random walk at each step
    position = np.cumsum(step)
    plt.plot(position) # plot position(step) vs. step