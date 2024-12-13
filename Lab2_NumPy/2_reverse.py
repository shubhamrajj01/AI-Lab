# Lab2.2: WAP to reverse a NumPy array 

import numpy as np

size = int(input("Enter the size of the NumPy array: "))

elements = []

print(f"Enter {size} elements for the NumPy array:")
for i in range (size): 
    elements.append(int(input()))
    
original_array = np.array(elements)
print("Original Array: ", original_array)

reversed_array = original_array[::-1]
print("Reversed Array: ", reversed_array)