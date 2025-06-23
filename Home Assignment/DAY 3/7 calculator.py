a = input("Enter first number: ")
b = input("Enter second number: ")

a = float(a)
b = float(b)
operator = input("Enter operator (+, -, *, /): ")
if operator == '+':
    c = a + b
elif operator == '-':
    c = a - b
elif operator == '*':
    c = a * b
elif operator == '/':
    if b != 0:
        c = a / b
    else:
        c = "Error: Division by zero"
else:
    c = "Error: Invalid operator"
print(f"{a} {operator} {b} = {c}")