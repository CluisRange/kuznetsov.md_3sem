from lab_python_oop import GeometryFigure
from lab_python_oop import Color
class Rectangle(GeometryFigure.GeometryFigure):
    name="Прямоугольник"

    def __init__(self, color, a, b=1):
        self.color=Color.Color(color).color
        self.a=a
        self.b=b
        self.area = self.Area()
    def Area(self):
        return self.a * self.b



