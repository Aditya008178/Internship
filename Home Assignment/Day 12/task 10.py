# 10.	Simple File Reader with Fallback
# o	Ask user for a file name.
# o	If file doesn’t exist, catch FileNotFoundError and create a new file with default content.
# o	Print "New file created."

try:
    file_name = input("Enter file name: ")
    file = open(file_name, 'r')
    print(f"File '{file_name}' opened successfully.")
    
except FileNotFoundError:
    print("File not found, Creating a new file.")
    with open(file_name, 'w') as file:
        file.write("This is the default file.")
    print("New file created.")

except Exception as e:
    
    print(f"An unexpected error occurred: {e}")
    
finally:
    print("File operation completed.")
