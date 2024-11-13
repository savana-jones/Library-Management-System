class Member:
    def __init__(self, name):
        self.name = name
#Observer pattern
    def update(self, book):
        print(f"{self.name} has been notified that {book.title} is available.")
