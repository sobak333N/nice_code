
data = [ [1, 2, 3], [4, 5, 6] ]

linear_data = [el for row in data for el in row]


Примеры
1. Простой генератор с for

[x * 2 for x in range(5)]
# [0, 2, 4, 6, 8]

2. Генератор с фильтрацией (if)

[x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]

3. Генератор с тернарным оператором (if-else)

[x if x % 2 == 0 else -x for x in range(5)]
# [0, -1, 2, -3, 4]

4. Генератор с вложенными циклами

[x * y for x in range(1, 4) for y in range(1, 4)]
# [1, 2, 3, 2, 4, 6, 3, 6, 9]

Эквивалентный традиционный цикл:

result = []
for x in range(1, 4):
    for y in range(1, 4):
        result.append(x * y)

5. Вложенные циклы с фильтрацией

[x * y for x in range(1, 4) for y in range(1, 4) if x != y]
# [2, 3, 2, 6, 3, 6]

Правильный порядок в сложных случаях
1. Вложенные циклы с фильтрацией

[выражение for элемент1 in итерируемый1 if условие1 for элемент2 in итерируемый2 if условие2]

Пример:

[(x, y) for x in range(3) if x > 0 for y in range(3) if y < x]
# [(1, 0), (2, 0), (2, 1)]

2. Сочетание фильтрации и тернарного оператора

Если используется тернарный оператор (if-else), он идёт перед циклом:

[выражение_с_if_else for элемент in итерируемый if условие]

Пример:

[x if x % 2 == 0 else -x for x in range(5) if x > 1]
# [2, -3, 4]
