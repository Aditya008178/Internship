# 6.	Create a small bill calculator:
# 	Input: item name, quantity, price per item
#     Output: total cost = quantity × price

item_name = input("Enter a Product name : ")
quantity = int(input("Enter the Quantity of product : "))
price = float(input("Enter a price of product : "))

print(f"\nTotal cost of {quantity} {item_name} is ₹{quantity * price}")