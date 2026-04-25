# def func1():
#     print("Sub now")
    
# func2 = func1
# del func1 
# func2()

# def funcret(num):
#     if num == 0:
#         return print
#     if num == 1:
#         return sum
    
# a = funcret(0)
# print(a)

# def executor(func):
#     func("this")
    
    
# executor(print)


def dec1(func1):
    def nowExec():
        print("Executing Now!!")
        func1()
        print("Executed")
    return nowExec

@dec1
def who():
    print("This is me saying!")
    
    
# whois = dec1(who)
who()