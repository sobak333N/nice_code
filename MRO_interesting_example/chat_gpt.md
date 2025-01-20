BaseRepository initialized with model: <class 'int'>
[<class '__main__.DocumentRepository'>, <class '__main__.BaseRepository'>, <class 'typing.Generic'>, <class 'object'>]
DocumentRepository initialized with document_model: <class 'str'>
====================================================================================================
BaseRepository initialized with model: <class 'int'>
[<class '__main__.DocumentRepository'>, <class '__main__.BaseRepository'>, <class 'typing.Generic'>, <class 'object'>]
DocumentRepository initialized with document_model: <class 'str'>
====================================================================================================
CUSTOM CLASSES
[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
====================================================================================================
[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
====================================================================================================
[<class '__main__.DocumentRepository'>, <class '__main__.A'>, <class '__main__.BaseRepository'>, <class 'typing.Generic'>, <class 'object'>]
====================================================================================================
[<class '__main__.DocumentRepository'>, <class '__main__.BaseRepository'>, <class 'typing.Generic'>, <class '__main__.A'>, <class 'object'>]



from typing import Generic, TypeVar, Type

T = TypeVar('T')
D = TypeVar('D')

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model
        print(f"BaseRepository initialized with model: {model}")

class DocumentRepository(BaseRepository[T], Generic[T, D]):
    def __init__(self, model: Type[T], document_model: Type[D]):
        super().__init__(model)
        self.document_model = document_model
        print(DocumentRepository.mro())
        print(f"DocumentRepository initialized with document_model: {document_model}")

DocumentRepository(int, str)


class DocumentRepository(Generic[T, D], BaseRepository[T]):
    def __init__(self, model: Type[T], document_model: Type[D]):
        super().__init__(model)
        self.document_model = document_model
        print(DocumentRepository.mro())
        print(f"DocumentRepository initialized with document_model: {document_model}")
        

print("="*100)
DocumentRepository(int, str)
# SAME BEHAVIOR




# Custom classes:

class A:
    pass

class B:
    pass

class C(A, B):
    def __init__(self):
        print(C.mro())

print("="*100)
print("CUSTOM CLASSES")
C()

class C(B, A):
    def __init__(self):
        print(C.mro())
   

print("="*100)
C()


# ANOTHER TESTS




class DocumentRepository(A, BaseRepository[T]):
    def __init__(self):
        print(DocumentRepository.mro())
        

print("="*100)
DocumentRepository()


class DocumentRepository(BaseRepository[T], A):
    def __init__(self):
        print(DocumentRepository.mro())
        

print("="*100)
DocumentRepository()

объясни подробно данное поведение

***ChatGPT said***:
ChatGPT

Давайте разберем поведение вашего кода шаг за шагом, чтобы объяснить, почему MRO остается одинаковым в одних случаях и меняется в других.
1. Поведение MRO в Generic-классах
Ваш пример:

class BaseRepository(Generic[T]):
    def __init__(self, model: Type[T]):
        self.model = model

class DocumentRepository(BaseRepository[T], Generic[T, D]):
    def __init__(self, model: Type[T], document_model: Type[D]):
        super().__init__(model)
        self.document_model = document_model
        print(DocumentRepository.mro())

Результат:

[<class '__main__.DocumentRepository'>, <class '__main__.BaseRepository'>, <class 'typing.Generic'>, <class 'object'>]

Пояснение:

    В Python классы с Generics, такие как BaseRepository и Generic, имеют предсказуемое поведение.
    В данном случае MRO (Method Resolution Order) формируется следующим образом:
        DocumentRepository (сам класс).
        BaseRepository (первый родительский класс с конкретным методом __init__).
        Generic (базовый класс для Generics, встроенный в Python).
        object (самая базовая часть Python).
    Generic[T, D] не имеет собственного метода __init__, поэтому он просто включается в MRO без изменения порядка.

Почему MRO не меняется при изменении порядка наследования?

Если вы измените порядок наследования:

class DocumentRepository(Generic[T, D], BaseRepository[T]):
    def __init__(self, model: Type[T], document_model: Type[D]):
        super().__init__(model)
        self.document_model = document_model
        print(DocumentRepository.mro())

Результат останется таким же:

[<class '__main__.DocumentRepository'>, <class '__main__.BaseRepository'>, <class 'typing.Generic'>, <class 'object'>]

    Почему? Python обрабатывает MRO на основе C3-линеаризации. В этом случае:
        BaseRepository является более конкретным классом, чем Generic, поэтому он остается выше Generic в MRO.
        Generic всегда находится после конкретных родительских классов, поскольку его роль — предоставление типизации, а не методов.

2. MRO в обычных классах
Ваш пример:

class A:
    pass

class B:
    pass

class C(A, B):
    def __init__(self):
        print(C.mro())

Результат:

[<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]

Теперь изменим порядок наследования:

class C(B, A):
    def __init__(self):
        print(C.mro())

Результат:

[<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

Пояснение:

    В данном случае MRO меняется, потому что A и B — обычные классы без сложной иерархии.
    Python просто следует порядку, в котором классы указаны при наследовании (B раньше A).

3. Смешивание Generics с обычными классами
Ваш пример:

class DocumentRepository(A, BaseRepository[T]):
    def __init__(self):
        print(DocumentRepository.mro())

Результат:

[<class '__main__.DocumentRepository'>, <class '__main__.A'>, <class '__main__.BaseRepository'>, <class 'typing.Generic'>, <class 'object'>]

Теперь изменим порядок наследования:

class DocumentRepository(BaseRepository[T], A):
    def __init__(self):
        print(DocumentRepository.mro())

Результат:

[<class '__main__.DocumentRepository'>, <class '__main__.BaseRepository'>, <class 'typing.Generic'>, <class '__main__.A'>, <class 'object'>]

Пояснение:

    Теперь A смешивается с Generics. При этом BaseRepository остаётся выше в MRO, так как оно связано с Generic и идёт перед ним.
    Когда вы меняете порядок A и BaseRepository, Python перераспределяет их в MRO согласно C3-линеаризации.

4. Почему C3-линеаризация важна?

C3-линеаризация используется Python, чтобы:

    Убедиться, что классы перечислены в таком порядке, чтобы избежать конфликтов.
    Сохранять консистентность: если класс наследуется от двух родителей, порядок наследования должен быть логичным.

Алгоритм C3 гарантирует:

    Если класс C наследуется от A и B, A идёт раньше B, только если это указано явно.
    Python обрабатывает деревья зависимостей рекурсивно, чтобы построить последовательность без конфликтов.

5. Что важно помнить о MRO и Generics

    Generics не оказывают влияния на порядок методов, если они не содержат реализации. Они просто добавляются в MRO как вспомогательные элементы.
    Обычные классы изменяют MRO в зависимости от порядка наследования.
    Смешанные случаи (обычные классы + Generics): порядок наследования Generic-классов может остаться неизменным, а обычные классы добавляются выше или ниже в зависимости от их приоритета.

Выводы:

    MRO для Generics всегда включает Generic после основного функционального класса (например, BaseRepository).
    Изменение порядка наследования работает только для классов, которые не входят в типизированные структуры, такие как Generics.
    Алгоритм C3-линеаризации гарантирует, что MRO остаётся предсказуемым и не создаёт конфликтов в сложных иерархиях наследования.

You said:
и к кому обращается super() к тому кто стоит первый после текущего класса в mro() линеаризации
ChatGPT said:
ChatGPT

Да, абсолютно верно! Вызов super() обращается к следующему классу в порядке MRO (Method Resolution Order) после текущего класса, из которого производится вызов.
Как работает super() с MRO?

    Когда вы вызываете super(), Python просматривает MRO текущего класса, чтобы определить, кто стоит следующим в цепочке наследования.
    После нахождения текущего класса в MRO, super() вызывает метод (например, __init__) у первого класса, следующего за текущим в MRO.

Пример с объяснением

class A:
    def __init__(self):
        print("A.__init__ called")

class B(A):
    def __init__(self):
        print("B.__init__ called")
        super().__init__()  # Ищет следующий класс в MRO после B

class C(B):
    def __init__(self):
        print("C.__init__ called")
        super().__init__()  # Ищет следующий класс в MRO после C

c = C()

MRO для класса C:

print(C.mro())
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

Результат выполнения кода:

C.__init__ called
B.__init__ called
A.__init__ called

Пояснение:

    Когда super().__init__() вызывается в классе C, Python ищет следующий класс в MRO после C, это B.
    Когда super().__init__() вызывается в классе B, Python ищет следующий класс в MRO после B, это A.

Взаимодействие с множественным наследованием

super() также обращается к следующему классу в MRO, даже если используются несколько родителей.

class A:
    def __init__(self):
        print("A.__init__ called")

class B(A):
    def __init__(self):
        print("B.__init__ called")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__ called")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__ called")
        super().__init__()

d = D()

MRO для класса D:

print(D.mro())
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

Результат выполнения:

D.__init__ called
B.__init__ called
C.__init__ called
A.__init__ called

Пояснение:

    super().__init__() в классе D вызывает B.__init__ (следующий класс в MRO после D).
    super().__init__() в классе B вызывает C.__init__ (следующий класс в MRO после B).
    super().__init__() в классе C вызывает A.__init__.

Когда super() полезен

    Для вызова методов родительских классов:
        super() позволяет избежать жесткого указания имени родительского класса.
        Это особенно полезно при изменении иерархии наследования.

    Для множественного наследования:
        super() соблюдает MRO и гарантирует, что каждый класс вызывается ровно один раз.
        Это важно, чтобы избежать дублирования вызовов (например, дважды вызвать A.__init__).

Ошибки, связанные с super()
1. Отсутствие корректной реализации метода

Если следующий класс в MRO не реализует метод, который вы пытаетесь вызвать через super(), будет выброшено исключение AttributeError.

Пример:

class A:
    pass

class B(A):
    def method(self):
        super().method()  # Ошибка! У A нет метода `method`

B().method()
# AttributeError: 'super' object has no attribute 'method'

2. Пропуск super() в цепочке

Если один из классов в MRO не вызывает super(), это может нарушить цепочку вызовов.

Пример:

class A:
    def __init__(self):
        print("A.__init__ called")

class B(A):
    def __init__(self):
        print("B.__init__ called")
        # super().__init__() пропущен

class C(B):
    def __init__(self):
        print("C.__init__ called")
        super().__init__()

c = C()

Результат:

C.__init__ called
B.__init__ called

Что произошло?

    B.__init__ не вызвал super().__init__(), поэтому A.__init__ не был вызван.

Вывод

    super() всегда обращается к следующему классу в порядке MRO, после текущего класса.
    MRO обеспечивает предсказуемость и безопасность при вызове методов в сложных иерархиях.
    Используйте super() везде, где методы родительских классов должны быть вызваны, особенно при множественном наследовании.