from functools import wraps
from typing import List, Tuple, Callable
from random import randint


def tuple_exceptions(exceptions: List[Tuple[Exception, Callable[[],None]]]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            
            try:
                result = func(*args, **kwargs)
            except Exception as local_exception:
                for exception in exceptions:
                    if isinstance(local_exception, exception[0]):
                        exception[1]()
            return None

        return wrapper
    
    return decorator


def index_func():
    print("index_func")

def key_func():
    print("key_func")


@tuple_exceptions([(IndexError, index_func), (KeyError, key_func)])
def func():
    if randint(1,2) == 1:
        raise KeyError("bar")
    else:
        raise IndexError
    ...


func()
print(func.__name__)