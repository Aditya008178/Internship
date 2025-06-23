a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
try:
    c=a/b
    print(f"Division is: {c}")
except ZeroDivisionError:
    print("cannot divide by zero")
