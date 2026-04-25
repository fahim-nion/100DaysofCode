

class Employee:
    num_of_leaves = 8
    
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
        
    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))
        

harry = Employee("Harry",5000,"Instructor")

rohan = Employee("Rohan",3000,"Student")

karan = Employee.from_str("Karan-2000-Student")

# print(karan.num_of_leaves)
print(karan.__dict__)