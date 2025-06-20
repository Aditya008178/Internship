# 8.	Student Marks Entry
# o	Ask the user to enter a student’s mark (0–100).
# o	If out of range, raise ValueError.
# o	Catch the error and print "Invalid mark. Must be between 0 and 100."

try:
        mark = int(input("Enter the mark: "))
        if mark < 0 or mark > 100:
            raise ValueError("Invalid mark. Must be between 0 and 100.")
        print(f"Student's mark entered: {mark}")

except ValueError as e:
        print(e)
        print("Invalid mark. Must be between 0 and 100.")




