#create an array and then convert all the even numbers w/ 0
import numpy as np
a=np.arange(1,11)
a[a%2==0]=0
print(a)