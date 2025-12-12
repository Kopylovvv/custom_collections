import random

from src.library import Library
from src.real_books import REAL_BOOKS
from src.models import Book


def test_add_book():
    random.seed(0)
    lib = Library()
    book = random.choice(REAL_BOOKS)
    before = len(lib.books)
    lib.add_book(book)
    after = len(lib.books)
    assert after == before + 1
    assert lib.books[0] == book


def test_remove_book():
    random.seed(0)
    lib = Library()
    book = random.choice(REAL_BOOKS)
    lib.add_book(book)
    assert lib.find_by_isbn(book.isbn) == book
    lib.remove_book(book)
    assert lib.find_by_isbn(book.isbn) != book
    assert len(lib.books) == 0


def test_remove_by_isbn():
    random.seed(0)
    lib = Library()
    book = random.choice(REAL_BOOKS)
    lib.add_book(book)
    removed = lib.remove_by_isbn(book.isbn)
    assert removed == book
    assert lib.find_by_isbn(book.isbn) != book
    assert len(lib.books) == 0


def test_remove_by_isbn_not_found():
    lib = Library()
    removed = lib.remove_by_isbn(1234567890123)
    assert removed is None
    assert len(lib.books) == 0


def test_find_by_author():
    random.seed(0)
    lib = Library()
    a = random.choice(REAL_BOOKS)
    b = random.choice(REAL_BOOKS)
    c = random.choice(REAL_BOOKS)
    lib.add_book(a)
    lib.add_book(b)
    lib.add_book(c)
    res = lib.find_by_author(a.author)
    assert any(book in res for book in (a, b, c))
    assert all(isinstance(x, Book) for x in res)


def test_find_by_year():
    random.seed(0)
    lib = Library()
    book = random.choice(REAL_BOOKS)
    lib.add_book(book)
    res = lib.find_by_year(book.year)
    assert book in res


def test_find_by_genre():
    random.seed(0)
    lib = Library()
    book = random.choice(REAL_BOOKS)
    lib.add_book(book)
    res = lib.find_by_genre(book.genre)
    assert book in res
