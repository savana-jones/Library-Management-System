class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookFactory:
    @staticmethod
    def create_book(title, author):
        return Book(title, author)

# Decorator Pattern to add attributes to books
class BookDecorator(Book):
    def __init__(self, book):
        self.book = book
        super().__init__(self.book.title, self.book.author)

class NewArrival(BookDecorator):
    def __str__(self):
        return f"{self.book.title} by {self.book.author} - New Arrival"
