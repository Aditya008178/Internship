# 10.	Import the os module:
# o	List all files in the current directory.
# o	Get the current working directory.

import os

files_directory = os.listdir('.')
current_directory = os.getcwd()

print("Files in current directory: ", files_directory)
print("Current working directory: ",current_directory)