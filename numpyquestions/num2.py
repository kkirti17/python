#transpose of a matrix 
import numpy as np
x= np.array([[2,3],[4,5],[6,7]])
result = [[0,0,0],[0,0,0]]
for i in range  (len(x)):
    for j in range(len(x[0])):
        result[j][i]=x[i][j]
for r in result:
    print(r)