import random

print("--------Hey Welcome to the [[Snake ** Water ** Gun ]] game--------")

print(''' 
Here you will guess one item from:
[[Snake ** Water ** Gun]]

Press "S" for Snake
Press "W" for Water
Press "G" for Gun

Let's Begin!!!
''')

inp = int(input("How many times you wanna play? "))

tray = ["Snake", "Water", "Gun"]

me = 0
computer = 0
i = 1

def user_slct(arg):
    if arg.upper() == "S":
        return "Snake"
    elif arg.upper() == "W":
        return "Water"
    elif arg.upper() == "G":
        return "Gun"
    else:
        return None

while i <= inp:
    print(f"\nRound {i}")
    
    com_choice = random.choice(tray)
    user_inp = input("Choose (S/W/G): ")
    user_choice = user_slct(user_inp)

    if user_choice is None:
        print("Invalid Input! Try again.")
        continue

    print(f"Computer chose: {com_choice}")

    if user_choice == com_choice:
        print("Nobody won! It's a draw.")
    elif user_choice == "Gun":
        if com_choice == "Water":
            print("Computer Won!")
            computer += 1
        else:
            print("You Won!")
            me += 1
    elif user_choice == "Water":
        if com_choice == "Snake":
            print("Computer Won!")
            computer += 1
        else:
            print("You Won!")
            me += 1
    elif user_choice == "Snake":
        if com_choice == "Gun":
            print("Computer Won!")
            computer += 1
        else:
            print("You Won!")
            me += 1

    i += 1  # FIX: increment loop

# Final Result (after all rounds)
print("\n----- Final Result -----")
print(f"You won: {me} times")
print(f"Computer won: {computer} times")

if me > computer:
    print("🎉 Congratulations! You are the overall winner!")
elif computer > me:
    print("😢 Sorry! Computer wins the game.")
else:
    print("🤝 It's a tie overall!")
    