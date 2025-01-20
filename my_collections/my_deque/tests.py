from my_deque import MyDeque

def test_deque_operations():
    # Создание пустой деки
    deque = MyDeque()

    # Тест 1: Проверка, что дека пуста
    assert deque.is_empty() == True, "Тест не пройден: дека должна быть пуста при создании"

    # Тест 2: Добавление элементов с конца
    deque.append(10)
    deque.append(20)
    deque.append(30)
    print(deque)
    assert deque.size() == 3, "Тест не пройден: размер деки должен быть 3 после добавления элементов"
    print(deque.peek())
    assert deque.peek() == 10, "Тест не пройден: первый элемент должен быть 10"
    assert deque.peeklast() == 30, "Тест не пройден: последний элемент должен быть 30"

    # Тест 3: Добавление элементов в начало
    deque.appendleft(0)
    deque.appendleft(-10)
    
    assert deque.peek() == -10, "Тест не пройден: первый элемент должен быть -10 после appendleft"
    assert deque.peeklast() == 30, "Тест не пройден: последний элемент должен быть 30"
    assert deque.size() == 5, "Тест не пройден: размер деки должен быть 5 после appendleft"

    # Тест 4: Удаление элементов с конца
    print(deque)

    assert deque.pop() == 30, "Тест не пройден: pop должен вернуть последний элемент (30)"
    assert deque.size() == 4, "Тест не пройден: размер деки должен быть 4 после pop"
    assert deque.peeklast() == 20, "Тест не пройден: последний элемент должен быть 20"

    # Тест 5: Удаление элементов с начала
    assert deque.popleft() == -10, "Тест не пройден: popleft должен вернуть первый элемент (-10)"
    assert deque.size() == 3, "Тест не пройден: размер деки должен быть 3 после popleft"
    assert deque.peek() == 0, "Тест не пройден: первый элемент должен быть 0 после popleft"

    # Тест 6: Проверка на пустоту
    deque.pop()
    deque.pop()
    deque.pop()
    
    assert deque.is_empty() == True, "Тест не пройден: дека должна быть пуста после удаления всех элементов"

    # Тест 7: Получение элементов с помощью peek (когда дека пуста)
    try:
        deque.peek()
        assert False, "Тест не пройден: исключение должно быть вызвано при попытке получить элемент из пустой деки"
    except IndexError:
        pass  # Ожидаем IndexError

    try:
        deque.peeklast()
        assert False, "Тест не пройден: исключение должно быть вызвано при попытке получить элемент из пустой деки"
    except IndexError:
        pass  # Ожидаем IndexError

    # Тест 8: Проверка итерации по деки
    deque.append(1)
    deque.append(2)
    deque.append(3)
    
    items = [item for item in deque]
    assert items == [1, 2, 3], "Тест не пройден: элементы деки должны быть [1, 2, 3]"

    print("Все тесты пройдены!")

# Запуск тестов
if __name__ == "__main__":
    test_deque_operations()
