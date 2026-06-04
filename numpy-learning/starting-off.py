import numpy as np

arr = np.array([1,2,3,4,5,60], dtype=int)

# print(arr)
# print(type(arr))

#2D array


arr2 = np.array([[1,2,3],[4,5,6]])

# print(arr2)
# print(type(arr2))

arr3 = np.zeros((2,3))  #row column

# print(arr3)

arr4 = np.ones((3,3))

# print(arr4)

arr5 = np.identity(5)  #2D Array though 
# print(arr5)

arr6 = np.arange(5,16)      #SES method can also be applied here. (5,6,2)  [5 7 9 11 13 15]

# print(arr6)


arr7 = np.linspace(10,20,10)

print(arr7)

arr8 = arr7.copy()
#numpy arrays can also be coppied.

