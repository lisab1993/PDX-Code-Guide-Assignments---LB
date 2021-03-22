'''
Let's convert a dollar amount into a number of coins. 
The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
For this, you'll have to use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.


Welcome to the Change Maker 5000 (tm)
Enter a dollar amount: 1.36
5 quarters, 1 dime, and 1 penny
Would you like make more change? yes
Enter a dollar amount: 0.67
2 quarters, 1 dime, 1 nickel, 2 pennies
Would you like make more change? no
Have a good day!


Brain Dump:
- create a variable to get the dollar amount from the user as a float

-write a function to get the coin amounts
-multiply it by 100 to get the number of pennies. 

divide the number of pennies by 25 to get the number of quarters
divide it by %25 to get the remainder for other coins. 

'''





def get_coins(data):
    '''Tells you the smallest combination of coins needed to make a selected dollar/cent amount'''
    data = int(data * 100) #multiply it by 100 to get the number of pennies. 
    quarters = data // 25#floor divide by 25 to get the number of quarters as a whole number without a remainder
    data %= 25#same as data = data%25 #data %25 to find out what's left after we divide it by 25. The data variable will decrease as we account for more and more coins.
    dimes = data // 10
    data %= 10
    nickels = data // 5
    data %5
    pennies = data
    print(f"{quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")
    

amount = float(input("Please enter an amount of money in the following format: 1.50 \n>"))   #get the amount from the user.

print(get_coins(amount))