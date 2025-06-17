# Modifying Elements
# 6.	Replace the third element of a list marks = [45, 67, 89, 34] with 99.
# 7.	Add an element "python" at the end of a list languages = ["C", "Java"].
# 8.	Insert "HTML" at index 1 in the above list.
# 9.	Remove the last item using pop() and print it.
# 10.	Delete the second element using del.

marks=[45, 67, 89, 34]
marks[2]=99
print("Updated marks: ", marks) 

languages=["C","Java"]
languages.append("python")
print("After added element: ", languages)

languages.insert(1,"HTML")
print("After inserted: ", languages)

l_item = languages.pop()
print("Last pooped item")

