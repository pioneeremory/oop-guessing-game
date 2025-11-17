# ATM Challenge Requirements:
# User login with pin
# account selection
# view balance
# deposit
# withdraw
# logout

# UI, insert card, enter PIN, choose withdraw or deposit, account update, finished? 
# confirm logout
class ATM():
    def __init__(self, current_user):
        self.current_user = current_user
    
    def validate_pin(self, pin):
        self.pin = pin
        return self.pin == enter_pin
        
    def get_balance(self, balance):
        self.balance = balance
        print(f'Your balance is {current_user.balance}.')
    
    def deposit(self, amount_deposit):
        self.amount_deposit = amount_deposit

    def withdraw(self, amount_withdraw):
        self.amount_withdraw = amount_withdraw

class User():
    def __init__(self, name, account_number, pin, balance):
        self.name = name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

# start a new tx
user1 = User("Jane Doe", 12345, 9999)
transaction1 = ATM(user1)

transaction1.current_user = user1

while transaction1.self.current_user == True:
    enter_pin = int(input("Please enter your PIN: "))
    if 
