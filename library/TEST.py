from typing import Generator

def get_cur_user_id() -> Generator[int, None, None]:
    start_id = 1
    while True:
        yield start_id
        start_id+=1

gen = get_cur_user_id()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
