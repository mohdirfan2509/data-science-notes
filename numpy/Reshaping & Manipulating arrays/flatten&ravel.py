# array_name.ravel() --> returns the view of original array in flattened form, if we modify the data of returned array the changes also reflect in the original array
#  array_name.flatten() --> returns the copy (fresh) flattened array, modifications in flattened array won't effect original array

import numpy as np

arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
ravel_array=arr1.ravel()
flatten_array=arr1.flatten()

ravel_array[0]=200


print(arr1)
print(ravel_array)
print(flatten_array)