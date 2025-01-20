from my_array import MyList



def test_append():
    my_list = MyList()
    
    # Добавляем элементы
    my_list.append(1)
    assert len(my_list) == 1, "Тест не пройден: размер списка должен быть 1"
    assert my_list[0] == 1, "Тест не пройден: первый элемент должен быть 1"
    
    my_list.append(2)
    assert len(my_list) == 2, "Тест не пройден: размер списка должен быть 2"
    assert my_list[1] == 2, "Тест не пройден: второй элемент должен быть 2"
    
    # Перезаполнение списка, когда достигнут предел размера
    my_list.append(3)
    assert len(my_list) == 3, "Тест не пройден: размер списка должен быть 3 после добавления 3"
    assert my_list[2] == 3, "Тест не пройден: третий элемент должен быть 3"
    assert my_list.size == 3, "Тест не пройден: размер внутреннего массива должен быть увеличен"
    
    print("Тест append прошел успешно!")

def test_remove():
    my_list = MyList()
    
    # Добавляем элементы
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    
    # Удаляем элемент
    my_list.remove(2)
    assert len(my_list) == 2, "Тест не пройден: размер списка должен быть 2 после удаления элемента"
    assert 2 not in my_list, "Тест не пройден: элемент 2 должен быть удален из списка"
    
    # Попытка удалить несуществующий элемент
    try:
        my_list.remove(4)
        assert False, "Тест не пройден: ValueError должен был быть вызван при удалении несуществующего элемента"
    except ValueError:
        pass  # Ожидаемый результат
    
    print("Тест remove прошел успешно!")

def test_pop():
    my_list = MyList()
    
    # Добавляем элементы
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    
    # Убираем последний элемент
    my_list.pop()
    assert len(my_list) == 2, "Тест не пройден: размер списка должен быть 2 после pop"
    assert my_list[1] == 2, "Тест не пройден: последний элемент должен быть 2 после pop"
    
    # Убираем элемент по индексу
    my_list.pop(0)
    assert len(my_list) == 1, "Тест не пройден: размер списка должен быть 1 после pop по индексу"
    assert my_list[0] == 2, "Тест не пройден: первый элемент должен быть 2 после pop по индексу"
    
    # Попытка извлечь элемент из пустого списка
    try:
        my_list.pop(10)
        assert False, "Тест не пройден: IndexError должен был быть вызван при pop несуществующего индекса"
    except IndexError:
        pass  # Ожидаемый результат
    
    print("Тест pop прошел успешно!")

def test_iter_and_indexing():
    my_list = MyList()
    
    # Добавляем элементы
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    
    # Проверка индексации
    assert my_list[0] == 1, "Тест не пройден: первый элемент должен быть 1"
    assert my_list[1] == 2, "Тест не пройден: второй элемент должен быть 2"
    assert my_list[2] == 3, "Тест не пройден: третий элемент должен быть 3"
    
    # Итерация
    elements = [item for item in my_list]
    assert elements == [1, 2, 3], "Тест не пройден: элементы при итерации должны быть [1, 2, 3]"
    
    print("Тест итерации и индексации прошел успешно!")

def test_empty_list():
    my_list = MyList()
    
    # Проверка длины пустого списка
    assert len(my_list) == 0, "Тест не пройден: длина пустого списка должна быть 0"
    
    # Попытка удалить элемент из пустого списка
    try:
        my_list.remove(1)
        assert False, "Тест не пройден: ValueError должен был быть вызван при удалении элемента из пустого списка"
    except ValueError:
        pass  # Ожидаемый результат
    
    # Попытка извлечь элемент из пустого списка
    try:
        my_list.pop()
        assert False, "Тест не пройден: IndexError должен был быть вызван при извлечении элемента из пустого списка"
    except IndexError:
        pass  # Ожидаемый результат
    
    print("Тест пустого списка прошел успешно!")

def test_resize():
    my_list = MyList(size=2)
    
    # Добавляем элементы
    my_list.append(1)
    my_list.append(2)
    
    # Проверяем, что размер внутреннего массива увеличился

    # Добавляем еще один элемент
    my_list.append(3)
    
    assert my_list.size > 2, "Тест не пройден: размер массива не должен оставаться прежним после переполнения"
    assert len(my_list) == 3, "Тест не пройден: размер списка должен быть 2 после добавления элементов"

    for i in range(4,20):
        my_list.append(i)
        print(f"{my_list.size}  {my_list.cur_size}")

    # Проверка размера и элементов
    # assert len(my_list) == 3, "Тест не пройден: размер списка должен быть 3 после добавления третьего элемента"
    # assert my_list[2] == 3, "Тест не пройден: третий элемент должен быть 3"
    
    print("Тест на увеличение размера прошел успешно!")

if __name__ == "__main__":
    test_append()
    test_remove()
    test_pop()
    test_iter_and_indexing()
    test_empty_list()
    test_resize()
    print("Все тесты пройдены!")
