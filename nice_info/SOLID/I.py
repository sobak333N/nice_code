from abc import ABC, abstractmethod
from math import pi, sqrt


# --- Общие интерфейсы ---
class Shape(ABC):
    """Базовый интерфейс для всех фигур"""
    @abstractmethod
    def describe(self) -> str:
        """Описание фигуры"""
        pass


class AreaCalculable(ABC):
    """Интерфейс для вычисления площади"""
    @abstractmethod
    def area(self) -> float:
        pass


class PerimeterCalculable(ABC):
    """Интерфейс для вычисления периметра"""
    @abstractmethod
    def perimeter(self) -> float:
        pass


class VolumeCalculable(ABC):
    """Интерфейс для вычисления объёма"""
    @abstractmethod
    def volume(self) -> float:
        pass


# --- Абстрактные классы для 2D и 3D фигур ---
class TwoDimensionalShape(Shape, AreaCalculable, PerimeterCalculable):
    """Базовый класс для всех 2D фигур"""
    @abstractmethod
    def describe(self) -> str:
        pass


class ThreeDimensionalShape(Shape, AreaCalculable, VolumeCalculable):
    """Базовый класс для всех 3D фигур"""
    @abstractmethod
    def describe(self) -> str:
        pass


# --- Реализации 2D фигур ---
class Rectangle(TwoDimensionalShape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def describe(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Circle(TwoDimensionalShape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * pi * self.radius

    def describe(self) -> str:
        return f"Circle(radius={self.radius})"


class Triangle(TwoDimensionalShape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        s = self.perimeter() / 2  # Полупериметр
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Формула Герона

    def perimeter(self) -> float:
        return self.a + self.b + self.c

    def describe(self) -> str:
        return f"Triangle(a={self.a}, b={self.b}, c={self.c})"


# --- Реализации 3D фигур ---
class Cube(ThreeDimensionalShape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return 6 * (self.side ** 2)

    def volume(self) -> float:
        return self.side ** 3

    def describe(self) -> str:
        return f"Cube(side={self.side})"


class Sphere(ThreeDimensionalShape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 4 * pi * self.radius ** 2

    def volume(self) -> float:
        return (4 / 3) * pi * self.radius ** 3

    def describe(self) -> str:
        return f"Sphere(radius={self.radius})"


class Cylinder(ThreeDimensionalShape):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def area(self) -> float:
        return 2 * pi * self.radius * (self.radius + self.height)

    def volume(self) -> float:
        return pi * self.radius ** 2 * self.height

    def describe(self) -> str:
        return f"Cylinder(radius={self.radius}, height={self.height})"


# --- Менеджер для работы с фигурами ---
class ShapeManager:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        self.shapes.append(shape)

    def calculate_all(self):
        for shape in self.shapes:
            print(shape.describe())
            if isinstance(shape, AreaCalculable):
                print(f"  Area: {shape.area()}")
            if isinstance(shape, PerimeterCalculable):
                print(f"  Perimeter: {shape.perimeter()}")
            if isinstance(shape, VolumeCalculable):
                print(f"  Volume: {shape.volume()}")


# --- Пример использования ---
if __name__ == "__main__":
    manager = ShapeManager()

    # Добавляем 2D фигуры
    manager.add_shape(Rectangle(10, 5))
    manager.add_shape(Circle(7))
    manager.add_shape(Triangle(3, 4, 5))

    # Добавляем 3D фигуры
    manager.add_shape(Cube(4))
    manager.add_shape(Sphere(6))
    manager.add_shape(Cylinder(3, 7))

    # Рассчитываем параметры всех фигур
    manager.calculate_all()
