# 4.	Count Words in a Sentence
# Function count_words(sentence) returns total number of words in the input.

def count_word():
    count = 0
    sentence = "He said that is his favorite book, and he agreed that is a great choice"
    for word in sentence.split(): 
        if word=="is" :
            count += 1
    print(f" is appears {count} times")
count_word()