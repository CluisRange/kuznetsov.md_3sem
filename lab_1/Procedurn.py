import math
def root(a, b, c):
    discr = b ** 2 - 4 * a * c
    if (discr > 0):
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(x1, x2)
    elif (discr == 0):
        x1 = (-b) / (2 * a)
        print(x1)
    else:
        print('Нет корней!')


def vvod(s):
    print(s)
    while True:
        coef = input()
        try:
            return float(coef)

        except ValueError:
            print("Введите число!")


if __name__ == "__main__":
    a = vvod('Введите коэффициент A')
    b = vvod('Введите коэффициент B')
    c = vvod('Введите коэффициент C')
    root(a, b, c)
