#to find sum,difference,product& quotient of each element of two matrices
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[3,4],[1,2]])
print("sum is:" ,np.add(a,b))
print("difference is :", np.subtract(a,b))
print("product is :",np.multiply(a,b))
print("quotient is: ",np.divide(a,b))