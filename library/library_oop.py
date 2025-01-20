from typing import (
    ClassVar, Set, List, Optional ,
    Generator, Dict, Tuple, Any,
)
from functools import wraps
from pydantic import BaseModel, Field, field_validator, ValidationError

from errors import (
    BookAlreadyExists,
    UserAlreadyExists,
    BookDoesntExistsInLibrary,
    UserDoesntExistsInLibrary,
    BookNotAvailableException,
    BookAlreadyBorrowedException,
)

def get_cur_user_id() -> Generator[int, None, None]:
    start_id = 1
    while True:
        yield start_id
        start_id+=1



class Book(BaseModel):
    title: str = Field(min_length=3, max_length=128)
    author: str = Field(min_length=3, max_length=128)
    isbn: str = Field(..., description="unique key")
    is_available: bool = Field(..., description="description of available")

    book_set: ClassVar[Set] = set()

    @field_validator("isbn")
    def isbn_unique_validator(cls, value):
        if value in cls.book_set:
            raise BookAlreadyExists()
        cls.book_set.add(value)
        return value

    def __eq__(self, another) -> bool:
        if not isinstance(another, Book):
            raise ValueError("not book")
        return self.isbn == another.isbn

    def __hash__(self) -> int:
        return hash(self.isbn)
    
    def __setattr__(self, name, value):
        if name == "isbn" and hasattr(self, name):
            raise ValueError("book is immutable instance")
        return super().__setattr__(name, value)
    
    def __str__(self):
        return f"book {self.title} {self.author}"
    
    def __repr__(self):
        ans = "Book("
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):
                ans+=f"{attr}={value},"
        return (ans+')')
    
    # class Config:
    #     allow_mutation = True
    #     allow_hash = True
    #     frozen = False


class User(BaseModel):
    user_id: Optional[int] = Field(default=None, exclude=True)
    name: str = Field(...)
    borrowed_books: Set[Book] = Field(default_factory=set)

    user_id_set: ClassVar[Set] = set()
    _user_id_getter: ClassVar[Generator[int, None, None]] = get_cur_user_id()

    @staticmethod
    def generate_user_id() -> int:
        print(User._user_id_getter)
        value = next(User._user_id_getter)
        print(value)
        return value

    @field_validator('user_id')
    def validate_user_id(cls, value: Optional[int]) -> int:
        if value is None:
            print(value)
            value = cls.generate_user_id()  # Автоматическая генерация user_id
        if value in cls.user_id_set:
            raise ValueError(f"User ID {value} уже существует.")
        cls.user_id_set.add(value)
        return value

    @classmethod
    def from_dict(cls, user_dict: Dict[str, Any]):
        return cls(**user_dict)

    def __eq__(self, another):
        if not isinstance(another, User):
            raise ValueError("not user")
        return self.user_id == another.user_id

    def __hash__(self):
        return hash(self.user_id)
    
    def __setattr__(self, name, value):
        if name == "user_id" and hasattr(self, name):
            raise ValueError("user is immutable instance")
        return super().__setattr__(name, value)

    def __str__(self):
        return f"user {self.name}"
    
    def __repr__(self):
        ans = "User("
        for attr, value in self.__dict__.items():
            if not attr.startswith('_'):
                ans+=f"{attr}={value},"
        return (ans+')')

class Library(BaseModel):
    book_dict: Dict[str, Book] = Field(default_factory=dict)
    user_dict: Dict[int, User] = Field(default_factory=dict)
    users_taken_books: Dict[User, Set[Book]] = Field(default_factory=dict)

    def add_book(self, book: Book) -> None:
        self.book_dict[book.isbn] = book
    
    def register_user(self, user: User) -> None:
        self.user_dict[user.user_id] = user
        self.users_taken_books[user] = set()
    
    def validate_and_get_user_and_book(
        self, user_id: int, isbn: str
    ) -> Tuple[User, Book]:
        user = self.user_dict.get(user_id, None)
        if not user:
            raise UserDoesntExistsInLibrary()
        book = self.book_dict.get(isbn, None)
        if not book:
            raise BookDoesntExistsInLibrary()
        return (user, book)

    def borrow_book(self, user_id: int, isbn: str) -> None:
        (user, book) = self.validate_and_get_user_and_book(user_id, isbn)
        if not book.is_available:
            raise BookNotAvailableException()
        if book in self.users_taken_books[user]:
            raise BookAlreadyBorrowedException()
        book.is_available = False
        user.borrowed_books.add(book)    
        self.users_taken_books[user].add(book)
    
    def return_book(self, user_id: int, isbn: str) -> None:
        (user, book) = self.validate_and_get_user_and_book(user_id, isbn)
        if book.is_available:
            raise ValueError("cant return available book")
        book.is_available = True
        user.borrowed_books.remove(book)



# test_library.py

def main():
    library = Library()

    # Добавление книг
    try:
        book1 = Book(title="1984", author="Джордж Оруэлл", isbn="123-456-7890", is_available=True)
        library.add_book(book1)
        print(f"Добавлена книга: {book1}")

        book2 = Book(title="Преступление и наказание", author="Фёдор Достоевский", isbn="098-765-4321", is_available=True)
        library.add_book(book2)
        print(f"Добавлена книга: {book2}")

        # Попытка добавить книгу с уже существующим ISBN
        book3 = Book(title="Мастер и Маргарита", author="Михаил Булгаков", isbn="123-456-7890", is_available=True)
        library.add_book(book3)
    except BookAlreadyExists as e:
        print(f"Ошибка при добавлении книги: {e}")
    except ValidationError as e:
        print(f"Ошибка валидации при добавлении книги: {e}")

    # Регистрация пользователей
    try:
        user_data1 = {'user_id': None, 'name': 'Алексей Смирнов'}
        user1 = User.from_dict(user_data1)
        library.register_user(user1)
        print(f"Зарегистрирован пользователь: {user1.__repr__()}")

        user_data2 = {'user_id': None, 'name': 'Мария Иванова'}
        user2 = User.from_dict(user_data2)
        library.register_user(user2)
        print(f"Зарегистрирован пользователь: {user2.__repr__()}")

        # Попытка зарегистрировать пользователя с уже существующим user_id
        user_data3 = {'user_id': 1, 'name': 'Иван Петров'}
        user3 = User.from_dict(user_data3)
        library.register_user(user3)
    except UserAlreadyExists as e:
        print(f"Ошибка при регистрации пользователя: {e}")
    except ValidationError as e:
        print(f"Ошибка валидации при регистрации пользователя: {e}")

    # Выдача книги пользователю
    try:
        library.borrow_book(user_id=1, isbn='123-456-7890')
    except (BookNotAvailableException, UserDoesntExistsInLibrary, BookDoesntExistsInLibrary, BookAlreadyBorrowedException, ValueError) as e:
        print(f"Ошибка при выдаче книги: {e}")

    # Попытка повторной выдачи той же книги
    try:
        library.borrow_book(user_id=1, isbn='123-456-7890')
    except (BookNotAvailableException, UserDoesntExistsInLibrary, BookDoesntExistsInLibrary, BookAlreadyBorrowedException, ValueError) as e:
        print(f"Ошибка при выдаче книги: {e}")

    # Попытка выдать книгу несуществующему пользователю
    try:
        library.borrow_book(user_id=3, isbn='098-765-4321')
    except (BookNotAvailableException, UserDoesntExistsInLibrary, BookDoesntExistsInLibrary, BookAlreadyBorrowedException, ValueError) as e:
        print(f"Ошибка при выдаче книги: {e}")

    # Возврат книги
    try:
        library.return_book(user_id=1, isbn='123-456-7890')
    except (UserDoesntExistsInLibrary, BookDoesntExistsInLibrary, ValueError) as e:
        print(f"Ошибка при возврате книги: {e}")

    # Попытка вернуть доступную книгу
    try:
        library.return_book(user_id=1, isbn='123-456-7890')
    except (UserDoesntExistsInLibrary, BookDoesntExistsInLibrary, ValueError) as e:
        print(f"Ошибка при возврате книги: {e}")

    # Попытка вернуть книгу, которую пользователь не взял
    try:
        library.return_book(user_id=2, isbn='098-765-4321')
    except (UserDoesntExistsInLibrary, BookDoesntExistsInLibrary, ValueError) as e:
        print(f"Ошибка при возврате книги: {e}")

    # Вывод состояния библиотеки
    print("\nСостояние библиотеки:")
    print(library)

    # Вывод информации о пользователе
    print("\nИнформация о пользователе 1:")
    print(library.user_dict[user1.user_id])

    # Вывод информации о книге
    print("\nИнформация о книге '1984':")
    print(library.book_dict['123-456-7890'])

if __name__ == "__main__":
    main()
