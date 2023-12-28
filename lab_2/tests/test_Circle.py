from lab_python_oop import Circle
import math
import pytest
@pytest.mark.parametrize("color, area", [("Красный", 17),
                                         ("Синий", 10),
                                         ("Зеленый", 100)])
def test_Circle(color, area):
    assert Circle.Circle(color, area).color == color
    assert Circle.Circle(color, area).area == (area** 2) * math.pi
    assert Circle.Circle(color, area).name == "Круг"