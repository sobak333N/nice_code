
def fibonacci(n: int, first: int=0, second: int=1):
    for _ in range(n):
        yield first
        first, second = second, first+second

def fibonacci_starts_with_index(n: int, start_index: int=0):
    first, second = 0, 1
    for _ in range(start_index):
        first, second = second, first+second
    for _ in range(n):
        yield first
        first, second = second, first+second


# for num in fibonacci(10, 1, 1):
#     print(num)

for num in fibonacci_starts_with_index(10, 6):
    print(num)