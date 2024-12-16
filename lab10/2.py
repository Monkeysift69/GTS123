import numpy as np

matrix1 = []
matrix2 = []

c = 0
#insert lists(row) to a list
for i in range(3): # 0
    row1 = []
    row2 = []
    for j in range(4): # 0 1 2 3
        c += 1
        e = int(input("Input element at row %d column %d" %(i+1, j+1)))
        if c in [4,8,12]:
            row2.append(e)
        
        else:
            row1.append(e)

    matrix1.append(row1)
    matrix2.append(row2)

matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

imatrix1 = np.linalg.inv(matrix1)
    
mul =np.matmul(imatrix1, matrix2)

print(mul)

print("Solution: ")
print("x = %.2f" %mul[0,0]) #row 0 c 0
print("y = %.2f" %mul[1,0])
print("z = %.2f" %mul[2,0])