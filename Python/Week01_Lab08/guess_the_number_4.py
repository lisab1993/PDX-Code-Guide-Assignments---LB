import random

computer_selection = random.randint(2,9)#The computer will choose a number between 1 and 10, but not 1 or 10 themselves

print("Welcome to the guessing game.!")#Welcome screen
older_guess = int(input("Guess a number between 1 and 10.\n> "))#The first guess of the game, and the oldest guess for all rounds after.


if older_guess == computer_selection:#if the user is correct on the first try, end the game
    print(f"You got it! The answer was {computer_selection}.")  
else:
    newer_guess = int(input("That wasn't it, try again:\n> "))#I don't want this to loop around

while True:
        if newer_guess == computer_selection:#I do want lines 14 - 22 to loop
          print(f"You got it! The answer was {computer_selection}.")
          break
        else:
            if abs(newer_guess - computer_selection) < abs(older_guess - computer_selection):#if the absolute value of the current guess is smaller than the absolute value of the older guess, then you are closer. 
                print("You're getting warmer!")#keep the statements about being warmer or colder separate from the input line
                older_guess = newer_guess#their previous older guess is now obsolete, so let's overwrite it
                newer_guess = int(input("Try again:\n>"))#after we overwrite the older guess, let's get the newest guess

            else:
                print("You're getting colder!")#the only thing that changes in this block of code, is that we will tell the user they are colder rather than hotter.
                older_guess = newer_guess
                newer_guess = int(input("Try again:\n"))