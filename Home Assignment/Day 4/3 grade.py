# Part B: If-Elif-Else
# 3.	Ask the user to enter marks (0–100) and display grade:
# o	90–100: Grade A
# o	75–89: Grade B
# o	50–74: Grade C
# o	Below 50: Fail

marks = int(input("Enter your marks (0–100): "))

if marks >= 90 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks < 90:
    print("Grade B")
elif marks >= 50 and marks < 75:
    print("Grade C")
elif marks >= 0 and marks < 50:
    print("Fail")
else:
    print("Invalid marks .")