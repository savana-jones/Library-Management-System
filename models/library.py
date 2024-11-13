class Library:
    _instance = None

    def __init__(self):
        if Library._instance is not None:
            raise Exception("This class is a singleton!")
        self.books = []
        self.observers = []

    @staticmethod
    def get_instance():
        if Library._instance is None:
            Library._instance = Library()
        return Library._instance

    def add_book(self, book):
        self.books.append(book)
        self.notify_observers(book)

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, book):
        for observer in self.observers:
            observer.update(book)
