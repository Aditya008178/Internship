
# Part C: Nested If
# 5.	Take a number as input. Check if it is:
# o	Positive
# 	If yes, also check whether it is greater than 100 or not
# o	Negative
# o	Zero
# Example Output:
# Number is positive and greater than 100

number = float(input("Enter a number: "))

if number > 0:
    print("Number is positive")
    if number > 100:
        print("and greater than 100")
    else:
        print("and not greater than 100")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")
