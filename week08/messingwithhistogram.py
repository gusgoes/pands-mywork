#messing with histograms
#Author: Gustavo Fernandes

import numpy as np  # import numpy library
import matplotlib.pyplot as plt  # import matplotlib library

'''np.random.seed(1)  # set the seed to 1
normalpoints = np.random.normal(size=100)  # create a numpy array with 10 random numbers with a normal distribution
plt.hist(normalpoints, bins=30)  # plot the numpy arrays
plt.savefig('pands-mywork\week08\histogram.png') # save the plot to a file'''

fruit = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "pear", "plum", "grape"]
numbers =  np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

plt.pie(numbers, labels=fruit)  # plot the numpy arrays
plt.savefig('pands-mywork\week08\piechart.png') # save the plot to a file