"""Создайте декоратор, который вызывает задекорированную функцию
 пока она не выполнится без исключений (но не более n раз - параметр
  декоратора). Если превышено количество попыток, должно
   быть возбуждено исключение типа TooManyErrors
"""


class TooManyErrors(Exception):
    def __init__(self, message='Ошибка не устранилась'):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


def counter(times):
    def decorator(func):
        def call(*args):
            i = 0
            while i < times:
                try:
                    func(*args)
                    return func
                    break
                except TypeError:
                    i += 1
                    print('Есть ошибка, необходимо устранить')
                    if i == times:
                        raise TooManyErrors
        return call
    return decorator


@counter(3)
def simple(n):
    if type(n) is str:
        print(n)
    else:
        print(n / 2)


simple(["pip"])
