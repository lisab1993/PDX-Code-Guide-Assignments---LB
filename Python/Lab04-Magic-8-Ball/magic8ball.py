import random#this module is needed to randomly select an option from the list

#magic 8 ball possible predictions
prediction = ["It is certain","It is decidedly so","Without a doubt","Yes definitely"]
random_answer = random.choice(prediction)#this variable will get us a random selection from the list

#welcome screen
print("Welcome to the Magic 8 Ball Game!")
question = input("What question can the magic 8 ball answer for you? \n>")#get the question from the user
print(random_answer)#call up a random option from the list after the user enters a question.



'''
-Logic
have the user ask a question
the answer will be randomly chosen from a list
the output will come from a list of predictions



-To Do List
welcome screen (hi, welcome to the program)
user input (please enter your question)
make the list with predictions

'''
