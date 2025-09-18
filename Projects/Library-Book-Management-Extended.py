class Book():
    def __init__(self, title, author, isbn, published_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.published_year = published_year
        self.is_available = True

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            return True
        return False
        

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            return True
        return False
        
    def __str__(self):
        availability = "Available" if self.is_available else "Borrowed"
        return f"{self.title} {self.author} {self.isbn} {self.published_year} - {availability}"
    
class Member():
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        
    def list_borrowed_books(self):
        if not self.borrowed_books:
            print(f"{self.name} has not borrowed any book")
        else:
            print(f"{self.name} has borrowed:")
            for book in self.borrowed_books:
                print(f"- {book.title} {book.isbn}")

    
    def __str__(self):
        return f"{self.name} {self.member_id}"


class Library():
    def __init__(self):
        self.book_storage = []
        self.members = []
        
    def add_book(self, book):
        self.book_storage.append(book)
        print(f"{book.title} - has been added to library")

    def remove_book(self, isbn):
        for book in self.book_storage:
            if book.is_available == True:
                if book.isbn == isbn:
                    self.book_storage.remove(book)
                    print(f"{isbn} - has been removed from library")
                    return True #To stop the loop
                else:
                    print(f"{isbn} doesn't exist")
            else:
                print(f"{book.title} has been borrowed")
                return False #To stop the loop

    def register_member(self, member):
        for new_member in self.members:
            if new_member.member_id == member.member_id:
                print(f"{member} is already registered")
                return False

        self.members.append(member)
        print(f"{member} is now a member of the library")
        return True
                 
        
    def find_book(self, isbn):
        for book in self.book_storage:
            if book.isbn == isbn:
                print(book)
                return True
        return f"{isbn} not found" 
                
    def lend_book(self,member_id, isbn):
        for book in self.book_storage:
            if book.isbn == isbn:
                if book.is_available == True:
                    for member in self.members:
                        if member.member_id == member_id:
                            print(f"{book.title} has been borrowed sucessfully")
                            member.borrowed_books.append(book)
                            book.is_available = False
                            return True
                    print(f"{member.id} is not a registered member")
                    return False
                else:
                    print(f"{book.title} has been borrowed")
                    return False
        print(f"{isbn} not found in library database")
        return
        
    def accept_return(self, member_id, isbn):
        for book in self.book_storage:
            if book.isbn == isbn:
                if book.is_available == False:
                    for member in self.members:
                        if member.member_id == member_id:
                            print(f"{book.title} has been returned sucessfully")
                            book.is_available = True
                            return True
                    print(f"{member_id} is not a registered member")
                    return False
                else:
                    print(f"{book.title} is currently not borrowed")
                    return False
        print(f"{isbn} not found in library database")
        return

    def list_books(self):
        for book in self.book_storage:
            print(book)
        
    def search(self, query):
        self.query = query.lower()
        self.results = []

        for book in self.book_storage:
            if query in book.title.lower or query in book.author.lower or query in book.isbn.lower or query in book.published_year.lower:
                self.results.append(book)

        for result in self.results:
            print(result)

my_lib = Library()

b3 = Book("Life", "Mamello", "123", "2025")
b1 = Book("Python Basics", "Alice", "1234", "2020")
b2 = Book("Advanced Python", "Bob", "456", "2021")

user1 = Member("Mamello", "M001")
user2 = Member("Vimbai", "M002")
user3 = Member("Mhlophe", "M003")

my_lib.book_storage = [b1, b2, b3]
my_lib.members = [user1, user2, user3]

my_lib.list_books()
my_lib.lend_book("M003", "123")
my_lib.accept_return("M001", "13")
my_lib.search("Mamello")
user1.list_borrowed_books()
