# to change the elements(data) from one type to another type
# arr.astype(new_type)--> return an array with elements changed to new type

import numpy as np

flt_arr=np.array([1.2,3.45,2.6,7.8])
print(flt_arr.dtype) # float64
int_arr=flt_arr.astype(int)
print(int_arr.dtype) # int64