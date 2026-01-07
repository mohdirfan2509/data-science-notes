# np.delete(array_name, index, axis=None)
# axis=None --> flattens the array

import numpy as np

arr_1=np.array([10,20,30,40,50])

modified_arr_1=np.delete(arr_1,2)
print(modified_arr_1)
