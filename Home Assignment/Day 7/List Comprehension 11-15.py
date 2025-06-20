# List Comprehension
# 11.	Create a list of squares from 1 to 10 using list comprehension.
# Example: [1, 4, 9, ..., 100]
# 12.	From a list of numbers 1 to 20, create a new list that contains only even numbers using list comprehension.
# 13.	Given words = ["Apple", "banana", "Cherry"], create a new list with all words in lowercase using list comprehension. (hint: use lower())
# 14.	From a string "python", create a list of characters using list comprehension.
# 15.	Create a list of numbers from 1 to 50 that are divisible by both 3 and 5 using list comprehension.


square_list = [i ** 2 for i in range(1, 10+1)]
print(f"List of squares from 1 to 10 : {square_list}")


for num in range(1, 21):
    even_numbers = [num for num in range(1, 21) if num % 2 == 0]   
print("Even Numbers List:", even_numbers)


words = ["Apple", "banana", "Cherry"]
lower_list = [word.lower() for word in words]
print(f"Lower Case List : {lower_list}")


string = "python"
characters = [char for char in string]
print(f"Character :{characters}")



divisible_list = [num for num in range(1, 50+1) if num % 3 == 0 and num % 5 == 0]
print("Divisible List :", divisible_list)