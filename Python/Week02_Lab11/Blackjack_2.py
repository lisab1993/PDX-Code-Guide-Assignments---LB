'''
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. 
Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. 
Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

'''
#create a dictionary the cards as the keys, and their numerical value as the dictionary value.
options = {
    "Ace": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    }

def blackjack(num):#left empty to keep the card input variables within the function for readibility.
    '''Advises to hit, stay, blackjack, or busted in a game of blackjack'''   
    first_card = input("What's your first card? Acceptable answers are 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, or Ace.\n>")#Get the card data from the user as strings.
    second_card = input("What's your second card? \n>")
    third_card = input("What's your third card?\n>")
   
    first_card_value = options[first_card]#Use the user input to access their dictionary values 
    second_card_value = options[second_card]#Do this for all 3 cards. 
    third_card_value = options[third_card]

    current_total = first_card_value + second_card_value + third_card_value#Put the total in it's own value. Add the values of the cards up to see where we're at.
    print(f"Your current total is {current_total}")
    if current_total < 17:#Less than 17, advise to "Hit"
        print("hit")
    elif current_total >= 17 and current_total < 21:#Greater than or equal to 17, but less than 21, advise to "Stay"
        print("stay")
    elif current_total == 21:#Exactly 21, advise "Blackjack!"
        print("Blackjack!!!")
    else:                     #Over 21, advise "Already Busted"
        print("Already Busted")
    

print(blackjack(3))
