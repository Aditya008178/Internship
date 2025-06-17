# Multiple Except Blocks
# Input: take a number and a file name.
# Divide 100 by the number and open the file.
# Catch both ZeroDivisionError and FileNotFoundError.

num = int(input("Enter a number: "))
file = input("Enter file name: ")

try:
    div = 100 / num
    file_n = open(file,"r")
    print(f"Division is: {div}")

# except(ZeroDivisionError , FileNotFoundError):
#     print("Exception occur due to wrong input")

except ZeroDivisionError:
    print("Cannot divide by zero")

except FileNotFoundError:
    print("file not found")


