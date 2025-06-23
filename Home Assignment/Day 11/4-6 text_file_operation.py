# 4.	Write Multiple Lines
# o	Create a file bio.txt
# o	Write the following lines (each on a new line):
# Name: Ravi  
# Age: 22  
# Course: Python  
# 5.	Read Line by Line
# o	Read and print each line from bio.txt using a loop.
# 6.	Count Words, Lines, Characters
# o	From a file sample.txt, print:
# 	Total lines
# 	Total words
# 	Total characters

# 4
with open('Adi.txt', 'w') as file:
    file.write("Name: Ravi\n")
    file.write("Age: 22\n")
    file.write("Course: Python\n")

# 5
with open('Adi.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 6
def count_file_details(filename):

    with open(filename, 'r') as file:
        content = file.read()
        total_lines = content.count('\n') + 1  
        total_words = len(content.split())
        total_characters = len(content)

    return total_lines, total_words, total_characters


filename = 'sample.txt'
total_lines, total_words, total_characters = count_file_details(filename)
print(f"Total lines: {total_lines}")


print(f"Total words: {total_words}")
print(f"Total characters: {total_characters}")  
     