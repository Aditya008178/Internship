# 3.	Product Class:
# o	Make price private.
# o	Use a method to apply discount (without direct access).


class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        print("Price: ",self.__price)

    def apply_discount(self, discount):
        discount_amount = (discount / 100) * self.__price
        self.__price -= discount_amount
        print(f"Discount applied: {discount}%")

    def display_product(self):
        print(f"Product Name: {self.name}")
        print(f"Price: {self.__price}")

product = Product("Laptop", 1000)
product.display_product()

product.apply_discount(10)
product.display_product()
