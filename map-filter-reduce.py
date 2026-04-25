'''num = ["1","34","6"]

summation = list(map(int, num))
print(summation)


def sq(a):
    return a*a

nums = [2,3,3,1,4,2,8]

# square = list(map(sq, nums))
# print(square)

square = list(map(lambda x : x*x, nums))
print(square)'''




# def sq(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [sq, cube]
# # nums = [2,3,3,1,4,2,8]

# for i in range(5):
#     val = list(map(lambda x:x(i),func))
#     print(val)
    
    
    
#filter function-------------------------

# lsi = [1,2,3,4,5,6,7,8,9]

# def is_greater_5(n):
#     return n>5

# #takes a function and then the list to work on
# gt_than_5 = list(filter(is_greater_5,lsi))
# print(gt_than_5)


#reduce function_=========================
from functools import reduce

lis = [1,2,3,4]

#want to sum each elem

numb = reduce(lambda x,y:x+y, lis)

print(numb)