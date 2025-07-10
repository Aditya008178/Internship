# 1.	BankAccount Class:
# o	Make balance a private attribute.
# o	Add deposit() and withdraw() methods.
# o	Prevent withdrawals if balance is insufficient.

class BankAccount:
    def __init__(self, __balance=0):
        self.__balance = __balance

    def deposit(self, amount):
            self.__balance += amount
            print(f"Amount Deposited. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw Successfull. Available Balance: {self.__balance}")
        else:
            print("Insufficient balance.")


ba = BankAccount()

d = int(input("Enter deposite amount: "))
ba.deposit(d)

w = int(input("Enter Withdraw amount: "))
ba.withdraw(w)
