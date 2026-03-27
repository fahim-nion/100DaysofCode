'''
a random num,
user will input the number 7 times
the programme will say is it lower or higher
failed then prints game over
'''

import random
num = random.randint(1,100)
print(num)

print("Hello to the number guessing game!")
print("I have guessed a number now start guessing!")
count = 7
while True:
    print(f"You have {count} guesses remaining!")
    user_inp = int(input("Please Enter:"))
    
    if user_inp > num:
        print("Wrong guess! Try Lower!!")
        count-=1
    elif user_inp < num:
        print("Wrong guess! Try Higher!!")
        count-=1
    elif user_inp == num:
        print("Congratulations! \nYou Guessed it Right")
        break
    if count == 0:
        print("Game Over Mate!")
        break
    