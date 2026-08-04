#library Management System

class Book:
    def __init__(self, title, author, bookname, bookid, price):
        self.title = title
        self.author = author
        self.bookname = bookname
        self.bookid = bookid
        self.price = price

book1 = Book("python", "abc", "python programming", 1, 500)
book2 = Book("java", "xyz", "java programming", 2, 600)
book3 = Book("c++", "pqr", "c++ programming", 3, 700)

print(book1.title)
print(book2.author)
print(book3.bookname)
print(book1.bookid)
print(book2.price)

