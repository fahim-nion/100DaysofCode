#Self & init


class Employee:
    num_of_leaves = 8
    
    def printDetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"

harry = Employee()

rohan = Employee()

harry.name = "Harry"
harry.salary = 5000
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 3000
rohan.role = "Student"

print(rohan.printDetails())