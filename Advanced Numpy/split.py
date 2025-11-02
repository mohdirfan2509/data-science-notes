# np.split(array_name,number of arrays)

import numpy as np

arr_1=np.array([10,20,30,40,50,60])
splitted_arr_1=np.split(arr_1,2)
print(splitted_arr_1)

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
splitted_arr_2d=np.split(arr_2d,2)
print(splitted_arr_2d)