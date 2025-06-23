# Ask the user to input a number and a file name.
# Divide 100 by the number.
# If successful, try to open the given file in read mode.
# Use try, except, and else to structure the code.

try:
    num = int(input("Enter a number: "))
    div = 100 / num
    file = input("Enter file name: ")
    file_n = open(file,"w")
    

# except(ZeroDivisionError , FileNotFoundError):
#     print("Exception occur due to wrong input")

except ZeroDivisionError:
    print("Cannot divide by zero")

except FileNotFoundError:
    print("File not found")

else:
    print(f"Division is: {div}")
    print("file opened successfully")
    # print(open(file,"r"))
    # file.close()
    