import math
class Coef:
    def vvod(a, str):
        while True:
            print(f"Введите {str}")
            a=input()
            try:
                return float(a)
            except:
                print("Введите число")
    def __init__(self):
        self.a = self.vvod('A')
        self.b = self.vvod('B')
        self.c = self.vvod('C')
class Roots(Coef):
    def poluchenie_roots(self):
        discr = self.b**2 -4*self.a*self.c
        if(discr>0):
            self.x1=(-self.b - math.sqrt(discr))/(2*self.a)
            self.x2=(-self.b + math.sqrt(discr))/(2*self.a)
        elif(discr==0):
            self.x1=self.b/(-2*self.a)
            self.x2=''
        else:
            self.x1=''
            self.x2=''
            print('No Roots')
        print(self.x1, self.x2)
if __name__ == "__main__":
    a=(Roots())
    a.poluchenie_roots()