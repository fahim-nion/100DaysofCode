'''you have to design a faulty calcultor
wrong calc will be;
- 45*3 = 555
- 56 + 9 = 77
- 56 /4 = 4

'''

def calc (a,b,op):
    if ((a == 45 and b == 3) or (a == 3 and b == 45)) and op == "*":
        return 555
    elif ((a == 56 and b == 9) or (a == 9 and b == 56) and op == "+"):
        return 77
    elif (a == 56 and b == 4 and op == "/"):
        return 4
    else:
        if op == "+":
            return a+b
        
        if op == "-":
            return a-b
        
        if op == "*":
            return a*b
        
        if op == "/":
            return a/b
        
        
        
print("Welcome to the magic calculator")
inp1 = int(input("Enter first value: "))
inp2 = int(input("Enter second value: "))
inp3 = input("& what do you want to do with them?")
print(f"Your Sum is {calc(inp1,inp2,inp3)}")