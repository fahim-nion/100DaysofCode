#Super()  and Overriding

class A:
    classVar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A constructor"
        self.classVar1 = "i am from constructor"
        self.special = "special"
        

class B(A):
    classVar1 = "I am in class B"
    def __init__(self):
        super().__init__()
        self.var1 = "I am inside class B constructor"
        self.classVar1 = "i am from B constructor"
    
    
    
a = A()
b = B()

print(b.classVar1)
print(b.special)