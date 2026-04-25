#public private & protected access specifiers

'''
public- anyone can see
protected - only my home people can see
private - none can see but me
'''



#Static Method


class Employee:
    num_of_leaves = 8
    var =99
    _protect = 69
    
    
    #Constructor
    def __init__(self, name, sal, role):
        self.name = name
        self.salary = sal
        self.role = role
        
    #this is method
    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    
    @classmethod
    def change_leaves(cls, newleaves):
        cls.change_leaves = newleaves
        
    @staticmethod
    def printGood(string):
        return(f"This is a good string executed with {string}")

harry = Employee("Harry",5000,"Instructor")

rohan = Employee("Rohan",3000,"Student")

print(_emp.protect)