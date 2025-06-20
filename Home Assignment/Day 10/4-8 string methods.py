# 4.	split() Method
# Input: "apple,banana,cherry"
# o	Split the string by comma and print the list.
# 5.	join() Method
# Given a list: ["red", "green", "blue"]
# o	Join the list using - as separator: "red-green-blue"
# 6.	replace() Method
# Input: "The sky is blue"
# o	Replace "blue" with "clear"
# 7.	lower() and upper()
# o	Convert "Python Is FUN" to all lowercase and all uppercase.
# 8.	count() and find()
# For the string "banana":
# o	Count how many times "a" appears
# o	Find the first occurrence of "n"

#4
input = "apple,banana,cherry"
split = input.split()
print("Splitted List : ", split)

#5
color = ["red", "green", "blue"]
joined_list = "-".join(color)
print("\nJoined List : ",joined_list)

#6
input = "The sky is blue"
print("\nReplaced string :", input.replace("blue", "clear"))

#7
string = "Python Is FUN"
print("\nLowercase :", string.lower())
print("Uppercase :", string.upper())

#8
fruit = "banana"
print("\nCount of \"a\" :", fruit.count("a"))
print("First occurrence of \"n\" :",fruit.find("n"))
