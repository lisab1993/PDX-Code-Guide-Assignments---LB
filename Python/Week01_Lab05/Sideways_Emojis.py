import random


eyes = ["^","+","-","T"]#only one list is needed for the eyes since they'll match
mouth = ["-","o", "^"]
both_eyes = random.choice(eyes)#make a variable to select an option from the eyes list

print("Let's make an eastern-style emoji!")
print(both_eyes + random.choice(mouth) + both_eyes)#use the variable to keep the eye style the same.


