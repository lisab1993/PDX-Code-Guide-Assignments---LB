


class ATM:
    def __init__(self):
        self.balance = 0#newly created accounts always default to a balance of zero, and a self interest rate of 0.1
        self.interest_rate = 0.1#this and self.balance are the two class attributes
        
    def check_balance(self):#this is a method. So are the other methods listed below.
        '''checks the account balance'''
        print(f"You currently have {self.balance} dollars in your account.")

    def deposit(self, amount):
        '''adds money to the account'''
        deposit =(self.balance + amount)
        self.balance += amount
        print(f"Thank you. You now have {self.balance} dollars in your account.")
        

    def check_withdrawal(self, amount):
        '''withdraws money from the account'''
        withdraw = (self.balance - amount)
        self.balance -= amount
        print(f"Thank you. You now have {self.balance} dollars in your account.")

    def calc_interest(self):
        pass


#the code below was taken from the lab assignment and adjusted along the way.
atm = ATM() # create an instance of our class
print('Welcome to the ATM')#welcome screen
while True:
    command = input('Enter a command (balance, deposit, withdraw, interest, help, or exit)\n>')#ask the user for their command
    if command == 'balance':
        balance = atm.check_balance() # call the balance() method
        print(f'Your balance is ${balance}')

    elif command == 'deposit':
        amount = float(input('How much would you like to deposit?\n>'))
        atm.deposit(amount) # call the deposit(amount) method
        print(f'Deposited ${amount}')

    elif command == 'withdraw':
        amount = float(input('How much would you like to withdraw?\n>'))
        if atm.check_withdrawal(amount): # call the check_withdrawal(amount) method
            atm.withdraw(amount) # call the withdraw(amount) method
            print(f'Withdrew ${amount}')
        else:
            print('Insufficient funds')

    elif command == 'interest':
        amount = atm.calc_interest() # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'help':
        print('Available commands:')
        print('balance  - get the current balance')
        print('deposit  - deposit money')
        print('withdraw - withdraw money')
        print('interest - accumulate interest')
        print('exit     - exit the program')

    elif command == 'exit':
        break
    else:
        print('Command not recognized')