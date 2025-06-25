# 16.	Create a text_utils.py:
# o	Functions:
# 	count_vowels(sentence)
# 	count_consonants(sentence)
# o	Import and test both.(main6.py)

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    n_vowels = sum(1 for char in sentence if char in vowels)
    print("Number of Vowels: ", n_vowels)

def count_consonants(sentence):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    n_consonants = sum(1 for char in sentence if char in consonants)
    print("Number of Consonants: ", n_consonants)