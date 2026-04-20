#pattern printing

inp = int(input())
boolVal = int(input("Enter 0 or 1:"))

if boolVal == 1:
    for i in range(1,inp+1):
        print("*"*i, end="\n")
elif boolVal == 0:
    for i in range(inp,0,-1):
        print("*"*i, end="\n")