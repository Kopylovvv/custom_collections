import random
from time import sleep

import typer
import click_shell

from .library import Library
from .real_books import REAL_BOOKS
from .logger import logger

app = typer.Typer(help="CLI для работы с библиотекой и симуляцией.")
user_library = Library()


@app.callback(invoke_without_command=True)
def launch(ctx: typer.Context):
    shell = click_shell.make_click_shell(ctx, prompt="library> ")
    shell.cmdloop()


@app.command()
def add() -> None:
    """
    добавить случайную книгу в библиотеку из списка реальных книг
    """
    book = random.choice(REAL_BOOKS)
    user_library.add_book(book)
    logger.info(f"book {book.title} added")


@app.command()
def rm(isbn: int = typer.Argument(help="isbn по которому удаляется книга")) -> None:
    """
    удалить книгу из библиотеки по ее isbn
    """
    book = user_library.remove_by_isbn(isbn)
    if book:
        logger.info(f"book {book.title} removed")
    else:
        logger.info("there isn’t book with this isbn")


@app.command()
def ls() -> None:
    """
    обзор библиотеки
    """
    logger.info(f"{user_library}")


@app.command()
def find(
        param=typer.Argument(help="параметр поиска"),
        genre: bool = typer.Option(
            False,
            "--genre",
            "-g",
            help="поиск по жанру",
        ),
        year: bool = typer.Option(
            False,
            "--year",
            "-y",
            help="поиск по году",
        ),
        author: bool = typer.Option(
            False,
            "--author",
            "-a",
            help="поиск по автору",
        ),
) -> None:
    """
    поиск книги по isbn(по умолчанию), жанру, году или автору
    """
    if not any([genre, year, author]):
        book = user_library.find_by_isbn(int(param))
        logger.info(book)
    elif genre:
        books = user_library.find_by_genre(param)
        for book in books:
            logger.info(book)
    elif year:
        books = user_library.find_by_year(int(param))
        for book in books:
            logger.info(book)
    else:
        books = user_library.find_by_author(param)
        for book in books:
            logger.info(book)


@app.command()
def simulate(
        steps: int = typer.Option(20, help="Количество шагов симуляции."),
        seed: int | None = typer.Option(None, help="Seed"),
) -> None:
    """
    Запустить симуляцию библиотеки.
    """
    commands = ["add", "add", "remove", "find", "find_non-existent"]
    random.seed(seed)
    for i in range(steps):
        sleep(2)
        command = random.choice(commands)
        match command:
            case "add":
                logger.info("adding book")
                sleep(1)
                add()
            case "remove":
                if user_library.books:
                    book = random.choice(user_library.books)
                    logger.info(f"removing book by isbn {book.isbn}")
                    sleep(1)
                    rm(book.isbn)
                else:
                    logger.info("Cannot remove book from empty library")
            case "find":
                if user_library.books:
                    book = random.choice(user_library.books)
                    logger.info(f"searching the book by isbn {book.isbn}")
                    sleep(1)
                    logger.info(user_library.find_by_isbn(book.isbn))
                else:
                    logger.info("Cannot find book in empty library")
            case "find_non-existent":
                isbn = random.randint(1000000000000, 9999999999999)
                logger.info(f"searching the book by isbn {isbn}")
                sleep(1)
                logger.info(user_library.find_by_isbn(isbn))
