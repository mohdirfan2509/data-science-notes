# array_name[index] 1d array
# array_name[row, column] 2d array

import numpy as np

arr1=np.array([1,8,5,9,12,20])
print(arr1[0]) #  1  first element
print(arr1[3]) #  9  4th element
print(arr1[-1]) # 20 last element

# print(arr1[10])  raises IndexError: index 10 is out of bounds for axis 0 with size 6