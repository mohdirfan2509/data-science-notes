# axis=0 --> inserts row wise
# axis=1 --> inserts column wise

import numpy as np

arr_2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
modified_array=np.insert(arr_2d,1,[100,200,300],axis=0)
modified_array2=np.insert(arr_2d,1,[100,200,300],axis=1)
print(modified_array)
print(modified_array2)