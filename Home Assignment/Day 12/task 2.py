# 2.	String to Integer Conversion
# o	Take a string input and try converting it to an integer.
# o	Catch exceptions and print the type of error using type(e).



user_input = input("Enter a string to convert to an integer: ")
try:
        
        result = int(user_input)
        print(f"Conversion successful: {result}")
except ValueError as e:
        print(f"An unexpected error occurred: {e}")
