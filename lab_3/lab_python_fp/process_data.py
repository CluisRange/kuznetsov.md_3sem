import json
import sys
import print_result
import field
import cm_timer
import sort
import unique
import gen_random
# Сделаем другие необходимые импорты

path = 'data_light.json'

# Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

with open(path, encoding='utf-8') as f:
    data = json.load(f)

# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк
@print_result.print_result
def f1():
    return sort.Sort(unique.zapusk(field.zapusk(data, 'job-name'), True))

@print_result.print_result
def f2(arg):
    return list(filter(lambda it: 'программист' in it, arg))
@print_result.print_result
def f3(arg):
    return list(map(lambda i: i+' с опытом Python', arg))
@print_result.print_result
def f4(arg):
    return list(zip(arg, gen_random.gen_random(len(arg), 100000, 200000)))


if __name__ == '__main__':
    with cm_timer.cm_timer_1():
        f4(f3(f2(f1())))
