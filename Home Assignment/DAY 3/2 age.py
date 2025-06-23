# 2.	Take age as input from the user and check if:
# 	The person is 18 or older
# 	The person is a senior citizen (>= 60)

age = int(input("Enter your age: "))

if age >= 18 and age <=60:
    print("you are 18 or older than 18")

elif age >= 60:
    print("You are senior citizen")

else:
    print("You are not 18")