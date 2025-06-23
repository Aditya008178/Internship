# Task 4: Resource Lock Example
# Instructions:
# Create a lock = False.
# In the try, set lock = True.
# Simulate an error (e.g., 1 / 0).
# In finally, set lock = False and print "Lock released".
# (This is a real-world concept for releasing resources like files, DBs, etc.)

lock = False
try:
    lock = True
    print("Lock acquired")
    result = 1 / 0
    

except Exception as e:
    print("An error occurred:", e)

    
finally:
    lock = False
    print("Lock released")
    