# 5.	Nested Try Blocks
# o	In outer try: convert user input to integer.
# o	In inner try: divide a fixed number by the input.
# o	Catch errors in appropriate places and explain with print statements.

try:
    user_input = input("Enter an integer: ")
    number = int(user_input)  
    print(f"Entered number: {number}")

    try:
        result = 100 / number  
        print(f"Division: {result}")

    except ZeroDivisionError:
        print("Cannot divide by zero")

except  ValueError as e:
    print("Invalid input")
