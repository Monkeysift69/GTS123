import numpy as np

f = r'C:\Users\mince\Desktop\py\Uni\lab10\grades.tsv'
data = np.loadtxt(f, dtype=str)
print(data)