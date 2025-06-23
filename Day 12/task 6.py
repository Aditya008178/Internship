# Dictionary and File Handling
# Instructions:
# Create a dictionary: prices = {"apple": 10, "banana": 5}
# Ask user for a fruit name and a filename.
# Try to print the price of the fruit and open the file.
# Catch KeyError and FileNotFoundError.

prices = {"apple": 10, "banana": 5}
try:
    fruit = input("Enter a fruit name: ")
    price = prices[fruit]
    file_name = input("Enter a file name: ")
    with open(file_name, "r") as file:
        content = file.read()
        print(f"The price  is: {price}")
        print("File content:-", content)
# except (KeyError , FileNotFoundError) as e:
#     print("file not found")
#     print("key not found")
    # print(e)

except KeyError as e:
    print("key not found",e)

except FileNotFoundError as e:
    print("File not found",e)



    