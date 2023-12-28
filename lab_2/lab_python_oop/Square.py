from lab_python_oop import Rectangle
class Square(Rectangle.Rectangle):
    name = "Квадрат"
    def Area(self):
        return self.a**2