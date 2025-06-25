# 9.	Online Shopping Cart Simulation
# o	Create a class Cart:
# 	Attribute: items (dictionary with item_name: price).
# 	Methods:
# 	add_item(name, price)
# 	remove_item(name)
# 	get_total()
# 	display()

class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price
        print(f"Item '{name}' added to cart.")

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            print(f"Item '{name}' removed from cart.")
        else:
            print(f"Item '{name}' not found in cart.")

    def get_total(self):
        print(sum(self.items.values()))

    def display(self):
        print("\n---- Shopping Cart ----")
        for item, price in self.items.items():
            print(f"{item}: {price:.2f}")
        print(f"Total: {self.get_total():.2f}")

# Create a cart object
c = Cart()

c.add_item("Apple", 1.00)
c.add_item("Banana", 0.50)
c.add_item("Orange", 1.50)
c.display()
c.remove_item("Banana")
c.display()
