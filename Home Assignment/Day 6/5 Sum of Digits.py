# 5.	Sum of Digits
# Function sum_of_digits(n) returns the sum of all digits in a number.
# Example: 123 → 6

n = 456
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

    

print(sum_of_digits(n))