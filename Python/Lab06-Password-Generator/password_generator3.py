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
print (password)



# Ask the user for how many lowercase letters, uppercase letters, numbers, and special characters they'd like in their password. 
# You do not want the pieces in order (e.g. 3 lowercase letters followed by 3 uppercase letters...). 
# You can use list(password_string) or password_string.split('') to convert the string to a list, random.shuffle(password_list) to shuffle it, and then ''.join(password_list) to turn it back into a string.

'''
requested_lower = input("How many lowercase letters would you like in your password: \n>")
requested_upper = input("How many uppercase letters would you like in your password: \n>")
requested_numbers = input("How many numbers would you like in your password: \n>")
requested_specials = input("How many special characters would you like in your password: \n>")

'''