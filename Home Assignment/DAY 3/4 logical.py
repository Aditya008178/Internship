# 4.	Create a login check:
# 	Ask for username and password
# 	If both match predefined values (e.g., "admin" and "1234"), print "Login successful"
# 	Else, print "Invalid credentials"

u_name = input("Enter username: ")
password = input("Enter password: ")

if u_name == "aditya" and password == "8968":
    print("Login Sucessfull")
else:
    print("Invalid credentials")