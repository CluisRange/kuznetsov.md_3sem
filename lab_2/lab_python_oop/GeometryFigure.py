from abc import ABC, abstractmethod

class GeometryFigure(ABC):
    @abstractmethod
    def Area(self):
        pass
    def __repr__(self):
        return f'{self.name}, площадь = {self.area}, цвет = {self.color}.'



