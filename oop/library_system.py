class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    # def __repr__(self):
    #     return f"Book: {self.title}, {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    # def __repr__(self):
    #     return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB)"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    # def __repr__(self):
    #     return f"PrintBook({self.title!r}, {self.author!r}, {self.page_count!r})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return

        for idx, book in enumerate(self.books, start=1):
            print(f"{book}")
