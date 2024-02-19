class Book:
    """    Represents a book in a library catalog.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The International Standard Book Number (ISBN) of the book.
        is_checked_out (bool): Indicates whether the book is checked out (True) or available (False).

    Methods:
        __init__(self, title: str, author: str, isbn: str) -> None:
            Initializes a new Book instance with title, author, and ISBN. The book is set as not checked out by default.

        check_out(self) -> None:
            Marks the book as checked out.

        return_book(self) -> None:
            Marks the book as not checked out, making it available again.

        get_info(self) -> str:
            Returns a formatted string containing the book's title, author, and ISBN."""

    def __init__(self, title, author, isbn) -> None:
        self.title: str = title
        self.author: str = author
        self.isbn: str = isbn
        self.is_checked_out: bool = False

    def check_out(self) -> None:
        if not self.is_checked_out:
            print(f"Checking out book: {self.title}")
            self.is_checked_out = True
            return None
        print(f"Book already checked out.")
        return None

    def return_book(self) -> None:
        if self.is_checked_out:
            print(f"Returning book: {self.title}")
            self.is_checked_out = False
            return None
        print(f"This book was already returned.")

    def get_info(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"


class Library:
    """
    Represents a library, managing a collection of books (catalog).

    Attributes:
        name (str): The name of the library.
        catalog (list of Book): A list of Book objects representing the library's current catalog of books.

    Methods:
        __init__(self, name: str) -> None:
            Initializes a new Library instance with a name and an empty book catalog.

        add_book(self, book: Book) -> None:
            Adds a book to the library's catalog.

        find_book_by_isbn(self, isbn: str) -> Book | None:
            Searches for a book in the catalog by its ISBN and returns the Book object if found, otherwise returns None.

        remove_book(self, isbn: str) -> None:
            Removes a book from the catalog based on its ISBN. Prints a message indicating the outcome.

        list_books(self) -> None:
            Prints the details of all books currently in the catalog.

        check_out_book(self, isbn: str) -> None:
            Checks out a book by marking it as checked out, using its ISBN to find it in the catalog.

        return_book(self, isbn: str) -> None:
            Returns a book to the library by marking it as not checked out, using its ISBN to find it in the catalog.
    """

    def __init__(self, name: str) -> None:
        if name is None:
            name = input("Name the Library")
        self.name = name
        self.catalog = []

    def find_book_by_isbn(self, isbn: str) -> Book | None:
        """
        loops through the catalog and returns the book object that matches the isbn
        :param isbn: a string
        :return:
        """
        for book in self.catalog:
            if book.isbn == isbn:
                print(f"Book {book.title} found on catalog")
                return book

        print("book not found for this isbn")
        return None

    def add_book(self, book: Book) -> None:
        """Adds a book to the library by appending to the catalog list"""
        isbn = book.isbn
        existing_book = self.find_book_by_isbn(isbn)
        if existing_book is not None:
            raise ValueError(f"A book with the isbn {isbn} already exists in the catalog")

        self.catalog.append(book)
        print(f"Book {book.title} added to {self.name}'s catalog.")

    def remove_book(self, isbn: str) -> None:
        """
        Calls the find_book_by_isbn method and if receives a book, removes the book from the catalog list
        :param isbn: a string containing the isbn
        """
        book = self.find_book_by_isbn(isbn)
        if book:
            self.catalog.remove(book)
            print(f"{book.title} removed from {self.name}'s catalog")
            return None
        print("cannot remove this book. ISBN not found.")

    def list_books(self) -> None:
        for book in self.catalog:
            print(book.get_info())

    def check_out_book(self, isbn: str) -> None:
        book = self.find_book_by_isbn(isbn)
        if book:
            book.check_out()
            return None
        print("Book not found. Unable to Check out")
        return None

    def return_book(self, isbn: str) -> None:
        book = self.find_book_by_isbn(isbn)
        if book:
            book.return_book()
            return None
        print("Book not found. Unable to return")
        return None
