# 13.	Loop Until Success
# •	Ask the user to enter an integer.
# •	If invalid, catch the exception and repeat the question until the input is valid.

while True:
    try:
        user_input = int(input("Enter a integer: "))
        print(f"Entered integer: {user_input}")
        break  # Exit the loop if input is valid
    except ValueError:

        print("Invalid input")
        