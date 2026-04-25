#inheritance


#Static Method


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
        
    @staticmethod
    def printGood(string):
        return(f"This is a good string executed with {string}")

class Programmer(Employee):
    def printProg(self):
        return f"Programmer Name is {self.name}. Salary is {self.salary} and role is {self.role}"



harry = Employee("Harry",5000,"Instructor")

rohan = Employee("Rohan",3000,"Student")

shubham = Programmer("Shubham", 8000, "Programmer")
karan = Programmer("Karan", 10000, "Programmer")


# print(rohan.printGood("wow string"))
print(karan.printProg())

