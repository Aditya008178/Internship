# 2.	Inventory Item
# o	Create a class Item:
# 	Attributes: name, price, quantity.
# 	Methods:
# 	add_stock(amount) – Increase quantity.
# 	sell_stock(amount) – Decrease quantity if available.
# 	get_total_value() – Returns total value of stock (price * quantity).

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_stock(self, amount):
        self.quantity += amount
        print(f"Added {amount} {self.name}(s) to stock. New quantity is {self.quantity}.")

    def sell_stock(self, amount):
        if amount > self.quantity:
            print(f"Insufficient stock. Only {self.quantity} {self.name}(s) available.")
        else:
            self.quantity -= amount
            print(f"Sold {amount} {self.name}(s). New quantity is {self.quantity}.")

    def get_total_value(self):
         t= self.price * self.quantity
         print(t)

    def display(self):
        print(f"\n---- {self.name} Details ----")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Value: {self.get_total_value()}")

name = input("Enter Item Name: ")
price = float(input("Enter Item Price: "))
quantity = int(input("Enter Initial Quantity: "))

item = Item(name, price, quantity)

        
