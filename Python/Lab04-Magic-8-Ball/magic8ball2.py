import random#this module is needed to randomly select an option from the list


while True:
    #magic 8 ball possible predictions
    prediction = ["It is certain","It is decidedly so","Without a doubt","Yes definitely"]
    random_answer = random.choice(prediction)#this variable will get us a random selection from the list

    #welcome screen
    print("Welcome to the Magic 8 Ball Game!")
    question = input("What question can the magic 8 ball answer for you? When you are done, enter \"done\" \n>")#get the question from the user
    if question == "done":#If the user enters done, the program will say "thanks for playing" and end
        print("Thank you for playing! ")
        break
    else:#if the user enters anything other than done, the program will continue and then loop.
        print(random_answer)#call up a random option from the list after the user enters a question.











'''
-Logic
If the user enters done, I want to stop. If they enter anything else, I want to continue. 


-To Do List
make a welcome screen to the game
if statement: if question does not equal done, then get a random option. If question does equal done, we want to say "thank you for playing" at the bottom. 
    if question != done:
        *actual code*
    else:
        print("Thank you for playing")

'''