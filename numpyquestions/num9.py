#numpy program to count the number of p in a given array 
import numpy as np
a=np.array(['python','php','physics','project'],dtype=np.str)
print("\noriginal aaray: ")
print(a)
r=np.char.count(a,"p")
print("number of p: ",r)