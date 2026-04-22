# with open('pi.txt') as f:
#     contents = f.read()
#     print(contents)
    
#reading line by line

# with open("pi.txt") as f:
#     for line in f:
#         print(line)         #using rstrip() will remove the extra space


##making list from a file

with open('pi.txt') as f:
    lines = f.readlines()
    print(lines)
    for i in lines:
        print(i)

'''
if the file is in another folder that needs access then it should be with backslashes. 

with open('project\\file-1\\desired-file') as f:

working with relative file path is also a solution 

file_path = 'C:\\Users\\ehmatthes\\other_files\\text_files\\filename.txt'
with open(file_path) as file_object:



'''
