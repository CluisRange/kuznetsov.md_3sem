from lab_python_oop import GeometryFigure
from lab_python_oop import Color
import math
class Circle(GeometryFigure.GeometryFigure):
    name = "Круг"
    def __init__(self, color, r):
        self.color=Color.Color(color).color
        self.r=r
        self.area = Circle.Area(self)
    def Area(self):
        self.area = (self.r ** 2) * math.pi
        return self.area
