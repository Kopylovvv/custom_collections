from typing import Iterable

from .collections import BookCollection, IndexDict
from .models import Book


class Library:
    """
    библиотека через которую идет управение всеми книгами
    доступные манипуляции над книгами:
        добавление книги
        удаление книги
        удаление книги по isbn
        поиск книг по автору, году, isbn и жанру
    """

    def __init__(self, books: Iterable[Book] | None = None) -> None:
        self.books = BookCollection()
        self.indexes = IndexDict()

        if books is not None:
            for book in books:
                self.add_book(book)

    def add_book(self, book: Book) -> None:
        self.books.add(book)
        self.indexes.add_book(book)

    def remove_book(self, book: Book) -> None:
        self.books.remove_book(book)
        self.indexes.remove_book(book)

    def remove_by_isbn(self, isbn: int) -> Book | None:
        """
        Удаление книги по isbn
        """
        book = self.indexes.remove(isbn)
        if book is None:
            return None
        self.books.remove_book(book)
        return book

    def find_by_isbn(self, isbn: int) -> Book | str:
        return self.indexes.find_by_isbn(isbn)

    def find_by_author(self, author: str) -> list[Book]:
        return self.indexes.find_by_author(author)

    def find_by_year(self, year: int) -> list[Book]:
        return self.indexes.find_by_year(year)

    def find_by_genre(self, genre: str):
        return self.indexes.find_by_genre(genre)

    def __repr__(self) -> str:
        lines: list[str] = [f"Библиотека: всего книг — {len(self.books)}.", f"{self.indexes}"]
        return "\n".join(lines)
