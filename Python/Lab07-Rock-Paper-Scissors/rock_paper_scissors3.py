import random


#True is my loop control
while True:
    choices = ["rock","paper","scissors","lizard","spock"]#A list of options for the computer to choose from
    computer_input = random.choice(choices)#The computer will randomly choice from the choices list

    print("Welcome!")#welcome screen
    send_it = input("Would you like to play rock, paper, scissors against the computer? Please enter yes or no: \n>").lower()
    print(send_it) 

    if send_it == "yes":#only ask the user to choose rock, paper, or scissors if they actually want to play. 
        user_input = input("Please select your office weapon (rock, paper, or scissors): \n>")
        if user_input == computer_input:
            print("It's a tie")

        elif user_input == "rock" and computer_input == "paper":
            print("The computer wins!")
        elif user_input == "rock" and computer_input== "scissors":
            print("You win!")
        elif user_input == "rock" and computer_input =="lizard":
            

        elif user_input == "paper" and computer_input == "scissors":
            print("The computer wins!")
        elif user_input == "paper" and computer_input == "rock":
            print("You win!")

        elif user_input == "scissors" and computer_input == "rock":
            print("The computer wins!")
        elif user_input == "scissors" and computer_input == "paper":
            print("You win!")
    else:
        print("Thank you for playing, have a great day!!!")
        break
