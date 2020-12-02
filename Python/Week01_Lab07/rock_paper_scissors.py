import random

choices = ["rock","paper","scissors"]

#welcome screen
print("Welcome to Rock, Paper, Scissors!")
user_input = input("Please select either rock, paper, or scissors: \n>").lower
computer_input = random.choice(choices)


if user_input == computer_input:
    print("It's a tie")

elif user_input == "rock" and computer_input == "paper":
    print("The computer wins!")
elif user_input == "rock" and computer_input== "scissors":
    print("You win!")

elif user_input == "paper" and computer_input == "scissors":
    print("The computer wins!")
elif user_input == "paper" and computer_input == "rock":
    print("You win!")

elif user_input == "scissors" and computer_input == "rock":
    print("The computer wins!")
else:
    print("You win!")




'''
The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper (tie)
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)
'''


'''
Make a welcome screen
ask the user for their input

have the computer select a random choice 

compare the user's choice to the computer's choice



'''