# 1.	Bank Account Simulation
# o	Create a class BankAccount:
# 	Attributes: account_number, account_holder, balance.
# 	Methods:
# 	deposit(amount)
# 	withdraw(amount) (check for insufficient balance)
# 	display() (prints account details)

class Bankaccount:
    def __init__(self,acc_holder):
        self.acc_holder = acc_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
         if amount > self.balance:
            print("Insufficient balance.")
         else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

            

       

    def display_balance(self):
        print("\n---- Account Details----")
        print(f"Account holder: {self.acc_holder}")
        print(f"Current balance: {self.balance}")

ac = input("Enter Name of Account holder: ")
d = int(input("Enter the Deposite amount: ")) 
w = int(input("Enter the Withdraw amount: "))


ba = Bankaccount(ac)
ba.deposit(d)
ba.withdraw(w)
ba.display_balance()

