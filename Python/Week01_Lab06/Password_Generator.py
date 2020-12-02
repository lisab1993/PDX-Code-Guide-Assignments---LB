import random
import string


#long string with all possible characters
possibilities = string.ascii_letters + string.digits + string.punctuation

#blank string, not a blank list
password = ''

x = 1
while x < 11:#go through the list ten times
    password += random.choice(possibilities)
    x += 1
print (password)

'''
for y in range (10): #cycle through the list 10 times, which will result in choosing a random character 10 times, then the loop will end. 
  password += random.choice(x) #add random.choice(x(variable from above)) to the blank list for cycling.
print(password)
'''
