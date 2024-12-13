# Lab2.5: WAP to calculate the sum of the diagonal elements of a NumPy array.

import numpy as np
n = int(input("Enter the size of the matrix (n x n): "))
element = []
print(f"Enter the elements of a {n}x{n} matrix row by row:")
for i in range(n):
    row = np.array(input(f"Enter {n} elements of Row{i+1}: ").split(), dtype=int)
    element.append(row)
matrix = np.array(element)

sum = np.trace(matrix) #numpy function 
print("sum of diagonal elements of the matrix is : ",sum)