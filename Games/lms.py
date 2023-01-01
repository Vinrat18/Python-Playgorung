
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from pydantic import BaseModel, Field


def book_id_generator(start: Optional[int] = 0) -> int:
    value = (start-1) if start > 0 else 0

    while True:
        value += 1
        yield value


book_id_generator_instance = book_id_generator()


@dataclass(frozen=True)
class Book:
    name: str
    id: int = field(init=False)
    is_borrowed: bool = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'id', next(book_id_generator_instance))
        object.__setattr__(self, 'is_borrowed', False)

    # @property
    # def is_borrowed(self) -> None:
    #     return self._is_borrowed

    # @is_borrowed.setter
    # def is_borrowed(self, v: bool) -> None:
    #     self._is_borrowed = v


@dataclass(frozen=False)
class User:
    name: str
    mobile: str
    id: int = field(init=False, repr=False)
    address: Optional[str] = None

    def __post_init__(self):
        if not self.mobile:
            raise ValueError("Missing Phone Number")

        object.__setattr__(self, 'id', next(book_id_generator_instance))


@dataclass(frozen=False)
class BorrowedBook:
    book: Book = field(default_factory=Book)
    user: User = field(default_factory=User)

    def __post_init__(self):
        if not self.book:
            raise ValueError("Missing Book")
        if not self.user:
            raise ValueError("Missing User")

        self.book.is_borrowed = True

    def return_book(self):
        self.book.is_borrowed = False

class Library(BaseModel):
    books: Optional[List[Book]] = Field(default_factory=list)
    me: Optional[List[User]] = Field(default_factory=list)

    borrowed_books: Dict[int, int] = Field(alias="_borrowed_books", default_factory=dict)

    def __init__(self) -> None:
        super().__init__()
        self.books = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def add_user(self, user: User) -> None:
        self.users.append(user)
    
    def lend_book(self, book: Book) -> None:
        self.borrowed_books.append(book)
    
    def return_book(self, book: Book) -> None:
        self.borrowed_books.append(book)


class LibraryMember(User):
    Library: 

if __name__ == '__main__':
    lib = Library()
