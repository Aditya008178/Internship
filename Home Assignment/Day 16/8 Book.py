# 8.	Library Book Tracker
# o	Create a class Book:
# 	Attributes:
# 	title, author, copies_available.
# 	Methods:
# 	issue() – Decrease copies if available.
# 	return_book() – Increase copies.
# 	status() – Shows book status.


class Book:
    def __init__(self, title, author, c_available):
        self.title = title
        self.author = author
        self.c_available = c_available

    def issue(self):
        if self.c_available > 0:
            self.c_available -= 1
            print(f"Book '{self.title}' issued. Copies available: {self.c_available}")
        else:
            print(f"Book '{self.title}' is not available.")

    def return_book(self):
        self.c_available += 1
        print(f"Book {self.title} returned. Copies available: {self.c_available}")

    def status(self):
        print(f"\n---- Book Status ----")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies Available: {self.c_available}")


book1 = Book("Agni pankh", "Dr A.P.J Kalam", 5)

book1.status()
book1.issue()
book1.return_book()
book1.status()

