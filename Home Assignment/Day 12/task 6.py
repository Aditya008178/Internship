# 6.	Simulate Locking/Unlocking
# lock = False
# o	In try: set lock = True and simulate an error (e.g., 1 / 0)
# o	In finally: set lock = False and print "Resource released".

lock = False
try:
    lock = True
    print("Locking resource")
    
    result = 1 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
finally:

    lock = False
    print("Resource released")

