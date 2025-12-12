from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    year: int
    genre: str
    isbn: int

    def __repr__(self) -> str:
        return f"«{self.title}» — {self.author}, {self.year} год, жанр: {self.genre}, ISBN: {self.isbn}"
