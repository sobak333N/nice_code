S-Single Responsibility Principle (SRP)

Определение:

Каждый класс должен иметь только одну ответственность. Другими словами, каждый класс отвечает только за одну часть логики программы.

    Простота понимания:
        Класс, который выполняет только одну задачу, проще понять, тестировать и поддерживать.

    Меньше ошибок:
        Если логика разделена между классами, изменение одной части программы с меньшей вероятностью повлияет на другие.

    Повышение гибкости:
        Легче добавлять новые функции или изменять существующие, если классы имеют чётко определённые роли.

Пример нарушения принципа (Bad Practice)
```python
class User:
    def send_info(self):
        pass

    def receive_info(self):
        pass

    def calculate_amount_of_liabilities(self):
        pass

    def calculate_percent_of_taxes(self):
        pass
```
Проблема:

    Класс User выполняет несколько несвязанных задач:
        Управление информацией (send_info, receive_info).
        Финансовые расчёты (calculate_amount_of_liabilities, calculate_percent_of_taxes).
    Это приводит к созданию God Class, который нарушает SRP и затрудняет сопровождение.
    Сделаем декомпозицию

Пример соблюдения принципа (Good Practice)
```python
class InfoInteraction:
    def send_info(self):
        pass

    def receive_info(self):
        pass

class FinancialCalculator:
    def calculate_amount_of_liabilities(self):
        pass

    def calculate_percent_of_taxes(self):
        pass
```
Что изменилось:

    Логика разделена на два класса:
        InfoInteraction отвечает только за управление информацией.
        FinancialCalculator отвечает только за расчёты.
    Каждый класс теперь выполняет только одну задачу, что делает код более читаемым и поддерживаемым.