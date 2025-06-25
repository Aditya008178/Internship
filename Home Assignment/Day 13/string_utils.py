# 13.	Create a string_utils.py:
# o	count_characters(s) → returns character count.
# o	count_words(s) → returns word count.
# o	reverse_string(s) → returns the reversed version.
# o	Import and test these in main.py.(main3.py)

def count_characters(sentence):
    print("Character count: ", len(sentence))

def count_words(sentence):
    words = sentence.split()
    print("Word count: ", len(words))

def reverse_string(sentence):
    r_string = sentence[::-1]
    print("Reversed string: ",r_string)