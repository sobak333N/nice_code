def fibonacci(n):
    first, second = 0, 1
    for i in range(n):
        yield first
        first, second = second, first+second

generator = fibonacci(100)
for g in generator:
    print(g)