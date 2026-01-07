# np.nan_to_num(array_name,nan=value) --> returns the new array
# replaces all the "nan" to specified value if not specified default value s "0" 

import numpy as np

arr1=np.array([1,2,np.nan,3,4,np.nan,6])
cleaned_arr1=np.nan_to_num(arr1)
