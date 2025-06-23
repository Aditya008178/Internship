# 18.Given sentence = "Python is powerful", convert it into a list of words and then reverse the list using slicing

sentence = "Python is powerful"
words=sentence.split()
print(f"List of Words: {words}")
reversed_words = words[::-1]
print(f"Reversed List: {reversed_words}")