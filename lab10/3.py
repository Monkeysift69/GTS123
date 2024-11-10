import numpy as np

file_path =r'C:\Users\mince\Desktop\py\Uni\lab10\grades.tsv'
data = np.loadtxt(file_path, dtype=str)

credits = [3,2,1,3,3,3]

ids = data[:,0]
grades = data[:,1:].astype(float)

def gpa(row, credits):
    summ = [grade * cred for grade, cred in zip(row,credits)]
    summ = sum(summ)

    """
    summm = []
    for grade, cred in zip(row,credits):
        mult = grade * cred
        summm.append(mult)
    sum(summm)
"""
    gpa = summ/sum(credits)
    return gpa

gpas =[gpa(row,credits) for row in grades]

for id, gpa in zip(ids, gpas):
    print("%s\t%.2f" %(id, gpa))
print(ids, gpas)