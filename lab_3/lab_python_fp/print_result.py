def print_result(func):
    def wrapper(*args):
        print(func.__name__)
        a=func(*args)
        if(isinstance(a, list)):
            for i in a:
                if(isinstance(i, tuple)):
                    print(*i)
                else:
                    print(i)
        elif(isinstance(a, dict)):
            for i in a.keys():
                print(f'{i} = {a[i]}')


        else: print(a)
        return a
    return wrapper



def main():
    @print_result
    def test_1():
        return 1

    @print_result
    def test_2():
        return 'iu5'

    @print_result
    def test_3():
        return {'a': 1, 'b': 2}

    @print_result
    def test_4():
        return [1, 2]
    test_1()
    test_2()
    test_3()
    test_4()