from functools import wraps 
from typing import Callable


def cache(func: Callable):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # for arg in args:
        print(f"func_name = {func.__name__}")
        print(" ".join(list((map(str, args)))))
        for key, value in kwargs.items():
            print(f"{key} {value}")

        result = func(*args, **kwargs)
        print(result)    



    return wrapper




@cache
def foo(s: str, *args, **kwargs):
    # print(foo.__name__)
    return s

foo("x",2,"xui",[1,2,3],lox="gay")