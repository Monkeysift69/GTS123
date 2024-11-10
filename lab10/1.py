import numpy as np

x = int(input("Input size of matrix: "))
matrix = []

#insert lists(row) to a list
for i in range(x):
    row = []
    for j in range(x):
        e = int(input("Input element at row %d column %d" %(i+1, j+1)))
        row.append(e)
    matrix.append(row)

matrix = np.array(matrix) 

det = np.linalg.det(matrix) #np.linalg = linear algebra.det

inverse = np.linalg.inv(matrix)
print(matrix)
print(det)
print(inverse)