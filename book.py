# book.py
class Book:
    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def __str__(self):
        status = "Available" if self.is_available else "Not Available"
        return f"{self.title} by {self.author} ({status})"

