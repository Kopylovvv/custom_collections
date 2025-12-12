from typing import Iterable, Iterator

from .models import Book


class BookCollection:
    """
    Пользовательская списковая коллекция книг.
    """

    def __init__(self, books: Iterable[Book] | None = None) -> None:
        self._books: list[Book] = []
        if books is not None:
            self._books.extend(list(books))

    def __iter__(self) -> Iterator[Book]:
        for book in self._books:
            yield book

    def __len__(self) -> int:
        return len(self._books)

    def __getitem__(self, item):
        result = self._books[item]
        if isinstance(item, slice):
            return BookCollection(result)
        return result

    def __contains__(self, book: Book) -> bool:
        return book in self._books

    def __repr__(self) -> str:
        if not self._books:
            return ""
        lines = []
        for book in self._books:
            lines.append(f"- {book}")
        return "\n".join(lines)

    def add(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, book: Book) -> None:
        self._books.remove(book)


class IndexDict:
    """
    Пользовательская словарная коллекция индексов:
    isbn -> Book
    author -> list[Book]
    year -> list[Book]
    genre -> list[Book]
    """

    def __init__(self) -> None:
        self._by_isbn: dict[int, Book] = {}
        self._by_author: dict[str, list[Book]] = {}
        self._by_year: dict[int, list[Book]] = {}
        self._by_genre: dict[str, list[Book]] = {}

    def __len__(self) -> int:
        return len(self._by_isbn)

    def __iter__(self):
        for author, books in self._by_author.items():
            yield author, list(books)

    def __getitem__(self, key):
        if isinstance(key, int):
            if key in self._by_isbn:
                return self._by_isbn[key]
            return list(self._by_year.get(key, []))
        if isinstance(key, str):
            if key in self._by_author:
                return list(self._by_author.get(key, []))
            return list(self._by_genre.get(key, []))
        raise KeyError(f"Unsupported key type: {type(key)}")

    def __contains__(self, isbn: str) -> bool:
        return isbn in self._by_isbn

    def __repr__(self) -> str:
        if not self._by_author:
            return ""
        lines: list[str] = []
        for author, books in self._by_author.items():
            lines.append(f"{author}:")
            for book in books:
                lines.append(f"\t- {book}")
        return "\n".join(lines)

    def add_book(self, book: Book) -> None:
        self._by_isbn[book.isbn] = book
        self._by_author.setdefault(book.author, []).append(book)
        self._by_year.setdefault(book.year, []).append(book)
        self._by_genre.setdefault(book.genre, []).append(book)

    def remove_book(self, book: Book) -> None:
        self._by_isbn.pop(book.isbn, None)

        if book.author in self._by_author:
            author_list = self._by_author[book.author]
            if book in author_list:
                author_list.remove(book)
            if not author_list:
                self._by_author.pop(book.author, None)

        if book.year in self._by_year:
            year_list = self._by_year[book.year]
            if book in year_list:
                year_list.remove(book)
            if not year_list:
                self._by_year.pop(book.year, None)

        if book.genre in self._by_genre:
            genre_list = self._by_genre[book.genre]
            if book in genre_list:
                genre_list.remove(book)
            if not genre_list:
                self._by_genre.pop(book.genre, None)

    def remove(self, isbn: int) -> Book | None:
        book = self._by_isbn.get(isbn)
        if book is None:
            return None
        self.remove_book(book)
        return book

    def find_by_isbn(self, isbn: int) -> Book | str:
        res = self._by_isbn.get(isbn)
        if res is not None:
            return res
        return "Cannot find book by this isbn"

    def find_by_author(self, author: str) -> list[Book]:
        return list(self._by_author.get(author, []))

    def find_by_year(self, year: int) -> list[Book]:
        return list(self._by_year.get(year, []))

    def find_by_genre(self, genre: str) -> list[Book]:
        return list(self._by_genre.get(genre, []))
