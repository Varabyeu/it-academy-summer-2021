"""

Создайте декоратор, который хранит результаты вызовов функции (за все
 время вызовов, не только текущий запуск программы)

"""


# Cам декоратор
def dec(fun):
    def wrapper(a, b):
        result_fun = fun(a, b)
        try:
            f = open('text.txt', 'x')
            f.write(str(result_fun) + ' ')
            f.close()
        except FileExistsError:
            f = open('text.txt', 'a')
            f.write(str(result_fun) + ' ')

        return result_fun

    return wrapper


@dec
def func(a, b):
    return a + b


print(func(1, 2))
print(func(3111, 2))
print(func(7, 2))
# Вывод на экран значений предыдущих результатов из файла
f = open('text.txt', 'r')
str_ = f.read().split()
print([el for el in str_])
f.close()
