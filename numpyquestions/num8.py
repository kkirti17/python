#numpy program to split the element of a given array with multiple lines.
import numpy as np
x=np.array(['apple','banana','mango','grapes'],dtype=np.str)
print("original array:")
print(x)
r=np.char.split(x)
print("\nsplit the element of array w/ spaces: ")
print(r)