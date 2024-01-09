class BankAccount:
    def __init__(self, account_holder_name, account_number, initial_balance=0):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nDeposited {amount}. Current balance is {self.balance}.")
        else:
            print("\nDeposit amount should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"\nWithdraw {amount}. Current balance is {self.balance}.")
            else:
                print("Insufficient funds!")
        else:
            print("\nWithdrawal amount should be greater than 0.")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")



account = BankAccount("Aditya Vinay", "123456789", 100000)
account.display_balance()
account.deposit(5000)
account.withdraw(20000) 

print("\nTo display Balance : **PRESS 1**")
n=int(input())
if(n==1):
    account.display_balance()
