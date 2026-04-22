with open('fahim.txt') as f:
    print(f.tell())
    print(f.readline())
    print(f.tell())
    print(f.readline())
    print(f.tell())
    print(f.readline())
    
    '''tell() function says you where your pointer is'''
    
    '''seek() function actually moves the pointer'''