"""Создайте декоратор, который вызывает задекорированную функцию
 пока она не выполнится без исключений (но не более n раз - параметр
  декоратора). Если превышено количество попыток, должно
   быть возбуждено исключение типа TooManyErrors
"""


class TooManyErrors(Exception):
    """Empty class of exceptions"""
    pass


def counter(n):
    """Counter of exceptions"""
    def decorator(func):
        """Decorates func to count"""
        def caller(*args):

            count = 0
            while n > count:
                result = func(*args)
                if type(result) is float:
                    break
                elif type(result) is float:
                    break
                else:
                    count += 1
                    if n == count:
                        raise TooManyErrors('Raised TooManyErrors')
        return caller
    return decorator


@counter(3)
def simple_func(a):
    try:
        result = a / 2
    except TypeError:
        result = 'raised TypeError'
    return result


print(simple_func("2"))
print(simple_func(2))
print(simple_func(2))
print(simple_func(4))
print(simple_func(8))
print(simple_func("2"))
print(simple_func(6))
