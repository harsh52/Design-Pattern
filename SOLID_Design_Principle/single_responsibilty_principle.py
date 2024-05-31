class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_books(self):
        return self.books


class Printer:
    @staticmethod
    def print_book_details(book):
        print(book.get_details())

    @staticmethod
    def print_all_books(books):
        for book in books:
            print(book.get_details())


if __name__ == "__main__":
    # Create some books
    book1 = Book("The Catcher in the Rye", "J.D. Salinger", "978-0316769488")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0061120084")

    # Create a library and add books to it
    library = Library()
    library.add_book(book1)
    library.add_book(book2)

    # Print book details using Printer class
    printer = Printer()
    printer.print_all_books(library.get_books())
