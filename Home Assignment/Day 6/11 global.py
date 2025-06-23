# 11.	Local vs Global Debugging
# Create a global variable x = 50
# •	Define function that modifies x locally
# •	Define another that uses global x
# •	Print x before and after both functions


x = 50

def changes_local():
    x = 100  
    print("Inside changes local, x =", x)

def changes_global():
    global x     
    x = 200
    print("Inside changes global, x =", x)


print(f"Before functions, x = {x}")

changes_local()   
print(f"After Changes_local, x = {x}")

changes_global()  
print(f"After Changes_global, x = {x}")
