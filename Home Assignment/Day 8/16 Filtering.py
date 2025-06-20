# 16.	Set-Based Filtering
# o	Ask user to enter 5 numbers (some duplicates allowed)
# o	Store them in a list
# o	Use a set to display only unique numbers


list1 = []
print("Enter 5 numbers (some duplicates allowed) -")
for i in range(5):
    num = int(input(f"Enter Number {i + 1}: "))
    list1.append(num)
print("Orginal List: ",list1)
print("List after converting in Set (Unique numbers): ",set(list1))