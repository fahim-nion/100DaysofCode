#Self & init


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

harry = Employee("Harry",5000,"Instructor")

rohan = Employee("Rohan",3000,"Student")

# harry.name = "Harry"
# harry.salary = "Harry"
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 3000
# rohan.role = "Student"

print(rohan.printDetails())
print(harry.printDetails())