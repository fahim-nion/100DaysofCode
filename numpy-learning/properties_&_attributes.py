import numpy as np

arr2 = np.array([[1,2,3],[4,5,6]])

# print(arr2.shape)

#Prints (2, 3)\
    
    
arr9 = np.array([[[1,2],[3,4]],[[5,6],[9,8]]])
# zer = np.zeros(10)
lin = np.linspace(5,20,9)
arr7 = np.linspace(18,20,9)

# print(arr9)
# print(arr9.shape)
# print(arr9.ndim)

#these are not functions, these are attributes

# print(arr9.size)
# print(arr9.itemsize)
# print(zer.itemsize)
# print(lin)
# print(arr7)
# print(lin.itemsize)
# print(lin.dtype)

arr9_float = arr9.astype('float')
print(arr9_float)
print(arr9_float.dtype)