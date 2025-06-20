# 12.	ATM Simulator
# •	Initial balance = 5000
# •	Ask user to withdraw an amount.
# •	If amount > balance, raise an exception with message "Insufficient balance".
# •	Always print "Transaction ended" in finally.

initial_balance = 5000
try:
    amount = int(input("Enter amount to withdraw: "))
    
    if amount > initial_balance:
        raise Exception("Insufficient balance")
    
    initial_balance -= amount
    print("Withdrawal successful.")

except Exception as e:
    print(f"Error: {e}")
finally:

   # print("Transaction completed")
    print(f"Final balance: {initial_balance}")