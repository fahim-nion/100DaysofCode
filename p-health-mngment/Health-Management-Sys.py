#Health Management System
'''

1. Objective
The goal is to create a Health Management System that can log and retrieve the diet and exercise routines of three specific clients.

2. Client Specifications [01:02]
The system must manage data for exactly three clients:

Harry

Rohan

Hammad

3. File Management [01:21]
You are required to manage a total of 6 files. Each client will have two dedicated files:

One file to log their Food/Diet data.

One file to log their Exercise data.

4. Functional Requirements
Data Logging Function [01:26]: Create a function that, when executed, asks for the client's name and then prompts the user to input what they want to log (either food or exercise).

Timestamp Integration [02:02]: You must use a helper function (typically named getdate()) that returns the current date and time using the datetime module. Every entry logged into a file must be prefixed with this timestamp.

Data Retrieval Function [03:54]: Create another function to retrieve and display the logged data. It should ask which client's data to view and whether the user wants to see the food log or the exercise log.

5. Helper Code Provided [02:13]
The video provides the following snippet to help with the timestamping:

Python
def getdate():
    import datetime
    return datetime.datetime.now()
6. Workflow Summary
Ask for Client: Select between Harry, Rohan, or Hammad.

Ask for Action: Choose between Logging (writing new data) or Retrieving (reading existing data).

Ask for Category: Choose between Food or Exercise.

Execute: Write to or read from the corresponding text file based on the selections above.
'''

def getDate():
    import datetime
    data = str(datetime.datetime.now())
    res = data.split(" ")
    return res

# print(getDate())


def dumpData(who,what,doing):
    if who.title() == "Harry":
        if what == 1:
            with open("harry_food.txt", "a") as f:
                f.write(f"{[getDate()]} : Harry had {doing}. \n")
        elif what == 2:
            with open("harry_exc.txt", "a") as f:
                f.write(f"{[getDate()]} : Harry had done {doing}. \n")
    if who.title() == "Rohan":
        with open("rohan_food.txt", "w") as f:
            f.write(f"{[getDate()]} : Rohan had {food}.\n")
    if who.title() == "Hammad":
        with open("hammad_food.txt", "w") as f:
            f.write(f"{[getDate()]} : Hammad had {food}.\n")
    
def loadData(who):
    if who.title() == "Harry":
        with open("harry_food.txt","r") as f1 , open("harry_exc.txt","r") as f2:
            content1 = f1.read()
            print(content1)

            content2 = f2.read()
            print(content2)
    if who.title() == "Rohan":
        with open("rohan_food.txt","r") as f1 , open("rohan_exc.txt","r") as f2:
            content1 = f1.read()
            print(content1)

            content2 = f2.read()
            print(content2)
    if who.title() == "Hammad":
        with open("hammad_food.txt","r") as f1 , open("hammad_exc.txt","r") as f2:
            content1 = f1.read()
            print(content1)

            content2 = f2.read()
            print(content2)
user_log = int(input(
    ''' 
    Welcome to the Health Data Management System!
    Press 1 for Harry
    Press 2 for Rohan
    Press 3 for Hammad
    '''
    ))


if user_log == 1:
    person = "harry"
    data = input(
        '''
        Welcome Harry!
        Press 1 to get data
        Press 2 to input Data
        '''
    )
    if data == 1:
        loadData(person)
    elif data == 2:
        updt_data = int(input('''
            Which data you want to input?
            Press 1 for Food Data.
            Press 2 for Excercise Data.
            '''))
        if updt_data == 1:
            doing = input("What did you just had? ")
        elif updt_data == 2:
            doing = input("What did you just do for excercise? ")
        dumpData(person,updt_data,doing)
        
elif user_log == 2:
    person = "rohan"
    data = input(
        '''
        Welcome Harry!
        Press 1 to get data
        Press 2 to input Data
        '''
    )
    if data == 1:
        loadData(person)
    elif data == 2:
        updt_data = int(input('''
            Which data you want to input?
            Press 1 for Food Data.
            Press 2 for Excercise Data.
            '''))
        if updt_data == 1:
            doing = input("What did you just had? ")
        elif updt_data == 2:
            doing = input("What did you just do for excercise? ")
        dumpData(person,updt_data,doing)
elif user_log == 3:
    person = "hammad"
    data = input(
        '''
        Welcome Harry!
        Press 1 to get data
        Press 2 to input Data
        '''
    )
    if data == 1:
        loadData(person)
    elif data == 2:
        updt_data = int(input('''
            Which data you want to input?
            Press 1 for Food Data.
            Press 2 for Excercise Data.
            '''))
        if updt_data == 1:
            doing = input("What did you just had? ")
        elif updt_data == 2:
            doing = input("What did you just do for excercise? ")
        dumpData(person,updt_data,doing)