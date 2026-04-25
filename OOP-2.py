#instances and class variables

class Employee:
    num_of_leaves = 8
    #this property belongs to everyOne
    
    pass


harry = Employee()

rohan = Employee()

harry.name = "Harry"
harry.salary = 5000
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 3000
rohan.role = "Student"

#accessing differently
'''
print(rohan.num_of_leaves)
print(harry.num_of_leaves)
print(Employee.num_of_leaves)

'''

#but if we want to change the variable then it will be only changed by using the class name
print(Employee.num_of_leaves)

Employee.num_of_leaves = 9

rohan.num_of_leaves = 9 # instance variable
harry.num_of_leaves = 12
print(rohan.num_of_leaves)

print(rohan.__dict__)
print(harry.__dict__)
