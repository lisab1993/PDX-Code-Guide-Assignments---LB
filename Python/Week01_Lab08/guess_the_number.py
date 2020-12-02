import random

#Computer selects a number
computer_selection = random.randint(2,9)#Set to 2 and 9 so that the computer doesn't guess 1 or 10.
#User enters their guess

x=0
while x < 10 :#I want the program to loop 10 times
    user_guess = int(input("Please guess a number between 1 and 10.  \n>"))
#if user guess == computer selection, the user will be told they're right
    if user_guess == computer_selection:
      print("Yay!!! You guessed the number. You must be psychic.")
      break
#if the user doesn't guess the number, they'll be told they're incorrect.
    else:
      print("Sorry, that's not it!")
      x += 1
else:#At the 11th guess, x will no longer be less than 10, and the loop will continue to the else statement at the bottom.
    print("Better luck next time")
    



'''
Let's play 'Guess the Number'. 
The computer will guess a random int between 1 and 10.
 The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Using a while loop, allow the user to guess 10 times. 
If they fail to guess the number after 10 tries, the user is told they've lost. 
If the user guesses the number, the user is told they've won and the game exits. 
You can get a random number using random.randint:
'''

