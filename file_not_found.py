'''with open("alice.txt", "r+") as f:
    c = f.open()
    print(c)
    
    #throws an FileNotFoundError
    
    '''
    
try:
    with open('alice.txt', "r+") as f:
        c = f.read()
except FileNotFoundError:
    print("Sorry brothe the file does not exists!!!")    