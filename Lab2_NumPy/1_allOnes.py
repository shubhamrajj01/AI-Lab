# Lab2.1: Create a NumPy array filled with all one's

import numpy as np

print("Enter the rows of NumPy array: ")
rows = int(input())
print("Enter the columns of NumPy array: ")
columns = int(input())
ones_array = np.ones((rows, columns))  # Create an array filled with ones
print("Array filled with ones:")
print(ones_array)
