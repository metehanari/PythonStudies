#numpy plotting

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
# create a numpy array with 100 elements from 0 to 2*pi.

y = np.sin(x)
# sine of x

plt.plot(x,y)
# plot x and y

plt.show()
# show the plot