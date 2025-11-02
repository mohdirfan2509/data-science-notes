# Broadcasting is the process by which NumPy performs element-wise arithmetic operations on arrays of different shapes by automatically expanding one or more arrays along dimensions where their sizes are 1 (or missing), so that their shapes become compatible according to specific broadcasting rules.

# Broadcasting Rules (Technical)

# When performing operations on two arrays, NumPy compares their shapes element-wise from right to left:

# 1.If the dimensions are equal, they are compatible.

# 2.If one of the dimensions is 1, it can be stretched to match the other.

# 3.If the dimensions are different and neither is 1, they are incompatible, and NumPy raises a ValueError.

import numpy as np

prices=np.array([100,200,300])
discount=10
final_prices=prices- (discount*prices)/100
print(final_prices)
