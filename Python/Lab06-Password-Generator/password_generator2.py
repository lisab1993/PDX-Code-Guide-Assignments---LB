import random
import string


#long string with all possible characters
possibilities = string.ascii_letters + string.digits + string.punctuation

#make a blank string
password = ''

user_input = int(input("Please enter the length of your password as a digit: \n>"))#Get the user's request
length = user_input + 1#Add 1 so that the program won't stop at the number the user enters. 


x = 1#loop control
while x < length :#go through the list as many times as the user requests
    password += random.choice(possibilities)#Add selections into the blank password string
    x += 1#increase the loop control by 1
print(password)


# Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string.

