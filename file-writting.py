f = open("fahim.txt", "rt")  #rb, read mode & binary mode #rt read text[keeps original formatting]

print(f.readlines()) #[to print lines as a list]

print(f.readline()) #using readline will read one line only
print(f.readline()) #using readline will read next line 
print(f.readline()) #using readline will read next line

content = f.read(3) #putting read(3) here means it will read 3 characters only
print(content)

#again using this one will NOT output the same

content = f.read(3) #putting read(3) here means it will read  next 3 characters only
print(content)

content = f.read(340) #putting read(3) here means it will read 3 characters only
print(content)

#it has read all the text in the third call, if it calls again then it will stay empty

content = f.read(30) 
print("empty content:",content)

f.close() #don't forget to close this one, it is a good practice



for line in f:
    print(line, end="")  #after each line this will contain a \n, using end will stop it

"to print line by line you dont need to use f.read()"



