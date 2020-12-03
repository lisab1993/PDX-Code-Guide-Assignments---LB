import random

#Computer selects a number
computer_selection = random.randint(2,9)#Set to 2 and 9 so that the computer doesn't guess 1 or 10.

x=1#the loop control is set to 1 so that the program will count the first guess as 1.
while x >=1 :#I want the program to loop infinitely. Since it's impossible for x to be less than 1, the user has infinite guesses.
    user_guess = int(input("Please guess a number between 1 and 10.  \n>"))#User enters their guess
    if user_guess < computer_selection:#If the user guesses lower than the computer's number
        print("Too low, try again.")
        x += 1#                            Add 1 to the loop control to keep track of the number of guesses
    elif user_guess > computer_selection:#If the user guesses higher than the computer's number
        print("Too high, try again.")
        x += 1#                             Add 1 to the loop control
    else:
        print(f"You got it!!! The number was {computer_selection}")#If the user guesses correctly
        print (f"You got it in {x} guesses.")#Number of guesses the player needed
        break#The program will end when you guess correctly.
