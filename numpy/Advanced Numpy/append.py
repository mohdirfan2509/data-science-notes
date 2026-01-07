# np.append(array_name,value)--> adds the element at the last index

import numpy as np

arr_1=np.array([10,20,30])
modified_array=np.append(arr_1,40)
print(modified_array)


# in case 2d array or multidimensional array

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)
modified_arr_2d=np.append(arr_2d,[200,300,400]) 
print(modified_arr_2d)