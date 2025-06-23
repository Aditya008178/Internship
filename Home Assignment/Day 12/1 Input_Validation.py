# 1.	Basic Input Validation
# o	Ask the user to enter a float number.
# o	Catch ValueError and print "Invalid input. Please enter a decimal number."


try:
        user_input = input("Please enter a decimal number: ")
        float_value = float(user_input)
        print(f"Float value: {float_value}")
except ValueError:
        print("Invalid input. Please enter a decimal number.")
        