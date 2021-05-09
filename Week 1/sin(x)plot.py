# IMPORT LIBRARIES
# % matplotlib inline # decirle que meta los graficos en el jupnot itself
import numpy as np # import numpy library as np
import matplotlib.pyplot as plt # import pyplot library as plt
plt.style.use('ggplot') # use "ggplot" style for graphs

x = np.linspace(-3, 3) # create array of x from -3 to 3
y = np.sin(x) # create array of sin(x)
plt.plot(x, y) # plot y vs. x
plt.show() # display plot

