# NumPy Type Promotion Hierarchy in numpy
# bool → int → float → complex → string → object
import numpy as np

arr_1=np.array([1,2,3])
arr_2=np.array([1,2,3.4])
arr_3=np.array([1,2,"hi"])
print(arr_1.dtype)
print(arr_2.dtype)
print(arr_3.dtype)