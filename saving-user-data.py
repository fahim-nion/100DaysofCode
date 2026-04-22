import json

username = input("Enter Your name to get registered:")

file_name = 'users.json'

with open('users.json',"w") as f:
    json.dump(username,f)
    print(f"Registered! You will be remembered when you get back! {username}")
    
