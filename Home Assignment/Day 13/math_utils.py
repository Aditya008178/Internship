# 6.	Create a file math_utils.py with these functions:
# o	add(a, b) – returns the sum.
# o	multiply(a, b) – returns the product.
# o	is_even(n) – returns True if even.
# 8.	Modify math_utils.py:
# o	Add a greet() function that takes a name and returns a greeting.
# o	Import and test it in main.py.


def add(a, b):
    print(f"Additon of {a} and {b} is: {a + b}")

def multiply(a, b):
    print(f"Multiplication of {a} and {b} is: {a * b}")

def is_even(n):
    if n % 2 == 0:
        print(f"{n} is even")
        return True
def greet(name):
    print(f"Hello {name}, welcome to college. ")
    