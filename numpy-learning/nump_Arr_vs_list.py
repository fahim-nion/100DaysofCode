import numpy as np

list_A = range(100)
arr_A = np.arange(100)
print(list(list_A))
print(arr_A)

#now we want to figure out which array is consuming how much memory

import sys

print(sys.getsizeof())