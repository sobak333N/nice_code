def cumulative_sum():
    total = 0
    while True:
        num = (yield total)
        if num is None:
            break
        total+=num




generator = cumulative_sum()
print(next(generator))
print(generator.send(2))
print(generator.send(3))
print(generator.send(4))
