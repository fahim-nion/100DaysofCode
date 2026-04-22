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

import datetime

def getDate():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")



def dumpData(who, what, doing):
    file_type = "food" if what == 1 else "exc"
    filename = f"{who.lower()}_{file_type}.txt"

    action = "had" if what == 1 else "did"

    with open(filename, "a") as f:
        f.write(f"[{getDate()}] : {who.title()} {action} {doing}\n")

    print("Data saved successfully!")


def loadData(who):
    files = [
        f"{who.lower()}_food.txt",
        f"{who.lower()}_exc.txt"
    ]

    for file in files:
        print(f"\n--- {file} ---")
        try:
            with open(file, "r") as f:
                print(f.read())
        except FileNotFoundError:
            print("No data found.")


people = {
    1: "harry",
    2: "rohan",
    3: "hammad"
}

try:
    user_log = int(input(
        '''
Welcome to the Health Data Management System!
Press 1 for Harry
Press 2 for Rohan
Press 3 for Hammad
: '''
    ))

    if user_log not in people:
        print("Invalid choice")
    else:
        person = people[user_log]

        data = int(input(
            f'''
Welcome {person.title()}!
Press 1 to get data
Press 2 to input data
: '''
        ))

        if data == 1:
            loadData(person)

        elif data == 2:
            updt_data = int(input('''
Which data you want to input?
Press 1 for Food Data
Press 2 for Exercise Data
: '''))

            if updt_data not in [1, 2]:
                print("Invalid choice")
            else:
                if updt_data == 1:
                    doing = input("What did you eat? ")
                else:
                    doing = input("What exercise did you do? ")

                dumpData(person, updt_data, doing)

        else:
            print("Invalid choice")

except ValueError:
    print("Please enter numbers only!")
    
    