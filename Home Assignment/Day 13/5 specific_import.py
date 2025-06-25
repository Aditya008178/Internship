# 5.	From the random module:
# o	Import only the choice function and use it to pick a random element from a list of names.

 
from random import choice

names = ["Aditya", "Piyush", "Prasad", "Sumedh", "Jayesh", "Shubham"]
r_name = choice(names)
print("Random selected name: ", r_name)