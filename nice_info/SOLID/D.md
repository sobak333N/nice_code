D-Dependency inversion principle

Модули верхнего уровня не должны зависеть от модулей нижнего уровня
И те, и другие должны зависеть от абстракций
Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций

Почему это важно?

    Ослабление связей:
        Верхний уровень (например, бизнес-логика) становится независимым от реализации нижнего уровня (например, базы данных, API).

    Гибкость:
        Легко менять реализацию (например, переключиться с базы данных на API) без изменения логики верхнего уровня.

    Тестируемость:
        Легко использовать заглушки (mock-объекты) вместо реальных модулей нижнего уровня для тестирования.


Пример нарушения принципа (Bad Practice)
Контекст:

Класс Service зависит напрямую от реализации репозитория DatabaseRepository.
```py
class DatabaseRepository:
    def save_data(self, data):
        print("Saving to database")

    def fetch_data(self, data):
        print("Fetching from database")


class Service:
    def __init__(self):
        self.repository = DatabaseRepository()

    def save_data(self, data):
        # Некоторая бизнес-логика
        self.repository.save_data(data)

    def fetch_data(self, data):
        # Некоторая бизнес-логика
        self.repository.fetch_data(data)
```
Проблемы:

    Класс Service зависит напрямую от конкретной реализации DatabaseRepository.
    Если нужно будет заменить хранилище (например, на API), придётся менять код в классе Service, что может привести к ошибкам.
    Отсутствие гибкости и модульности. Например, невозможно протестировать Service без использования реального DatabaseRepository.


Good practice

Например у нас есть класс для бизнес логики и сохранения информации
При этом он не будет зависеть от реализации того, как и куда будет сохраняться информация


```py
from abc import ABC, abstractmethod

class BaseRepository(ABC):
    @abstractmethod
    def save_data(self):
        pass
    
    @abstractmethod
    def fetch_data(self):
        pass
    

class DataBaseRepository(BaseRepository):
    def save_data(self, data):
        print("saving logic in database")

    def fetch_data(self, data):
        print("fetch logic in database")


class APIRepository(BaseRepository):
    def save_data(self, data):
        print("saving logic in API")

    def fetch_data(self, data):
        print("fetch logic in API")


class Service:
    def __init__(self, repository: BaseRepository):
        self.repository = repository

    def save_data(self, data):
        #some business logic
        self.repository.save_data(data)
    
    def fetch_data(self, data):
        #some business logic
        self.repository.fetch_data(data)
```

Преимущества:
    Класс Service теперь зависит от абстрактного интерфейса BaseRepository, а не от конкретной реализации.
    Легко заменить реализацию (DatabaseRepository на APIRepository) без изменений в классе Service.
    Повышается тестируемость: можно использовать mock-объекты для тестирования.