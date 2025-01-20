from functools import wraps


class Singleton:
    instances = {}
    @classmethod
    def singleton(cls, external_class):
        print(cls.instances)
        @wraps(external_class)
        def wrapper(*args, **kwargs):
            print(cls.instances)
            if external_class not in cls.instances:
                cls.instances[external_class] = external_class(*args, **kwargs)
            return cls.instances[external_class]
        return wrapper

@Singleton.singleton
class MySingleton:
    def __init__(self, value):
        self.value = value

@Singleton.singleton
class AnotherClass:
    def __init__(self, value):
        self.value = value

# Использование
obj1 = MySingleton(10)
obj2 = MySingleton(20)

print(obj1.value)  # Выведет: 10
print(obj2.value)  # Также выведет: 10
print(obj1 is obj2)  # Выведет: True

obj_another1 = AnotherClass(10)
obj_another1 = AnotherClass(20)
