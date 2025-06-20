# 9.	Create a set from a list with repeated values:
# numbers = [1, 2, 2, 3, 4, 4, 5]
# o	Use set() to remove duplicates
# 10.	Use a loop to print all items in a set.

numbers = [1, 2, 2, 3, 4, 4, 5]
print(f"\nOriginal List: {numbers}") #Printing the original list
num_set = set(numbers) #Created a set from a list 
print(f"Removed Duplicates (list converted into set): {num_set}") #Removed the duplicates



print("All items of set :",end = " ")
for i in num_set:
    print(i,end = " ")