from lab_python_oop import Square
import pytest
@pytest.mark.parametrize("color, a", [("Красный", 17),
                                         ("Синий", 10),
                                         ("Зеленый", 100)])
def test_Rectangle(color, a):
    assert Square.Square(color, a).color == color
    assert Square.Square(color, a).area == a**2
    assert Square.Square(color, a).name == "Квадрат"