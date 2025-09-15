class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} Deposit Accepted")

    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Insufficent balance")
        else: 
            self.balance -= amount
            print(f"{amount} Withdrawn")

    def __str__(self):
        return f"{self.owner} {self.balance}"

acct1 = Account('Jose',100)
print(acct1)
acct1.owner
acct1.balance
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)