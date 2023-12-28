import sys
def CalculateDiscriminant(a, b, c):
    return b**2 - 4*a*c
def CalculateRoots(a, b, discriminant):
    roots = []
    sq_roots = []
    if discriminant > 0:
        sq_roots.append((-b + discriminant**0.5) / (2*a))
        sq_roots.append((-b - discriminant**0.5) / (2*a))
    elif discriminant == 0:
         sq_roots.append(-b / (2*a))
    for a in sq_roots:
        if (a > 0):
            roots.append(a**(0.5))
            roots.append(-a**(0.5))
        if (a == 0):
            roots.append(a**(0.5))
    return roots
def InputCoefficient(prompt):
    while True:
        try:
            coefficient = float(input(prompt))
            return coefficient
        except ValueError:
            print("Ошибка ввода. Введите действительное число.")
    if __name__ == "__main__":
        if len(sys.argv) == 4:
            try:
                a = float(sys.argv[1])
                b = float(sys.argv[2])
                c = float(sys.argv[3])
            except ValueError:
                print("Некорректные коэффициенты. Пожалуйста, введите действительные числа.")
                sys.exit(1)
        else:
            print("Введите коэффициенты уравнения:")
            a = InputCoefficient("Коэффициент A: ")
            while a == 0:
                print("Коэффициент 'a' не может быть равен нулю для биквадратного уравнения.")
                a = InputCoefficient("Коэффициент A: ")
            b = InputCoefficient("Коэффициент B: ")
            c = InputCoefficient("Коэффициент C: ")
        discriminant = CalculateDiscriminant(a, b, c)
        if discriminant >= 0: 
            roots = CalculateRoots(a, b, discriminant)
            if len(roots) > 0:
                print("Корни уравнения:", roots)
        else:
            print("Уравнение не имеет действительных корней.")
