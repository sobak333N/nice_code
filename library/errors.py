
class BookAlreadyExists(Exception):
    """error while book already exists"""
    def __init__(self, message: str = "book with such ISBN already exists"):
        super().__init__(message)

class UserAlreadyExists(Exception):
    """error while user already exists"""
    def __init__(self, message: str = "user with such user_id already exists"):
        super().__init__(message)

class UserDoesntExistsInLibrary(Exception):
    """error while user already exists"""
    def __init__(self, message: str = "user with such user_id doesn't exists in registred users in library"):
        super().__init__(message)

class BookDoesntExistsInLibrary(Exception):
    """error while user already exists"""
    def __init__(self, message: str = "book with such ISBN doesn't exists in library books"):
        super().__init__(message)

class BookNotAvailableException(Exception):
    """error while user already exists"""
    def __init__(self, message: str = "book with such ISBN doesn't exists in library books"):
        super().__init__(message)

class BookAlreadyBorrowedException(Exception):
    """error while user already exists"""
    def __init__(self, message: str = "this user took this book"):
        super().__init__(message)