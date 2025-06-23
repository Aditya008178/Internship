# 5.	Ask the user to enter a number, and keep asking until they enter a number greater than 100

while True:
        
        num = int(input("Enter a number greater than 100: "))
        if num > 100:
            print("You entered:", num)
        
        else:
            print("Number is not greater than 100")