# 4.	Math and File Operations Combined
# o	Ask user to input a number and a file name.
# o	Perform division 100 / number and open the given file.
# o	Catch ZeroDivisionError and FileNotFoundError in separate except blocks.

try:
    number = float(input("Please enter a number: "))
    result = 100 / number
    print(f"Result of division: {result}")

    file_name = input("Enter a file name: ")
    file_name = open(file_name, 'r')
    print("File opened successfully.")

except ZeroDivisionError :
    print("Cannot divide by zero")
except FileNotFoundError :
    print("File not found")

