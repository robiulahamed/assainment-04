class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books_by_title(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}")


book1 = Book("2000", "tajuddin ahamed")
book2 = Book("soisober dinguli", "kaji nazrul islam")

library = Library()
library.add_book(book1)
library.add_book(book2)

library.display_books_by_title()
