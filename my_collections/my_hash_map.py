from pydantic import BaseModel
from typing import List, Optional, Tuple, Any


class Node(BaseModel):
    key: Any
    value: Any
    # def __init__(self, key: Any, value: Any):
    #     self.key = key
    #     self.value = value


class MyHashMap(BaseModel):
    buckets_size: int = 10
    load_factor: float = 0.75
    buckets: List[List[Node]] = []

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.buckets = [[] for _ in range(self.buckets_size)]

    def _hash(self, key: Any):
        return hash(key) % self.buckets_size

    def _resize(self, new_len: int):
        all_nodes = [node for bucket in self.buckets for node in bucket]
        self.buckets_size = new_len
        self.buckets = [[] for _ in range(new_len)]
        for node in all_nodes:
            index = self._hash(node.key)
            self.buckets[index].append(node)

    def __getitem__(self, key: Any):
        index = self._hash(key)
        for item in self.buckets[index]:
            if item.key == key:
                return item.value
        raise KeyError
    
    def __setitem__(self, key: Any, value: Any):
        index = self._hash(key)
        for item in self.buckets[index]:
            if item.key == key:
                item.value = value
                return
            
        new_node = Node(key=key, value=value)
        self.buckets[index].append(new_node)
        if len(self) > self.load_factor * self.buckets_size:
            self._resize(self.buckets_size*2)

    def __contains__(self, key: Any):
        index = self._hash(key)
        for item in self.buckets[index]:
            if item.key == key:
                return True
        return False

    def __len__(self):
        return sum([len(bucket) for bucket in self.buckets])            

    def pop(self, key: Any):
        index = self._hash(key)
        for i, item in enumerate(self.buckets[index]):
            if item.key == key:
                self.buckets[index].pop(i)
                return
        raise KeyError
    
    def items(self):
        return [(node.key, node.value) for bucket in self.buckets for node in bucket]

    def __str__(self):
        return "{ " + ", ".join([f"{key}: {value}" for key, value in self.items()]) + " }"

    # def __repr__(self):
    #     return "{ " + ", ".join([f"{key}: {value}" for key, value in self.items()]) + " }"




def test_put_and_get():
    hashmap = MyHashMap()

    # Добавляем элемент
    hashmap["key1"] = "value1"
    assert hashmap["key1"] == "value1", "Тест не пройден: значение для 'key1' неверное"

    # Добавляем второй элемент
    hashmap["key2"] = "value2"
    assert hashmap["key2"] == "value2", "Тест не пройден: значение для 'key2' неверное"

    # Проверка, что несуществующий элемент вызывает KeyError
    try:
        hashmap["non_existent_key"]
        assert False, "Тест не пройден: KeyError не был вызван"
    except KeyError:
        pass  # Ожидаемый результат

def test_update_existing_key():
    hashmap = MyHashMap()

    # Добавляем элемент
    hashmap["key1"] = "value1"
    assert hashmap["key1"] == "value1", "Тест не пройден: значение для 'key1' неверное"

    # Обновляем элемент с существующим ключом
    hashmap["key1"] = "new_value"
    assert hashmap["key1"] == "new_value", "Тест не пройден: обновление значения для 'key1' неверное"

def test_contains():
    hashmap = MyHashMap()

    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"

    # Проверяем, что ключи содержатся в хеш-таблице
    assert "key1" in hashmap, "Тест не пройден: 'key1' должен быть в хеш-таблице"
    assert "key2" in hashmap, "Тест не пройден: 'key2' должен быть в хеш-таблице"
    
    # Проверка для несуществующего ключа
    assert "key3" not in hashmap, "Тест не пройден: 'key3' не должен быть в хеш-таблице"

def test_len():
    hashmap = MyHashMap()

    # Проверка пустой хеш-таблицы
    assert len(hashmap) == 0, "Тест не пройден: длина пустой хеш-таблицы должна быть 0"

    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"

    # Проверка длины после добавления элементов
    assert len(hashmap) == 2, "Тест не пройден: длина хеш-таблицы должна быть 2"

    hashmap.pop("key1")

    # Проверка длины после удаления элемента
    assert len(hashmap) == 1, "Тест не пройден: длина хеш-таблицы должна быть 1"

def test_pop():
    hashmap = MyHashMap()

    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"

    # Проверяем удаление элемента
    hashmap.pop("key1")
    assert "key1" not in hashmap, "Тест не пройден: 'key1' должен быть удалён"

    # Проверяем удаление несуществующего ключа (должен подняться KeyError)
    try:
        hashmap.pop("non_existent_key")
        assert False, "Тест не пройден: KeyError не был вызван при удалении несуществующего ключа"
    except KeyError:
        pass  # Ожидаемый результат

def test_resize():
    hashmap = MyHashMap(buckets_size=2, load_factor=0.5)

    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"
    hashmap["key3"] = "value3"
    # Проверка, что размер хеш-таблицы увеличился (порог нагрузки был превышен)
    assert hashmap.buckets_size > 2, "Тест не пройден: хеш-таблица не была перераспределена (resize не сработал)"

def test_items():
    hashmap = MyHashMap()

    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"

    # Проверяем метод items
    items = hashmap.items()
    assert ("key1", "value1") in items, "Тест не пройден: пары (key1, value1) нет в items"
    assert ("key2", "value2") in items, "Тест не пройден: пары (key2, value2) нет в items"

def test_empty_hash_map():
    hashmap = MyHashMap()

    # Проверяем хеш-таблицу, когда она пустая
    assert len(hashmap) == 0, "Тест не пройден: длина пустой хеш-таблицы должна быть 0"
    assert "any_key" not in hashmap, "Тест не пройден: 'any_key' не должен быть в пустой хеш-таблице"

def test_resize_down():
    hashmap = MyHashMap(buckets_size=10, load_factor=0.5)

    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"
    hashmap["key3"] = "value3"

    # После уменьшения размера таблицы (удаление ключей) таблица должна уменьшиться
    hashmap.pop("key1")
    hashmap.pop("key2")
    
    # Проверяем уменьшение размера
    assert hashmap.buckets_size < 10, "Тест не пройден: размер хеш-таблицы не уменьшился"

def test_mixed_operations():
    hashmap = MyHashMap()

    # Смешанные операции вставки и удаления
    hashmap["key1"] = "value1"
    hashmap["key2"] = "value2"
    hashmap["key3"] = "value3"

    # Удаляем один элемент
    hashmap.pop("key2")

    # Добавляем ещё один элемент
    hashmap["key4"] = "value4"

    # Проверяем правильность содержимого
    assert "key1" in hashmap
    assert "key3" in hashmap
    assert "key4" in hashmap
    assert "key2" not in hashmap

    # Проверяем размер
    assert len(hashmap) == 3, "Тест не пройден: неверный размер хеш-таблицы после смешанных операций"

def test_large_number_of_elements():
    hashmap = MyHashMap()

    # Вставляем много элементов
    for i in range(1000):
        hashmap[f"key{i}"] = f"value{i}"

    # Проверяем, что хеш-таблица не пуста
    assert len(hashmap) == 1000, "Тест не пройден: неверный размер хеш-таблицы после добавления 1000 элементов"

    # Проверяем наличие некоторых элементов
    for i in range(100):
        assert f"key{i}" in hashmap, f"Тест не пройден: 'key{i}' не найден"

def test_key_error_on_getitem():
    hashmap = MyHashMap()

    try:
        hashmap["key1"]
        assert False, "Тест не пройден: KeyError не был вызван при попытке получить несуществующий ключ"
    except KeyError:
        pass  # Ожидаемый результат



class Pair(BaseModel):
    first: Any
    second: Any

    def __eq__(self, another):
        if self.first == another.first and self.second == another.second:
            return True
        return False
    
    def __hash__(self):
        return hash(tuple([self.first, self.second]))


    def __str__(self):
        return f"({self.first}, {self.second})"

    # def __repr__(self):
    #     print("XUI")
        # return hash(tuple([self.first, self.second]))


def test_custom_class_as_key():
    hashmap = MyHashMap()

    # Создаём несколько объектов класса Pair
    pair1 = Pair(first="a", second=1)
    pair2 = Pair(first="b", second=2)
    pair3 = Pair(first="a", second=1)  # Должен быть равен pair1 по значению
    print(pair1)
    # Добавляем пары в хеш-таблицу
    hashmap[pair1] = "value1"
    hashmap[pair2] = "value2"

    # Проверяем, что правильное значение возвращается для правильного ключа
    assert hashmap[pair1] == "value1", "Тест не пройден: значение для pair1 неверное"
    assert hashmap[pair2] == "value2", "Тест не пройден: значение для pair2 неверное"

    # Проверяем, что два одинаковых объекта Pair имеют одинаковый хэш и считаются равными
    assert pair1 == pair3, "Тест не пройден: pair1 должен быть равен pair3"
    assert hash(pair1) == hash(pair3), "Тест не пройден: хэш pair1 и pair3 должен быть одинаковым"

    # Проверяем, что обновление значений для одинаковых ключей работает корректно
    hashmap[pair3] = "new_value"
    assert hashmap[pair1] == "new_value", "Тест не пройден: значение для pair1 не обновилось"

    # Проверка на наличие ключа
    assert pair1 in hashmap, "Тест не пройден: pair1 должен быть в хеш-таблице"
    assert pair3 in hashmap, "Тест не пройден: pair3 должен быть в хеш-таблице"

    # Проверка на отсутствие несуществующего ключа
    pair4 = Pair(first="c", second=3)
    assert pair4 not in hashmap, "Тест не пройден: pair4 не должен быть в хеш-таблице"

    # Удаляем элемент по ключу
    hashmap.pop(pair1)
    assert pair1 not in hashmap, "Тест не пройден: pair1 должен быть удалён"

def test_mixed_operations_with_custom_class():
    hashmap = MyHashMap()

    # Создаём несколько объектов Pair
    pair1 = Pair(first="a", second=1)
    pair2 = Pair(first="b", second=2)
    pair3 = Pair(first="a", second=1)  # Должен быть равен pair1 по значению

    # Вставляем пары
    hashmap[pair1] = "value1"
    hashmap[pair2] = "value2"

    # print(hashmap)
    # Удаляем и добавляем новые пары
    hashmap.pop(pair1)
    hashmap[pair3] = "value3"  # pair3 должен быть равен pair1
    print(hashmap)


    # Проверка на корректное обновление значений и хэширование
    assert hashmap[pair3] == "value3", "Тест не пройден: значение для pair3 неверное"
    assert pair3 in hashmap, "Тест не пройден: pair3 должен быть в хеш-таблице"

def test_hash_custom_class():
    # Проверка, что одинаковые объекты имеют одинаковый хэш
    pair1 = Pair(first="a", second=1)
    pair2 = Pair(first="a", second=1)
    pair3 = Pair(first="b", second=2)

    assert hash(pair1) == hash(pair2), "Тест не пройден: одинаковые объекты должны иметь одинаковый хэш"
    assert hash(pair1) != hash(pair3), "Тест не пройден: разные объекты должны иметь разные хэши"

def test_equality_custom_class():
    pair1 = Pair(first="a", second=1)
    pair2 = Pair(first="a", second=1)
    pair3 = Pair(first="b", second=2)

    # Проверка равенства объектов
    assert pair1 == pair2, "Тест не пройден: pair1 должен быть равен pair2"
    assert pair1 != pair3, "Тест не пройден: pair1 не должен быть равен pair3"




# Запуск тестов
if __name__ == "__main__":
    test_put_and_get()
    test_update_existing_key()
    test_contains()
    test_len()
    test_pop()
    test_resize()
    test_items()
    test_empty_hash_map()
    # test_resize_down()    
    test_mixed_operations()
    test_large_number_of_elements()
    test_key_error_on_getitem()


    test_custom_class_as_key()
    test_mixed_operations_with_custom_class()
    test_hash_custom_class()
    test_equality_custom_class()


    print("Все тесты пройдены!")