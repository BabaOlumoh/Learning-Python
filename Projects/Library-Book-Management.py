class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow_book(self, title):
        if self.title == a_book.title:
            print("Book is available")
        pass

    def return_book(self, title):
        pass

    def display_info(self):
        pass

a_book = Book("Things Fall Apart", "Chinua Achebe")

print(a_book.title)