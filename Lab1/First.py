import random

def create_matrix(n):
    matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:
                row.append(random.randint(0, 50) * 2)
            else:
                row.append(random.randint(0, 50) * 2 + 1)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(row)

n = int(input("Enter the value of n (size of the matrix): "))
result_matrix = create_matrix(n)
print("The generated matrix is:")
print_matrix(result_matrix)