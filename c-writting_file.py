# with open('pi.txt','w') as f:
#     f.write("i am fahim.\n") #completely erasing the prev file texts
#     f.write("this is second line")
    

'''
"a" mode is for append
"r+" is for read and write

Python can only write strings to a text file. If you want to store numerical data in a 
text file, you’ll have to convert the data to string format first using the str() function.
'''
##appending to a file

with open('pi.txt',"r+") as f:
    c = f.read()
    print(c)

    f.write("\n3.1415926535\n")
    f.write("\t8979323846\n")
    f.write("\t2643383279\n")
    f.seek(0)           #moving the cursor in front
    c2 = f.read()
    print(c2)
