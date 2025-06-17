num1 = int(input("Enter number: "))

try:
    print(num1)

except ValueError:
    print("Cannot print string to integer")