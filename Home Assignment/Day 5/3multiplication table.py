# 3.	Print the multiplication table of a number (user input).

num=int(input("Enter any number: "))
for i in range(1,11,1):
    print(f"{num}*{i}={num*i}")
    