# 3.	Take two numbers and check:
# 	Which one is greater
# 	Whether they are equal

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))

if num1 > num2:
    print(f"{num1} is greater")
elif num2 > num1:
    print(f"{num2} is greater")
else:
    print(f"{num1} is equal to {num2}")