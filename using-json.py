import json
# numbers = [2,3,5,7,11,13]

file_name = 'numbers.json'

# with open('numbers.json',"w") as f:
#     json.dump(numbers,f)

with open('numbers.json') as f:
    jsonData = json.load(f)
    
print(jsonData)