#multiple inheritance

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

class Player:
    no_of_games = 4
    
    def __init__(self,name, game):
        self.name = name
        self.game = game
        
    def printDetails(self):
        return f"Name is {self.name}. Game is {self.game}"
    
class CoolProg(Employee, Player):
    pass
    
harry = Employee("Harry",5000,"Instructor")

rohan = Employee("Rohan",3000,"Student")

shubham = Player("Shubham", "Cricket")

karan = CoolProg("Karan",12000,"Cool Programmer")

print(karan.__dict__)
