import numpy as np # import numpy library as np
import matplotlib.pyplot as plt # import pyplot library as plt

plt.style.use('ggplot') # use "ggplot" style for graphs

def func (x, n):
    y = x**n
    return y

x = np.logspace(-2,2) # create array of x from
# 10^-2 to 10^2 equally spaced in log scale
plt.plot(x,func(x,1),label='$y=x$') # plot y=x
plt.plot(x,func(x,2),label='$y=x^2$') # plot y=x^2
plt.plot(x,func(x,3),label='$y=x^3$') # plot y=x^3
plt.legend() # display plot legends
plt.xscale("log") # set log scale for x axis
plt.yscale("log") # set log scale for y axis
plt.xlabel("$x$") # display name of x axis
plt.ylabel("$y$") # display name of y axis
plt.show() # display plots