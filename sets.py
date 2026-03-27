s = set()

set_from_list = set([1,2,3,4])

# print(set_from_list)

set_from_list.add(1) #will have no effect cuz 1 exists already
set_from_list.add(11)
# print(set_from_list)

#set always carries unique values

s.add(1)
s.add(2)
s.add(9)

# print(s)

s_updated = s.union({1,2,5})
s_updated_int = s.intersection({1,2,5,9})
print(s)
# print(s_updated)
print(s_updated_int)