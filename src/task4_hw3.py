"""Оформите указанную задачу из прошлых домашних в виде функции и покройте
 тестами. Учтите, что в функцию могут быть переданы некорректные
  значения, здесь может пригодится ‘assertRaises’. Не нужно
   переделывать функцию для того чтобы она ловила все возможные
    ситуации сама.

    По условию дз выполняется task4 hw3
"""


def function(str_num):
    """Посчитайте, сколько в списке пар элементов
    
    Посчитайте, сколько в списке пар элементов, равных друг другу
    Дан список чисел. Посчитайте, сколько в нем пар элементов,
    равных друг другу. Считается, что любые два элемента,
    равные друг другу образуют одну пару, которую необходимо посчитать.
    Входные данные - строка из чисел, разделенная пробелами.
    Выходные данные - количество пар.
    Важно: 1 1 1 - это 3 пары, 1 1 1 1 - это 6 пар
    """

    list_num = str_num.split()
    list_temp = []
    dict_new = {}
    num_pares = 0

    for num in list_num:
        if num not in list_temp:
            list_temp.append(num)
        for num_norepeat in list_temp:
            count = list_num.count(num_norepeat)
            dict_new[num_norepeat] = count
    for values in dict_new.values():
        counter = values - 3
        if counter >= 0:
            num_pares += 3 * (2 ** counter)
        else:
            if 0 < values <= 2:
                num_pares += values - 1

    return num_pares
