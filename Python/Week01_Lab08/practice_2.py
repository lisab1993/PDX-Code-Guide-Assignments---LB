#import random
#import string

#create the dictionary
profile = {
    "username":"gandalfTheGrey",
    "password":"noneShallPass!"
}

#Create a login function
def login():
    if username_attempt == profile["username"] and password_attempt == profile["password"]:
      return True
    else:
      return False


while True:
    username_attempt = input("Please enter your username ")
    password_attempt = input("Please enter your password ")
    if login() == True:
      print("Welcome gandalfTheGrey!!!")
      break
    else:
      print("Oops, try again: ")