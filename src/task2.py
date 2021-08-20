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
def division(a):
    try:
        result = a / 2
    except TypeError:
        result = 'raised TypeError'
    return result


print(division("2"))
print(division(2))
print(division(2))
print(division(4))
print(division(8))
print(division("2"))
print(division(6))