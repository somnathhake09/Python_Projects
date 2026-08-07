class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Issued"
        print(f"Title: {self.title} | Author: {self.author} | ISBN: {self.isbn} | Status: {status}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to library successfully!")

    def display_books(self):
        if len(self.books) == 0:
            print("No books in library.")
            return
        print("\n--- Library Books ---")
        for book in self.books:
            book.display_info()

    def search_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def issue_book(self, isbn):
        book = self.search_book(isbn)
        if book is None:
            print("Book not found!")
        elif not book.is_available:
            print(f"Sorry, '{book.title}' is already issued.")
        else:
            book.is_available = False
            print(f"You have issued '{book.title}'. Enjoy reading!")

    def return_book(self, isbn):
        book = self.search_book(isbn)
        if book is None:
            print("Book not found!")
        elif book.is_available:
            print("This book was not issued.")
        else:
            book.is_available = True
            print(f"Thank you for returning '{book.title}'.")


# ---------- Main Program ----------
library = Library()

library.add_book(Book("Python Basics", "John Doe", "101"))
library.add_book(Book("MySQL", "Jane Smith", "102"))
library.add_book(Book("Artificial Intelligence", "Andrew Ng", "103"))

while True:
    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        isbn = input("Enter ISBN: ")
        library.add_book(Book(title, author, isbn))

    elif choice == '2':
        library.display_books()

    elif choice == '3':
        isbn = input("Enter ISBN of book to issue: ")
        library.issue_book(isbn)

    elif choice == '4':
        isbn = input("Enter ISBN of book to return: ")
        library.return_book(isbn)

    elif choice == '5':
        print("Thank you for using Library System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")