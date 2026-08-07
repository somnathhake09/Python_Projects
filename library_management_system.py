class Book:
    def __init__(self, book_id,title,author):
        self.book_id = book_id
        self.title =title
        self.author =author
        self.is_issued = False

    def display_info(self):
        status = "Issued" if self.is_issued else "Available"
        print(f"[{self.book_id}] {self.title} by {self.author} - {status}")

class Library:
    def __init__(self):
        self.books = []   # sarv books ithe list madhe store hotil

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in library.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            book.display_info()   # Book class chi method call keli

    def search_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None