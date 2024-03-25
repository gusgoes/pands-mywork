# Author: Gustavo Fernandes
import numpy as np  # import numpy library
import matplotlib.pyplot as plt  # import matplotlib library


xpoints = np.array(range(1, 101))  # create a numpy array with 2 points
ypoints = xpoints * xpoints  # create a numpy array with 2 points

plt.plot(xpoints, ypoints, label = "xquare")  # plot the numpy arrays
plt.plot(xpoints, xpoints, label = "linear")  # plot the numpy arrays
plt.legend()  # show the legend
#plt.show()  # show the plot

randompoints = np.random.normal(1, 1000, 100)  # create a numpy array with 10 random numbers with a normal distribution
plt.scatter(xpoints, randompoints, label = "random")  # plot the numpy arrays
plt.savefig('pands-mywork\week08\plot.png') # save the plot to a file