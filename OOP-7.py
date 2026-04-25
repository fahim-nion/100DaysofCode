#inheritance



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
    def __init__(self, name, sal, role,lang):
        self.name = name
        self.salary = sal
        self.role = role
        self.language = lang
        
        #can be used super() here
    def printProg(self):
        return f"Programmer Name is {self.name}. Salary is {self.salary} and role is {self.role} and knows {self.language}"



harry = Employee("Harry",5000,"Instructor")

rohan = Employee("Rohan",3000,"Student")

shubham = Programmer("Shubham", 8000, "Programmer",["C","JavaScript"])
karan = Programmer("Karan", 10000, "Programmer",["C","Python","Dart"])


# print(rohan.printGood("wow string"))
print(karan.printProg())

