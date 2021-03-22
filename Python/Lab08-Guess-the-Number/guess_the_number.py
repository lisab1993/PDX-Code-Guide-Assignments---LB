import random

#Computer selects a number
computer_selection = random.randint(2,9)#Set to 2 and 9 so that the computer doesn't guess 1 or 10.

x=1#Set to 1 so that the program will start counting the user's guesses at 1.
while x < 11 :#I want the game to loop ten times, and I set it to eleven to account for the user's guess.
    user_guess = int(input("Please guess a number between 1 and 10.  \n>"))#User enters their guess

    if user_guess == computer_selection:#if user guess == computer selection, the user will be told they're right
      print("Yay!!! You guessed the number. You must be psychic.")#correct guess
      print(f"You guessed {x} times.")#number of guesses
      break#If the user guesses right, stop the program. 

    else:
      print("Sorry, that's not it!")#if the user doesn't guess the number, they'll be told they're incorrect.
      x += 1
else:#At the 11th guess, x will no longer be less than 10, and the loop will continue to the else statement at the bottom.
    print("Better luck next time")
    