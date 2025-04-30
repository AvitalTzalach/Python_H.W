from book import Book
from library import Library
import pytest

def test_add_book():
    lib = Library();
    book = Book("Big Secret", "Natan Zomer");
    lib.add_book(book);
    assert book in lib.books;

def test_add_user():
    lib = Library();
    lib.add_user("David");
    assert "David" in lib.users;

def test_check_out_book():
    lib = Library();
    book = Book("Blueberry", "Bob");
    lib.add_book(book);
    lib.add_user("Bob");
    lib.check_out_book("Bob", "Blue");
    assert book.is_checked_out

def test_search_books_invalid():
    lib = Library();
    with pytest.raises(ValueError):
        lib.search_books("");


def test_search_books_exact_match(library):
    result = library.search_books("Python 101")
    assert len(result) == 1
    assert result[0].title == "Python 101"
