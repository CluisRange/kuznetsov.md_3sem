from lab_python_oop import Rectangle
import pytest
@pytest.mark.parametrize("color, a, b", [("Красный", 17, 17),
                                         ("Синий", 10, 17),
                                         ("Зеленый", 100, 2)])
def test_Rectangle(color, a, b):
    assert Rectangle.Rectangle(color, a, b).color == color
    assert Rectangle.Rectangle(color, a, b).area == a*b
    assert Rectangle.Rectangle(color, a, b).name == "Прямоугольник"