# slicing
# array[start:stop:step] stop is excluded

import numpy as np

arr1=np.array([10,20,30,40,50,60])

print(arr1[2:5])
print(arr1[:4])
print(arr1[2:])
print(arr1[::-1]) #reverses the array
print(arr1[::2])
print(arr1[5:])