# number of elements before and after reshaping will remain same   
# # syntax:  array_name.reshape(rows,columns) -> specify new shape. works only if dimensions match   
# array_name.reshape() does return a new array. It returns a view 
# changing values in the reshaped (new) array will affect the old array (parent array)

import numpy as np

arr1=np.array([10,20,30,40,50,60])

arr2=arr1.reshape(2,3)
arr2[0][0]=123
arr2[0][2]=2000

print(arr1)
print(arr2)  

