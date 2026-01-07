# np.concatenate( (array_1,array_2),axis=)--> concatenates two arrays along the axis specified
# it retuns a new array
# axis=0 --> vertical stacking (concatenates row wise)
# axis=1 --> Horizontal stacking (concatenates column wise)

import numpy as np

arr_1=np.array([1,2,3])
arr_2=np.array([4,5,6])
new_arr=np.concatenate((arr_1,arr_2))
print(new_arr)

arr2d_1=np.array([[1,2,3],[4,5,6]])
arr2d_2=np.array([[7,8,9],[10,11,12]])

# flattened concatenation 
new_arr2d_flat=np.concatenate((arr2d_1,arr2d_2),axis=None)
print(new_arr2d_flat)

# row wise concatenation
new_arr2d_row=np.concatenate((arr2d_1,arr2d_2),axis=0)
print(new_arr2d_row)

# column wise concatenation
new_arr2d_column=np.concatenate((arr2d_1,arr2d_2),axis=1)
print(new_arr2d_column)