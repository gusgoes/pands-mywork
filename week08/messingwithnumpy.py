# Author: Gustavo Fernandes
import numpy as np  # import numpy library

list1 = [1, 2, 3, 4, 5,"asdf"]  # create a list
list1 = list1 + [10]  # add 10 to the list
print(list1)    # print the list

numbers = np.array([1, 2, 3, 4, 5]) # create a numpy array
numbers = numbers + 10 + [10] # add 10 to each element of the numpy array
print(numbers)  # print the numpy array

random = np.random.randint(1, 100, 10)  # create a numpy array with 10 random numbers between 1 and 100
print(random)  # print the numpy array

normalrandom = np.random.normal(loc=50, scale=20, size=100)  # create a numpy array with 10 random numbers with a normal distribution
print(normalrandom)  # print the numpy array