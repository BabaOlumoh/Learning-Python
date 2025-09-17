class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library():
    def __init__(self):
        self.book_storage = []

    def add_book(self, book):
        self.book_storage.append(book)

    def show_all_books(self):
        for book in self.book_storage:
            print(book)

    def borrow_book(self, title):
        for book in self.book_storage:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"You've borrowed {book.title}")
                else:
                    print(f"Book has been borrowed")
                return
            print("Book doesn't exist in this library")
                

    def return_book(self, title):
        for book in self.book_storage:
            if book.title == title:
                if book.is_available:
                    print(f"{book.title} is already in storage")
                else:
                    book.is_available = True
                    print(f"You've returned {book.title}")
                return
        print("Book doesn't exist in this library")

my_lib = Library()

tfa = Book("Things Fall Apart", "Chinua Achebe")
hp = Book("Harry Potter", "J.K. Rowling")
tslobsw =  Book("The Secret Lives Baba Segi's Wives", "Wole Soyinka")

my_lib.add_book(tfa)
my_lib.add_book(hp)
my_lib.add_book(tslobsw)

my_lib.borrow_book("Things Fall Apart")
my_lib.return_book("Harry Potter")