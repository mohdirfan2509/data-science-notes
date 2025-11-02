# np.isnan(array_name)--> returns a boolean array that has true in the place of "nan" values and False elsewhere

import numpy as np

arr1=np.array([1,2,np.nan,3,4,np.nan,6])
print(np.isnan(arr1)) 