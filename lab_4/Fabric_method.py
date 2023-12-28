import math
class Point(object):
    def show(self, a, b):
       raise NotImplementedError
    def Print(self, a, b):
        self.show(a, b)
        return f'x: {self.x}, y: {self.y}'
class Polar(Point):
    def show(self, r, theta):
        self.x = r * math.cos(theta)
        self.y = r * math.sin(theta)

class Decart(Point):
    def show(self, x, y):
        self.x=x
        self.y=y

if __name__ == '__main__':
    print(Polar().Print(1, 2))
    print(Decart().Print(1, 2))
