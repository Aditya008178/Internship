# 11.	Custom Calculator
# •	Take two numbers and an operator as input.
# •	Perform the calculation inside try.
# •	Handle:
# o	ZeroDivisionError
# o	ValueError for bad input
# o	Exception for invalid operators


try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operator = input("Enter an operator (+, -, *, /): ")

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2
        else:
            raise ValueError("Invalid operator. Please use +, -, *, or /.")

        print(f"The result of {num1} {operator} {num2} is: {result}")

except ZeroDivisionError as e:
        print(e)
except ValueError as e:
        print(e)
except Exception as e:
        print(f"unexpected error occurred: {e}")
