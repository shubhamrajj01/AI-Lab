# Lab2.6: WAP to find the frequencies of the unique value in NumPy array.

import numpy as np

array = np.array([1, 2, 3, 1, 2, 4, 1, 3, 4, 4])

# Find unique values and their frequencies
unique_values, frequencies = np.unique(array, return_counts=True)
print("Unique values and their frequencies:")
for value, frequency in zip(unique_values, frequencies):
    print(f"Value: {value}, Frequency: {frequency}")
