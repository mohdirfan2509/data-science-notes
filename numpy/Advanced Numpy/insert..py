# np.insert(array_name,index,value,axis)--> 
# default value of axis is None--> None "axis=None" means it will insert the value at specified index if it is a 1d array. if the array is 2d or 3d or etc... axis=None returns a copy of flattened array
# np.insert(array_name,index,value,axis)--> returns a new modified copy 
# the elements shift to the right when a new elements are inserted
# axis=0 --> inserts row wise
# axis=1 --> inserts column wise

import numpy as np

arr_1d=np.array([10,20,30,40,50,60])

modified_array=np.insert(arr_1d,2,400)
modified_array2=np.insert(arr_1d,2,400,axis=None)
print(modified_array)
print(modified_array2)