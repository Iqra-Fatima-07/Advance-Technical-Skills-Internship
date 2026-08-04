# 1. Library Management System
# Suggested Classes: Book, Member, Library
# Features: Add/Search/Borrow/Return books, manage members
# OOP Concepts: Classes, Encapsulation, Composition, Inheritance


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_available = True   # Encapsulation

    def borrow(self):
        if self.__is_available:
            self.__is_available = False
            return True
        return False

    def return_book(self):

        self.__is_available = True

    def is_available(self):
        return self.__is_available


# Inheritance
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.__borrowed_books = []   # Encapsulation

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is not available.")

    def return_book(self, book):
        if book in self.__borrowed_books:
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print("You haven't borrowed this book.")


class Library:
    def __init__(self, name):

        self.name = name

        # Composition
        self.__books = []
        self.__members = []

    def add_book(self, book):
        self.__books.append(book)
        print(f"Added '{book.title}' to library.")

    def search_book(self, title):
        for book in self.__books:
            if book.title.lower() == title.lower():
                print(f"Found: {book.title} by {book.author}")
                return book

        print("Book not found.")
        return None

    def add_member(self, member):
        self.__members.append(member)
        print(f"Member {member.name} added.")

    def show_books(self):
        print("\nLibrary Books:")

        for book in self.__books:
            status = "Available" if book.is_available() else "Borrowed"
            print(f"{book.title} - {book.author} ({status})")


# Example Usage

library = Library("BITM Library")

# Create books
book1 = Book("Clean Code", "Robert Martin")
book2 = Book("Atomic Habits", "James Clear")

# Inherited class
ebook = EBook("Python Basics", "John Smith", "5 MB")

# Add books
library.add_book(book1)
library.add_book(book2)
library.add_book(ebook)

# Create member
member = Member("Iqra", 101)

# Add member
library.add_member(member)

# Show books
library.show_books()

# Search
book = library.search_book("Clean Code")

# Borrow
member.borrow_book(book)

# Show updated status
library.show_books()

# Return
member.return_book(book)

# Show final status
library.show_books()