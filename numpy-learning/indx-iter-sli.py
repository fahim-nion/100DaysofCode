#indexing - iteration - slicing

import numpy as np
arr12 = np.arange(24)
# print(arr12)

'''
prints this

[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
but i want to see it as a 6x4
lets use reshape()

'''

arr12 = (arr12.reshape(6,4))
print(arr12)

print("----------------------")


'''
now it prints

[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]
 [12 13 14 15]
 [16 17 18 19]
 [20 21 22 23]]



'''

#print(arr12[2])  #we can achieve 2nd row from this but if we want to achieve 3rd row how can i achieve that?

print(arr12[:,2])

#now if we want 2nd and 3rd column then

print(arr12[:,2:4])

#updated


