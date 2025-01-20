# Создание метакласса
class MyMeta(type):
    register = []
    def __new__(cls, name, bases, dct):
        print(f"Создание класса {name} с базовыми классами {bases}")
        # Можно модифицировать атрибуты класса (dct)
        dct['custom_attribute'] = 'Я добавлен метаклассом!'
        class_ = super().__new__(cls, name, bases, dct)
        cls.register.append(class_) 
        return class_
    def __init__(self, name, bases, dct):
        self.test_value=111


# Класс с использованием метакласса MyMeta
class MyClass(metaclass=MyMeta):
    def __init__(self):
        self.value = 42


class MyClass2(metaclass=MyMeta):
    static_attr = "static_attr"
    def __init__(self):
        self.value = 52

# Создание экземпляра класса
obj = MyClass()
print(obj.__dict__) 
print(obj.custom_attribute)  # Вывод: Я добавлен метаклассом!
 # Вывод: Я добавлен метаклассом!
print(MyClass.__dict__)  # Вывод: Я добавлен метаклассом!

print('=================')

obj2 = MyClass2()
print(obj2.__dict__)  # Вывод: Я добавлен метаклассом!
print(MyClass2.__dict__)  # Вывод: Я добавлен метаклассом!

print(MyMeta.register)