#  Part D: Real-World Scenarios
# 6.	Ask for a username and password:
# o	If both are correct → "Login successful"
# o	If username is correct but password is wrong → "Wrong password"
# o	If username is wrong → "User not found"


username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "1001":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("User not found")

       