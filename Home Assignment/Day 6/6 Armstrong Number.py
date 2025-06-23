# 6.	Armstrong Number Checker
# Function is_armstrong(n) returns True if number is an Armstrong number.

n = int(input("Enter number: "))

def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    return n == sum

print(is_armstrong(n))