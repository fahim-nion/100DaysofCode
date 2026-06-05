import numpy as np

list_A = range(100)
arr_A = np.arange(100)
# print(list(list_A))
# print(arr_A)

#now we want to figure out which array is consuming how much memory

import sys

# print(sys.getsizeof(87)*len(list_A))   #2800

# the initial list A contains numbers between 1 to 99. Now the purpose for this block of code is, taking a random number that exists in the list and then getsizeof() function does what is it gets the one elements size and then multiplies with the total number of size of that list.


# print(arr_A.itemsize*arr_A.size)

import time

x = range(10000000)
y = range(10000000,20000000)

start_time = time.time()

c = [x+y for x,y in zip(x,y)]

print(time.time() - start_time)

a = np.arange(10000000)
b = np.arange(10000000,20000000)
s_t = time.time()
c = a+b                         #it does the same what this line does [x+y for x,y in zip(x,y)]
print(time.time()-s_t)