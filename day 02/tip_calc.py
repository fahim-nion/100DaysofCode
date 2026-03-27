print("Welcome to the tip calculator")

total = float(input("What was the total bill? $"))
tip_percentage = float(input("How much tip would you like to give? 10, 12, or 15? \n"))
people = int(input("How many people to split the bill with? "))
pay = (total + (total*(tip_percentage/100)))/people
print(f"Each person should pay ${round(pay,2)}")