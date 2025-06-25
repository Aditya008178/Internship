# Create a Book Class
# Attributes:
# title, author, year.
# Method:
# get_description() — Returns a formatted description like:
# "The book 'Title' by Author was published in Year."
# Test it: Create a book and print its description.

class Book:
    def __init__(self):
        self.title = input("Enter the title of  book: ")
        self.author = input("Enter the author name: ")
        self.year = int(input("Enter the year of book publication: "))

    def get_description(self):
        print(f"The book '{self.title}' by {self.author} was published in {self.year}.")


b = Book()
b.get_description()

        