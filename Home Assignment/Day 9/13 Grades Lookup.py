# 13.	Grades Lookup
# •	Create a dictionary where keys are roll numbers and values are student names.
# •	Ask user for a roll number and print the corresponding name.

student = {59 : "Aditya", 57 : "Swapnil", 31 : "Piyush", 47 : "Dhiraj", 58 : "Shubham", 13 : "Gurule"}

roll_number = int(input("For which roll number are you looking for? : "))
print(f"Name of roll no.: {roll_number} is {student[roll_number]}")