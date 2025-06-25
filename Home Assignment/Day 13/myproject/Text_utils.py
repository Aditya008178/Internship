def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    n_vowels = sum(1 for char in sentence if char in vowels)
    print("Number of Vowels: ", n_vowels)