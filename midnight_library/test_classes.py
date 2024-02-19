from classes import Book, Library
import pytest


# Testing for Book class:
# Methods: init, checkout, return_book, get info

# 1
def test_book_init():
    book = Book("Dom Casmurro", "Machado de Assis", "859431860X")
    assert book.title == "Dom Casmurro"
    assert book.author == "Machado de Assis"
    assert book.isbn == "859431860X"
    assert book.is_checked_out == False


# 2
def test_book_checkout():
    book = Book("Dom Casmurro", "Machado de Assis", "859431860X")
    book.check_out()
    assert book.is_checked_out == True


# 3
def test_book_return():
    book = Book("Dom Casmurro", "Machado de Assis", "859431860X")
    book.check_out()
    book.return_book()
    assert book.is_checked_out == False


# 4
def test_book_get_info():
    book = Book("Foudation", "Isaac Asimov", "0553293354")
    info = book.get_info()
    assert info == "Title: Foudation, Author: Isaac Asimov, ISBN: 0553293354"


# Test for Library
# not a test, just setting up objects.
def setup_function(function):
    """Setup for tests with a library instance and a book."""
    global library, book
    library = Library("Test Library")
    book = Book("Test Title", "Test Author", "123456789")
    library.add_book(book)


# 5
def test_add_book():
    # Assuming setup_function has run, there should be one book in the catalog
    assert len(library.catalog) == 1
    assert library.catalog[0].isbn == "123456789"


# 6
def test_find_book_by_isbn():
    found_book = library.find_book_by_isbn("123456789")
    assert found_book is not None
    assert found_book.title == "Test Title"


# 7
def test_remove_book():
    library.remove_book("123456789")
    assert len(library.catalog) == 0


# 8
def test_check_out_book():
    library.check_out_book("123456789")
    assert book.is_checked_out == True


# 9
def test_return_book():
    library.check_out_book("123456789")  # First, check out the book
    library.return_book("123456789")  # Then return it
    assert book.is_checked_out == False


# Error Tests
# 10
def test_add_duplicate_isbn_book():
    with pytest.raises(ValueError):
        duplicate_book = Book("Test Title", "Test Author", "123456789")
        library.add_book(duplicate_book)


# 12
def test_remove_nonexistent_book():
    library.remove_book("nonexistent ISBN")
