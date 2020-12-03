import random

#Computer selects a number
computer_selection = random.randint(2,9)#Set to 2 and 9 so that the computer doesn't guess 1 or 10.

x=1#the loop control is set to 1 so that the program will count the first guess as 1.
while x >=1 :#I want the program to loop infinitely. Since it's impossible for x to be less than 1, the user has infinite guesses.
    user_guess = int(input("Please guess a number between 1 and 10.  \n>"))#User enters their guess

    if user_guess == computer_selection:#if user guess == computer selection, the user will be told they're right
      print("Yay!!! You guessed the number. You must be psychic.")#correct guess
      print(f"You guessed {x} times.")#number of guesses
      break#stop running when the user guesses right.

    else:
      print("Sorry, that's not it!")#if the user doesn't guess the number, they'll be told they're incorrect.
      x += 1#Keep track of the number of guesses
