import random

#a list for each facial feature
eyes = [":","X","8","=","D","D"]
nose = ["-","o","","@",'']
mouth = [")","(","3","D","P","O"]

#welcome screen
print("Let's make an emoji!")
print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))





'''
Add a welcome screen

Make a list for the eyes, nose, and mouth.
use random.choice() on each list to get a random selection
concatenation will keep the face in order.

'''