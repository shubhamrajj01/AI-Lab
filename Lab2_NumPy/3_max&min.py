# Lab2.3: Find the max and min value in a matrix using NumPy.
import numpy as np

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

print("Enter the elements row by row (space-separated):")
elements = []
for i in range(rows):
    row = np.array(input(f"Enter {columns} elements of Row{i+1}: ").split(), dtype=int)
    elements.append(row)

matrix = np.array(elements)

# Find the maximum and minimum values in the matrix
max_value = np.max(matrix)
min_value = np.min(matrix)

print(f"The maximum element in the matrix is {max_value} and the minimum element is {min_value}.")