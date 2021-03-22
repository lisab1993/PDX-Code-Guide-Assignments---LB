import random

eyes = [":","X","8","=","D","D"]
nose = ["-","o","","@",'']
mouth = [")","(","3","D","P","O"]


i = 1#loop control
while i < 6:#I want it to loop 5 times, so I set it to 6
  print(random.choice(eyes) + random.choice(nose) + random.choice(mouth))#a random face will be generated
  i += 1#the control loop will increase by 1, so it will be able to sop after it has created 5 faces. 


