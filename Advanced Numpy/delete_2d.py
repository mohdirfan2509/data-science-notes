import numpy as np

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
modified_arr_2d=np.delete(arr_2d,1,axis=0)
print(modified_arr_2d)
modified_arr2_2d=np.delete(arr_2d,1,axis=1)
print(modified_arr2_2d)
modified_flatten=np.delete(arr_2d,1,axis=None)
print(modified_flatten)