# np.vstack((arr1,arr2,arr3,...))--> vertically stack (row wise)
# np.hstack((arr1,arr2,arr3,...))--> horizontally stack (column wise)

import numpy as np

arr_1=np.array([[1,2,3]])
arr_2=np.array([[4,5,6]])
arr_3=np.array([[7,8,9]])

vstacked_array=np.vstack((arr_1,arr_2,arr_3))
hstacked_array=np.hstack((arr_1,arr_2,arr_3))

print(vstacked_array)
print(hstacked_array)

