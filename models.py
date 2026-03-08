import math

class Shape:
    """
    Базовый класс для всех фигур.
    Используется для реализации полиморфизма: все наследники
    будут иметь метод __str__ для красивого вывода в консоль.
    """
    def __str__(self):
        raise NotImplementedError("Метод __str__ должен быть переопределен в дочерних классах")

class Point(Shape):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        # Используем f-строки — это современный стандарт Python
        return f"Точка(x={self.x}, y={self.y})"

class Line(Shape):
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        # Отрезок состоит из двух точек. Можно было передать объекты Point,
        # но для CLI удобнее принимать набор координат напрямую.
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)

    def __str__(self):
        return f"Отрезок: от {self.start} до {self.end}"

class Circle(Shape):
    def __init__(self, x: float, y: float, radius: float):
        self.center = Point(x, y)
        self.radius = radius

    def __str__(self):
        return f"Круг: центр {self.center}, радиус={self.radius}"

class Square(Shape):
    def __init__(self, x: float, y: float, side: float):
        # Квадрат задаем по верхней левой точке и длине стороны
        self.top_left = Point(x, y)
        self.side = side

    def __str__(self):
        return f"Квадрат: левый верхний угол {self.top_left}, сторона={self.side}"