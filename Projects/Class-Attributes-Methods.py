class BankAccount():
    #Attributes
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    #Methods
    def deposit(self, amount):
        self.balance += amount
        print(f"Your new balance is {self.balance}")
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficent balance")
        else:
            self.balance = self.balance - amount
            print(f"You've withdrawn {amount} and your balance is {self.balance}")
            return self.balance
        
    
    def check_balance(self):
        current_balance = self.balance
        print(f"Your account balance is {current_balance}")
        return current_balance


bank_account = BankAccount("Mamello")

while True:
    print("Welcome to your account!")
    print("Enter 1 to Deposit: ")
    print("Enter 2 to Withdraw: ")
    print("Enter 3 to Check Balance: ")
    print("Enter 4 to Quit: ")

    user_choice = int(input("Enter a value between 1-4: "))
    if user_choice == 1:
        user_deposit = int(input("Enter deposit amount: "))
        bank_account.deposit(user_deposit)
    elif user_choice == 2:
        user_withdraw = int(input("Enter withdrawal amount: "))
        bank_account.withdraw(user_withdraw)
    elif user_choice == 3:
        bank_account.check_balance()
    elif user_choice == 4:
        print("Thank you for banking with us!!!")
        break

