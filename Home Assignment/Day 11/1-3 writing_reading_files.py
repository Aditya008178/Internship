# 1.	Write a Greeting
# o	Create a file called greeting.txt
# o	Write "Hello, welcome to Python file handling!" into it.
# 2.	Read File Content
# o	Open greeting.txt and print the content.
# 3.	Append More Text
# o	Append "This is the second line." to greeting.txt
# o	Then read and print the updated content.

# 1
with open('greeting.txt', 'w') as file:
    file.write("Hello, welcome to Python file handling!")


#2
with open('greeting.txt', 'r') as file:
    content = file.read()
    print(content)


# 3
with open('greeting.txt', 'a') as file:
    file.write("\nThis is the second line.")

# Read the updated content
with open('greeting.txt', 'r') as file:
    updated_content = file.read()
    print(updated_content)
