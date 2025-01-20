L-Liskov substitutuion principle

Объекты в программе должны быть заменяемы их подклассами, без изменения корректности программы

То есть если В является подклассом класса А, то в областях программы, где использовался класс А, объекты класса В,
должны также ипользоваться корректно

Почему важно
Универсальность:
    Возможность работать с подклассами так же, как с базовым классом, упрощает расширение функциональности

Bad practice:
```py
class Bird:
    def talk(self):
        pass
    def fly(self):
        print("flying")


class Eagle(Bird):
    def talk(self):
        print("eagle talking")


class Penguin(Bird):
    def talk(self):
        print("penguin talking")

    def fly(self):
        raise NotImplementedError("penguins can't fly")
```
Класс пингвин нарушает логику класса Bird
например функция, которая будет ожидать объект типа Bird,
сломается при использоваии объекта класса пингвин
```py
def make_bird_fly(bird: Bird):
    bird.fly()

birds = [Eagle(),Penguin()]
for bird in birds:
    make_bird_fly(bird)
```



Пример соблюдения принципа (Good Practice)
Исправление:

    Создаём базовый класс Bird с более точным разделением обязанностей.
    Добавляем интерфейсы или методы, специфичные для летающих птиц.
```py
class Bird:
    def eat(self):
        print("Eating seeds")


class FlyingBird(Bird):
    def fly(self):
        print("Flying high!")


class NonFlyingBird(Bird):
    def swim(self):
        print("Swimming in water")


class Penguin(NonFlyingBird):
    def swim(self):
        print("Penguins are excellent swimmers!")

Использование:

def let_bird_eat(bird: Bird):
    bird.eat()

def let_flying_bird_fly(bird: FlyingBird):
    bird.fly()

def let_swimming_bird_swim(bird: NonFlyingBird):
    bird.swim()


sparrow = FlyingBird()
penguin = Penguin()

let_bird_eat(sparrow)  # Eating seeds
let_flying_bird_fly(sparrow)  # Flying high!

let_bird_eat(penguin)  # Eating seeds
let_swimming_bird_swim(penguin)  # Penguins are excellent swimmers!
```
Что изменилось:

    Базовый класс Bird теперь отражает общие свойства всех птиц.
    Летающие и нелетающие птицы разделены через отдельные подклассы, что исключает ошибки и делает поведение предсказуемым.