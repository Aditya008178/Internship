# Replace Words with Frequencies
# Input: "cat dog cat rat dog cat"
# Output:"3 2 3 1 2 3"

simple = "cat dog cat rat dog cat"
words = simple.split()

result = [str(words.count(word)) for word in words]
frequency = " ".join(result) 
print(frequency)








