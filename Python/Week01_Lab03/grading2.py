
#get the grade from the user as an integer.
grade = int(input("Please enter your grade as a number between 0 and 100: \n>"))
specific_grade = grade%10

if specific_grade >= 7:
    symbol = "+"
elif specific_grade <= 3:
    symbol = "-"
else:
    symbol = ""

#use if statements to convert the letter to a number
if grade > 89:
    print(f"You got an A{symbol}!")
elif grade > 79:
    print (f"You got a B{symbol}!")
elif grade > 69:
    print (f"You got a C{symbol}!")
elif grade > 59:
    print (f"You got a D{symbol}!")
else:
    print ("You didn't pass this time.")
