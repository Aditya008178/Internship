s = ("Aditya Vikram Wagh")
str_s = s.split()
print(str)

# keylength={word:len(word) for word in str_s}
# print(keylength)

keylength = {}
for word in str_s:
    keylength[word]=len(word)
print(keylength)






