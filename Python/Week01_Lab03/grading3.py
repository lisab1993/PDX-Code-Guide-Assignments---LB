
#get the grade from the user as an integer.

while True:#I'm using a while loop so that the loop will repeat

    grade = input("Please enter your grade as a number between 0 and 100. When done, type done: \n>")#have the user input their grade as a number
    x = grade.isdigit()#our new variable x will check if the grade is a digit or not
    if x:#if x is true, continue to the statements below. Otherwise, go to the else statement at the bottom.
        grade = int(grade)#convert the grade back into an integer once it passes the test
        specific_grade = grade%10#use modulus 10 to get rid of the tens column. This particular variable will help us get a plus, minus, or regular grade below.




        if specific_grade >= 7:# We are only working with the tens column to get the proper symbol after the grade. If the ones place is 7 or higher, the user will have a + added to their score
            symbol = "+"
        elif specific_grade <= 3:#If the ones column is a 3 or lower, they will have a - added to their score
            symbol = "-"
        else:
            symbol = ""#If the ones column is less than 7 but greater than 3, they will not receive a + or - at the end of their score

        #use if statements to convert the letter to a number
        if grade > 89:
            print(f"You got an A{symbol}!")#and then add the symbol to the end of the letter grade
        elif grade > 79:
            print (f"You got a B{symbol}!")
        elif grade > 69:
            print (f"You got a C{symbol}!")
        elif grade > 59:
            print (f"You got a D{symbol}!")
        else:
            print ("You didn't pass this time.")
    else:
        if grade == "done":
            print("Thank you!")
            break
        print("Please enter a valid number: ")#If a statement is entered that is not a number between 0 and 100, the program will ask for a valid number, and won't end until it receives a valid number.
