"""

Создайте декоратор, который хранит результаты вызовов функции (за все
 время вызовов, не только текущий запуск программы)

"""


def decorator(function):
    saved_result = []

    def wrapper(*args, **kwargs):
        nonlocal saved_result
        result_func = function(*args, **kwargs)
        print(result_func)
        saved_result += [result_func]
        return saved_result

    return wrapper


@decorator
def function(a, b):
    return a + b


print(function(2, 3))
print(function(23, 3))
print(function(28, 31))
