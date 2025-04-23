# library.py
import json
from book import Book

class Library:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = self.load_books()

    def save_books(self):
        with open(self.filename, "w") as f:
            json.dump([book.__dict__ for book in self.books], f)

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                book_data = json.load(f)
                return [Book(**data) for data in book_data]
        except FileNotFoundError:
            return []

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        self.save_books()
        print(f"✅ '{title}' added to library.")
    def display_books(self):
        if not self.books:
            print("📚 Library is empty.")
        else:
            for idx, book in enumerate(self.books):
                print(f"{idx + 1}. {book}")

    def delete_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print(f"❌ '{book.title}' removed from the library.")
                return
        print("❌ Book not found.")

    def lend_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                book.is_available = False
                self.save_books()
                print(f"📕 You borrowed '{book.title}'.")
                return
        print("❌ Book not available or doesn't exist.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                book.is_available = True
                self.save_books()
                print(f"📗 You returned '{book.title}'.")
                return
        print("❌ Book not found or already returned.")
